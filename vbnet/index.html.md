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

# VB.NET

Canonical: https://freew.org/vbnet/

Visual Basic .NET support for the Nova editor.

Visual Basic .NET support for Nova, with .NET SDK build, run, test, publish, and diagnostics.

It highlights Visual Basic .NET and lists namespaces, types, and members in the symbol list. Completions include the names declared in the open file and in the other files of its project. Format runs dotnet format on the editor's text, and commands sort Imports, add the missing End statement of a block, and insert XML doc comments. Saving a file builds its project, once you allow checks for the folder, and marks errors in the editor. Tasks build, run, clean, test, and watch the project. Run Test at Cursor and Run Tests in File run only the tests you choose. Publish makes a portable or self-contained app. Commands add, update, and remove NuGet packages, add project references, and create projects from the Console App, Class Library, xUnit, MSTest, and NUnit templates.

- Highlighting and the symbol list: https://freew.org/vbnet/highlight.jpg
- Run Test at Cursor in an xUnit project: https://freew.org/vbnet/tests.jpg
- A compiler error after saving, listed in Nova's Issues sidebar: https://freew.org/vbnet/diagnostics.jpg

## Surfaces

- Nova: Nova 11 or later on macOS. Install it from the Extension Library. https://extensions.panic.com/extensions/com.swiphtgroup/com.swiphtgroup.VBNET/
- .NET SDK: Optional. Build, run, tests, publishing, formatting, packages, and save-time diagnostics use dotnet from /usr/local/share/dotnet, ~/.dotnet, Homebrew, or your PATH, or a path set in preferences.
- Language server: Optional. Set an executable path in preferences. The extension does not download or bundle a server.

## Terms

- No public permission: The published license does not allow use, copying, or sharing. Written authorization from the author is required.
- Not free software: Proprietary. The license grants no other rights. The bundled Tree-sitter VB.NET parser is MIT-licensed. https://github.com/JohnThre/VB.NET.novaextension/blob/main/LICENSE

## Use

- Files: Visual Basic .NET files with the extension .vb.
- Source: https://github.com/JohnThre/VB.NET.novaextension

Programming language: JavaScript.

Author: Pengfan Chang (Swipht Group). https://swiphtgroup.com/
