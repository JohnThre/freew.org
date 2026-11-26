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
"""Check that the pure HTML & CSS catalog agrees with itself.

This read-only script verifies catalog completeness, alphabetical ordering,
license wording, local asset links, strict HTML+CSS-only constraints (zero
JS/TS files, zero <script> tags, zero inline styles/event handlers), retired
mirror absence, and consistent AGPLv3+ headers. Run it from anywhere:

    python3 tools/check-catalog.py

It exits with status 1 if it finds a problem. Notes do not change the status.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ("pricing", "donate")  # directories with a page that is not a catalog entry
MAX_DESCRIPTION = 160
SKIP_DIRS = {".git", ".playwright-mcp", ".claude", ".cursor"}

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


def meta(text, attr):
    m = re.search(rf'<meta {attr} content="(.*?)">', text)
    return html.unescape(m.group(1)) if m else None


def in_order(where, names, what):
    want = sorted(names, key=str.casefold)
    if names != want:
        problem(where, f"{what} is not in alphabetical order: {', '.join(names)}")


# 0. Strict HTML & CSS only: no JS/TS files and no retired mirror files.
for path in ROOT.rglob("*"):
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if path.is_file() and path.suffix.lower() in (".js", ".ts", ".mjs", ".cjs", ".jsx", ".tsx"):
        problem(str(path.relative_to(ROOT)), "JavaScript/TypeScript file is not allowed")

for retired in ["site.xml", "llms.txt", "index.html.md"] + [
    str(p.relative_to(ROOT)) for p in ROOT.glob("*/index.html.md")
]:
    if (ROOT / retired).exists():
        problem(retired, "retired mirror file should not exist")

# 1. Entries: every directory with an index.html that is not a plain page.
entries = sorted(
    p.parent.name
    for p in ROOT.glob("*/index.html")
    if p.parent.name not in PAGES
)
name = {}
free = {}

for e in entries:
    rel = f"{e}/index.html"
    text = read(rel)
    m = re.search(r'<h1 itemprop="name">(.*?)</h1>', text)
    name[e] = html.unescape(m.group(1)) if m else e
    acc = meta(text, 'itemprop="isAccessibleForFree"')
    if acc not in ("true", "false"):
        problem(rel, 'missing microdata <meta itemprop="isAccessibleForFree" content="true|false">')
        continue
    free[e] = acc == "true"

by_name = sorted(entries, key=lambda e: name[e].casefold())

# 2. Presence in every index/listing file.
listings = {
    "index.html": lambda e: f'href="/{e}/"',
    "pricing/index.html": lambda e: f'href="/{e}/"',
    "404.html": lambda e: f'href="/{e}/"',
    "sitemap.xml": lambda e: f"<loc>https://freew.org/{e}/</loc>",
    "README.md": lambda e: f"https://freew.org/{e}/",
}
for rel, needle in listings.items():
    text = read(rel)
    found = [e for e in entries if needle(e) in text]
    for e in entries:
        if e not in found:
            problem(rel, f"{name[e]} ({e}) is missing")
    if rel in ("pricing/index.html", "sitemap.xml", "README.md"):
        seen = sorted(found, key=lambda e: text.index(needle(e)))
        in_order(rel, [name[e] for e in seen], "the catalog")

# The sentence that names only the proprietary entries, wherever it appears.
proprietary = [name[e] for e in by_name if not free.get(e, True)]
free_names = [name[e] for e in by_name if free.get(e, False)]
scan = list(ROOT.glob("*.html")) + list(ROOT.glob("*/index.html")) + [ROOT / "README.md"]
for p in scan:
    text = p.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), 1):
        for sentence in re.split(r"(?<=[a-z)])\. |[<>\"]", line):
            if not all(n in sentence for n in proprietary) or any(n in sentence for n in free_names):
                continue
            places = [sentence.index(n) for n in proprietary]
            if places != sorted(places):
                problem(f"{p.relative_to(ROOT)}:{number}", "proprietary entries are not in alphabetical order")

# 3. Each HTML page: pure HTML+CSS constraints, descriptions, licensing, head links.
html_pages = ["index.html", "404.html"] + [f"{d}/index.html" for d in list(PAGES) + entries]
versions = {"icons": set(), "css": set()}

for rel in html_pages:
    text = read(rel)
    low = text.lower()

    if "<script" in low:
        problem(f"{rel}:{line_of(low, '<script')}", "<script> tag is not allowed")
    if re.search(r'\sstyle\s*=', text, re.I):
        problem(rel, "inline style attribute is not allowed")
    if re.search(r'\son[a-z]+\s*=', text, re.I):
        problem(rel, "inline event handler attribute is not allowed")
    for banned in ("nowpayments", "signal support", "llms.txt", "index.html.md", "site.xml"):
        if banned in low:
            problem(f"{rel}:{line_of(low, banned)}", f"disallowed reference \"{banned}\"")

    d = meta(text, 'name="description"')
    if rel != "404.html":
        og = meta(text, 'property="og:description"')
        tw = meta(text, 'name="twitter:description"')
        if not (d == og == tw):
            problem(f"{rel}:{line_of(text, 'name=\"description\"')}", "meta, og and twitter descriptions differ")
        if d and len(d) > MAX_DESCRIPTION:
            problem(f"{rel}:{line_of(text, 'name=\"description\"')}", f"meta description is {len(d)} characters, over {MAX_DESCRIPTION}")
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
    if 'itemtype="https://schema.org/SoftwareSourceCode"' not in text:
        problem(rel, "no SoftwareSourceCode microdata block")
        continue
    if not meta(text, 'itemprop="description"'):
        problem(rel, "missing SoftwareSourceCode microdata description")

    lic_match = re.search(r'<link itemprop="license" href="([^"]+)">', text)
    lic_url = lic_match.group(1) if lic_match else None

    if free[e]:
        if not lic_url or "gnu.org/licenses/" not in lic_url:
            problem(rel, "free software entry needs a gnu.org license microdata link")
        if not re.search(r'<span class="badge free">Free software · GPL-3\.0(?:-or-later)?</span>', text):
            problem(rel, "free software entry badge is missing or unexpected")
    else:
        for phrase in ("proprietary", "not free software", "grants no permission to use it"):
            if phrase not in (d or "").lower():
                problem(rel, f"the meta description must say \"{phrase}\"")
        for wrong in ("free of charge", 'class="badge free"'):
            if wrong in low:
                problem(f"{rel}:{line_of(low, wrong)}", f"a proprietary entry must not say \"{wrong}\"")
        if '<span class="badge restricted">Proprietary · no permission to use</span>' not in text:
            problem(rel, "proprietary entry badge is missing or unexpected")
        if not lic_url:
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
with_header = html_pages + [
    "README.md", "sitemap.xml", "robots.txt", "_headers", "css/site.css", "tools/check-catalog.py",
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
