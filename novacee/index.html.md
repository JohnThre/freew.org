<!--
freew.org presents apps and repositories you can use without paying.
Copyright (C) 2026 Pengfan Chang
Contact: https://swiphtgroup.com/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
-->

# NovaCEE Offline

Canonical: https://freew.org/novacee/

Offline docs and developer tools in the Nova editor, for Macs without a network connection.

Searches Dash-format docsets in Nova without a network connection, installs docsets, a search index, and toolchains only after their SHA-256 hashes match a manifest, and runs those toolchains, with Library Health and Disk Usage.

It is built for Macs that never reach the internet. You copy payloads onto the machine ahead of time: docsets, a full-text search index, and toolchains. Each payload is checked against its SHA-256 hash in a manifest before it installs, and every path in an archive is checked before it unpacks. One search, ⌘⇧D, covers every installed docset. It uses the search index when it is installed and scans each docset otherwise. Results are ranked, a type: filter keeps one kind of entry, and Look Up Symbol searches for the word under the cursor in the docsets for the document's language. You can search one docset, reinstall, update, or uninstall a payload, see how much disk each docset uses, and check the library's health: the manifest, every hash, what is not installed yet, and free space. Run Tool runs an installed toolchain with new arguments, the last arguments, or a saved preset, and checks the tool's hash before every run. The extension makes no network requests.

- One search across every installed docset: https://freew.org/novacee/search.jpg
- A Go docset page, read in Nova without a network connection: https://freew.org/novacee/doc.jpg
- Library Health, with the last result in the sidebar: https://freew.org/novacee/health.jpg
- Run Tool, with the last arguments and saved presets: https://freew.org/novacee/tool.jpg
- A 42-second tour with narration, made with a synthetic voice from ElevenLabs: https://freew.org/novacee/demo.mp4 (captions: https://freew.org/novacee/demo.vtt)

Transcript: NovaCEE Offline for Nova, from Swipht Group. It brings API docs and developer tools into Nova, on Macs that never go online. Copy the payloads onto the machine ahead of time. Each one is checked against its SHA-256 hash before it installs. Search every installed docset from one palette, and read the page right in Nova. Library Health checks the manifest, the hashes, and the free space. Run the tools you brought along, again with the last arguments or a saved preset, and see how much disk each docset uses. It makes no network requests. Find NovaCEE Offline in the Nova Extension Library.

## Surfaces

- Nova: Nova on macOS. Install it from the Extension Library. https://extensions.panic.com/extensions/com.swiphtgroup/com.swiphtgroup.OfflineMVP/
- Payloads: Copied onto the machine ahead of time, with a manifest of SHA-256 hashes. Docsets use the Dash format with a searchIndex table. Each docset and tool keeps its own license.
- Network: None. The extension makes no network requests.

## Terms

- No public permission: The published license does not allow use, copying, or sharing. Written authorization from the author is required.
- Not free software: Proprietary. The license grants no other rights. Docsets and tools you install keep their own licenses.

## Use

- Sidebar: Offline Library, with Docsets, Tools, and Verification.
- Search: Editor › Search Offline Docs, ⌘⇧D. Look Up Symbol, ⌃⇧D.
- Library folder: ~/Library/Application Support/NovaCEE Offline by default. Set Offline Library Folder in the extension preferences.

Programming language: JavaScript.

Author: Pengfan Chang (Swipht Group). https://swiphtgroup.com/
