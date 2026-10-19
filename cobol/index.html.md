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

# COBOL

Canonical: https://freew.org/cobol/

COBOL support for the Nova editor.

COBOL support for Nova in fixed and free format, with GnuCOBOL build, run, debugging, and diagnostics.

It highlights COBOL in fixed and free reference format, with SQL highlighting inside EXEC SQL blocks, and lists divisions, sections, paragraphs, files, and data items in the symbol list. Completions include the names declared in the copybooks a program copies. Go to Definition, Find References, and Rename Symbol work on data items, sections, and paragraphs, and Show Record Layout lists each field's offset, length, and picture. Commands convert between fixed and free format, align data clauses, and renumber or clear sequence areas. Saving a file runs GnuCOBOL and marks errors in the editor. A GnuCOBOL task builds, runs, and cleans the program, and a debug task runs it under lldb-dap.

- Highlighting and the symbol list: https://freew.org/cobol/highlight.jpg
- Show Record Layout for a record copied from a copybook: https://freew.org/cobol/layout.jpg
- A GnuCOBOL error after saving, listed in Nova's Issues sidebar: https://freew.org/cobol/diagnostics.jpg
- A 39-second tour with narration, made with a synthetic voice from ElevenLabs: https://freew.org/cobol/demo.mp4 (captions: https://freew.org/cobol/demo.vtt)

Transcript: COBOL for Nova, from Swipht Group. Open a COBOL program in fixed or free format, and Nova highlights it, including embedded SQL, with a symbol list for divisions, sections, and paragraphs. Completions follow your COPY statements into copybooks. Jump to definitions, find references, rename names, and see a record's offsets and lengths. Save, and GnuCOBOL checks your code, so errors appear right in the editor. Build, run, and debug from the GnuCOBOL tasks. It needs Nova 11 or later. Find COBOL in the Nova Extension Library.

## Surfaces

- Nova: Nova 11 or later on macOS. Install it from the Extension Library. https://extensions.panic.com/extensions/com.swiphtgroup/com.swiphtgroup.COBOL/
- GnuCOBOL: Optional. Build, run, clean, and save-time diagnostics use cobc on your PATH, or a compiler path set in preferences.
- Debugger: Optional. The debug task uses lldb-dap from Xcode or the Command Line Tools.
- Language server: Optional. Set an executable path in preferences. The extension does not download or bundle a server.

## Terms

- No public permission: The published license does not allow use, copying, or sharing. Written authorization from the author is required.
- Not free software: Proprietary. The license grants no other rights. The bundled Tree-sitter COBOL parser is MIT-licensed. https://github.com/JohnThre/COBOL.novaextension/blob/main/LICENSE

## Use

- Files: COBOL files with the extensions .cbl, .cob, .cobol, .pco, .cpy, .copy, and .cbx.
- Source: https://github.com/JohnThre/COBOL.novaextension

Programming language: JavaScript.

Author: Pengfan Chang (Swipht Group). https://swiphtgroup.com/
