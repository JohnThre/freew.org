#!/usr/bin/env python3
# freew.org lists apps and repositories and states the terms of each.
# Copyright (C) 2026 Pengfan Chang
# Contact: https://swiphtgroup.com/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Check that the hand-written catalog agrees with itself.

The catalog is repeated in many files. This script reads them and reports
where they disagree. It writes nothing. Run it from anywhere:

    python3 tools/check-catalog.py

It exits with status 1 if it finds a problem. Notes do not change the status.
"""

import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ("pricing", "donate")  # directories with a page that is not a catalog entry
MAX_DESCRIPTION = 160
NS = {"s": "https://freew.org/ns/site"}

problems = []
notes = []


def problem(where, text):
    problems.append(f"{where}: {text}")


def note(where, text):
    notes.append(f"{where}: {text}")


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def line_of(text, needle):
    i = text.find(needle)
    return text.count("\n", 0, i) + 1 if i >= 0 else 1


def jsonld(rel, text):
    nodes = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            nodes += json.loads(m.group(1)).get("@graph", [])
        except json.JSONDecodeError as e:
            problem(f"{rel}:{line_of(text, m.group(1))}", f"JSON-LD does not parse: {e}")
    return nodes


def meta(text, attr):
    m = re.search(rf'<meta {attr} content="(.*?)">', text)
    return html.unescape(m.group(1)) if m else None


def in_order(where, names, what):
    want = sorted(names, key=str.casefold)
    if names != want:
        problem(where, f"{what} is not in alphabetical order: {', '.join(names)}")


# 1. Entries: every directory with an index.html that is not a plain page.
entries = sorted(
    p.parent.name
    for p in ROOT.glob("*/index.html")
    if p.parent.name not in PAGES
)
name = {}
free = {}

site_xml = read("site.xml")
site = ET.fromstring(site_xml)
works = {w.get("id"): w for w in site.findall(".//s:work", NS)}

for e in entries:
    rel = f"{e}/index.html"
    text = read(rel)
    m = re.search(r'<h1 itemprop="name">(.*?)</h1>', text)
    name[e] = html.unescape(m.group(1)) if m else e
    w = works.get(e)
    if w is None:
        problem("site.xml", f"no <work id=\"{e}\">")
        continue
    free[e] = w.findtext("s:freedom", namespaces=NS) == "free-software"

by_name = sorted(entries, key=lambda e: name[e].casefold())

# 2. Presence in every mirror.
mirrors = {
    "index.html": lambda e: f'href="/{e}/"',
    "pricing/index.html": lambda e: f'href="/{e}/"',
    "404.html": lambda e: f'href="/{e}/"',
    "index.html.md": lambda e: f"https://freew.org/{e}/",
    "pricing/index.html.md": lambda e: f"https://freew.org/{e}/",
    "sitemap.xml": lambda e: f"<loc>https://freew.org/{e}/</loc>",
    "llms.txt": lambda e: f"https://freew.org/{e}/index.html.md",
    "README.md": lambda e: f"https://freew.org/{e}/",
}
for rel, needle in mirrors.items():
    text = read(rel)
    found = [e for e in entries if needle(e) in text]
    for e in entries:
        if e not in found:
            problem(rel, f"{name[e]} ({e}) is missing")
    # Order of first appearance. The HTML pages group entries by licence, so
    # only the flat lists are checked for order.
    if rel in ("sitemap.xml", "llms.txt", "README.md", "pricing/index.html.md"):
        seen = sorted(found, key=lambda e: text.index(needle(e)))
        in_order(rel, [name[e] for e in seen], "the catalog")

for rel in ("index.html", "pricing/index.html"):
    text = read(rel)
    lists = [n for n in jsonld(rel, text) if n.get("@type") == "ItemList"]
    if not lists:
        problem(rel, "no ItemList in the JSON-LD")
        continue
    items = lists[0]["itemListElement"]
    urls = [i["url"] for i in items]
    for e in entries:
        if f"https://freew.org/{e}/" not in urls:
            problem(rel, f"{name[e]} ({e}) is missing from the JSON-LD ItemList")
    in_order(rel, [i["name"] for i in items], "the JSON-LD ItemList")
    if [i["position"] for i in items] != list(range(1, len(items) + 1)):
        problem(rel, "ItemList positions do not count from 1")

in_order("site.xml", [w.findtext("s:name", namespaces=NS) for w in works.values()], "the <work> list")
for wid in works:
    if wid not in entries:
        problem("site.xml", f"<work id=\"{wid}\"> has no directory")

# The sentence that names only the proprietary entries, wherever it appears.
proprietary = [name[e] for e in by_name if not free.get(e, True)]
free_names = [name[e] for e in by_name if free.get(e, False)]
scan = list(ROOT.glob("*.html")) + list(ROOT.glob("*/index.html")) + list(ROOT.glob("*.md")) + list(ROOT.glob("*/*.md"))
scan += [ROOT / "site.xml", ROOT / "llms.txt"]
for p in scan:
    if p.name == "CLAUDE.md":
        continue
    text = p.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), 1):
        for sentence in re.split(r"(?<=[a-z)])\. |[<>\"]", line):
            if not all(n in sentence for n in proprietary) or any(n in sentence for n in free_names):
                continue
            places = [sentence.index(n) for n in proprietary]
            if places != sorted(places):
                problem(f"{p.relative_to(ROOT)}:{number}", "proprietary entries are not in alphabetical order")

# 3. Each HTML page: descriptions, licensing, head links.
html_pages = ["index.html", "404.html"] + [f"{d}/index.html" for d in list(PAGES) + entries]
versions = {"icons": set(), "css": set()}
header_ref = None

for rel in html_pages:
    text = read(rel)
    nodes = jsonld(rel, text)
    d = meta(text, 'name="description"')
    if rel != "404.html":
        og = meta(text, 'property="og:description"')
        tw = meta(text, 'name="twitter:description"')
        if not (d == og == tw):
            problem(f"{rel}:{line_of(text, 'name=\"description\"')}", "meta, og and twitter descriptions differ")
        if d and len(d) > MAX_DESCRIPTION:
            problem(f"{rel}:{line_of(text, 'name=\"description\"')}", f"meta description is {len(d)} characters, over {MAX_DESCRIPTION}")
        twin = rel + ".md"
        if f'<link rel="alternate" type="text/markdown" href="https://freew.org/{twin}">' not in text:
            problem(rel, f"no markdown alternate link to {twin}")
        if not (ROOT / twin).is_file():
            problem(rel, f"{twin} does not exist")
        if f'<link rel="canonical" href="https://freew.org/{rel[:-10]}">' not in text:
            problem(rel, "canonical link is missing or wrong")
    versions["icons"].update(re.findall(r'(?:favicon|apple-touch-icon|site\.webmanifest)[^"]*\?v=([^"]+)"', text))
    m = re.search(r'href="/css/site\.css(?:\?v=([^"]+))?"', text)
    versions["css"].add(m.group(1) if m else None)

    # Local files that the page points at.
    refs = re.findall(r'(?:href|src|poster)="(/[^"#?]*)', text)
    for srcset in re.findall(r'srcset="([^"]*)"', text):
        refs += [part.split()[0] for part in srcset.split(",")]
    for ref in set(refs):
        target = ROOT / ref.lstrip("/")
        if not (target.is_file() or (target / "index.html").is_file()):
            problem(f"{rel}:{line_of(text, ref)}", f"{ref} does not exist")

    e = rel.split("/")[0]
    if e not in entries:
        continue
    work = next((n for n in nodes if n.get("@type") == "SoftwareSourceCode"), None)
    if work is None:
        problem(rel, "no SoftwareSourceCode node in the JSON-LD")
        continue
    micro = meta(text, 'itemprop="description"')
    xml_summary = works[e].findtext("s:summary", namespaces=NS) if e in works else None
    if not (work.get("description") == micro == xml_summary):
        problem(rel, "the JSON-LD description, the microdata description and the site.xml summary differ")
    if e not in works:
        continue
    w = works[e]
    charge = w.findtext("s:charge", namespaces=NS)
    lic = w.find("s:freedom", NS).get("license") or ""
    low = text.lower()
    if free[e]:
        if work.get("isAccessibleForFree") is not True:
            problem(rel, 'free software entry needs "isAccessibleForFree": true')
        if charge != "free":
            problem("site.xml", f"{e}: free software entry needs <charge>free</charge>")
        if not lic.startswith("GPL-3.0"):
            problem("site.xml", f"{e}: unexpected license \"{lic}\"")
        if "gnu.org/licenses/" not in str(work.get("license")):
            problem(rel, "free software entry needs a gnu.org license URL")
        if f"Free software · {lic}<" not in text:
            problem(rel, f"the badge does not say \"Free software · {lic}\"")
    else:
        if work.get("isAccessibleForFree") is not False:
            problem(rel, 'proprietary entry needs "isAccessibleForFree": false')
        if charge != "no-public-permission":
            problem("site.xml", f"{e}: proprietary entry needs <charge>no-public-permission</charge>")
        if lic != "proprietary":
            problem("site.xml", f"{e}: proprietary entry needs license=\"proprietary\"")
        for phrase in ("proprietary", "not free software", "grants no permission to use it"):
            if phrase not in (d or "").lower():
                problem(rel, f"the meta description must say \"{phrase}\"")
        for wrong in ("free of charge", 'class="badge free"'):
            if wrong in low:
                problem(f"{rel}:{line_of(low, wrong)}", f"a proprietary entry must not say \"{wrong}\"")
        if "license" not in work:
            note(rel, "no license URL is published for this proprietary entry")

for kind, seen in versions.items():
    if len(seen) != 1:
        problem("head", f"pages use different {kind} cache-busting strings: {sorted(map(str, seen))}")

# 4. The AGPL header, the same text in every file.
def header_lines(text):
    lines = [l for l in text.splitlines()[:25] if not l.startswith(("#!", "<?xml"))]
    lines = [re.sub(r"^# ?", "", l).strip() for l in lines]
    lines = [l for l in lines if l not in ("<!--", "-->", "/*", "*/")]
    return lines[:15]

header_ref = header_lines(read("index.html"))
with_header = html_pages + [p + ".md" for p in html_pages if p != "404.html"] + [
    "README.md", "site.xml", "sitemap.xml", "llms.txt", "robots.txt", "_headers", "css/site.css", "tools/check-catalog.py",
]
for rel in with_header:
    if not (ROOT / rel).is_file():
        problem(rel, "file does not exist")
    elif header_lines(read(rel)) != header_ref:
        problem(f"{rel}:1", "the license header is missing or differs from index.html")

for n in notes:
    print("note:", n)
for p in problems:
    print(p)
print(f"{len(entries)} entries, {len(problems)} problem(s), {len(notes)} note(s).")
sys.exit(1 if problems else 0)
