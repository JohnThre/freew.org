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

# Pascal

Canonical: https://freew.org/pascal/

Pascal and Object Pascal support for the Nova editor.

Pascal and Object Pascal support for Nova, with Free Pascal build, run, and diagnostics.

It highlights Free Pascal and Delphi source, lists units, types, and routines in the symbol list, and completes keywords, runtime names, and the names declared in the open file. Saving a file runs the Free Pascal compiler and marks errors in the editor. A Free Pascal task builds, runs, and cleans the program, and Format uses ptop.

- Highlighting and the symbol list: https://freew.org/pascal/highlight.jpg
- A compiler error after saving, listed in Nova's Issues sidebar: https://freew.org/pascal/diagnostics.jpg
- A 29-second tour with narration, made with a synthetic voice from ElevenLabs: https://freew.org/pascal/demo.mp4 (captions: https://freew.org/pascal/demo.vtt)

Transcript: Pascal for Nova, from Swipht Group. Open a Pascal or Object Pascal file, and Nova highlights it, with a symbol list for your classes and routines. Save, and Free Pascal checks your code, so errors appear right in the editor. Build, run, and clean from the Free Pascal task. Format with ptop, and start new programs and units from clips. It needs Nova 11 or later. Find Pascal in the Nova Extension Library.

## Surfaces

- Nova: Nova 11 or later on macOS. Install it from the Extension Library. https://extensions.panic.com/extensions/com.swiphtgroup/com.swiphtgroup.Pascal/
- Free Pascal: Optional. Build, run, clean, and save-time diagnostics use fpc on your PATH, or a compiler path set in preferences.
- Language server: Optional. Set an executable path in preferences. The extension does not download or bundle a server.

## Terms

- No public permission: The published license does not allow use, copying, or sharing. Written authorization from the author is required.
- Not free software: Proprietary. The license grants no other rights. The bundled Tree-sitter Pascal parser is MIT-licensed. https://github.com/JohnThre/Pascal.novaextension/blob/main/LICENSE

## Use

- Files: Pascal files with the extensions .pas, .pp, .inc, .dpr, .lpr, and .dpk.
- Source: https://github.com/JohnThre/Pascal.novaextension

Programming language: JavaScript.

Author: Pengfan Chang (Swipht Group). https://swiphtgroup.com/
