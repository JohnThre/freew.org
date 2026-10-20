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

# Air Traffic Control (ATC)

Canonical: https://freew.org/atc/

Runs and coordinates coding agents from the Nova editor.

Runs Claude Code, Codex, Cursor, Antigravity, OpenCode, Pi, JetBrains Junie, and Grok from Nova, each flight in its own Git worktree, with diff review, races, hand-offs, and merge or pull request.

It gives a task to Claude Code, Codex, Cursor, Antigravity, OpenCode, Pi, JetBrains Junie, or Grok. Each task is a flight: one agent session, by default in its own Git worktree on an atc/ branch, so several agents can work at the same time without touching your checkout. A live Markdown transcript shows each turn with its tokens and cost. When a flight lands, you review its diff, write comments on lines starting with >> in the diff, and send them back to the same agent session. Editing turns in a worktree get checkpoints, so you can undo the last turn. A race sends one prompt to several agents, or to several sessions of one agent, and another agent can judge the results. You can hand a flight off to a different agent, run your test command and send failures back, fan one prompt out over files or TODO comments, and merge a flight as one commit, as one commit per turn, or as a pull request.

- A flight's live transcript, with its changed files in the sidebar: https://freew.org/atc/transcript.jpg
- A review comment written right in a flight's diff: https://freew.org/atc/diff.jpg
- Compare Race for a best-of-two race: https://freew.org/atc/race.jpg
- A 44-second tour with narration, made with a synthetic voice from ElevenLabs: https://freew.org/atc/demo.mp4 (captions: https://freew.org/atc/demo.vtt)

Transcript: Air Traffic Control for Nova, from Swipht Group. It runs coding agents right in Nova: Claude Code, Codex, Cursor, Antigravity, OpenCode, Pi, JetBrains Junie, and Grok. Write a flight plan, and take off. Each flight works in its own Git worktree, and you follow it in a live transcript. When it lands, review the diff, write a comment right in it, and send it back to the same agent session. Race several agents, or several sessions of one, and let another agent judge the results. Then merge the winner. It needs Nova 11 or later, and at least one agent CLI. Find Air Traffic Control in the Nova Extension Library.

## Surfaces

- Nova: Nova 11 or later on macOS. Install it from the Extension Library. https://extensions.panic.com/extensions/com.swiphtgroup/com.swiphtgroup.AirTrafficControlATC/
- Git: Required. Flights work in Git worktrees, and merges and discards go through Git.
- Agent CLIs: At least one, installed and signed in: Claude Code, Codex, Cursor, Antigravity, OpenCode, Pi, JetBrains Junie, or Grok. The extension runs your installed command-line tools and includes none of their code.

## Terms

- No public permission: The published license does not allow use, copying, or sharing. Written authorization from the author is required.
- Not free software: Proprietary. The license grants no other rights. The agents are the products and trademarks of their respective owners. https://github.com/JohnThre/AirTrafficControl.novaextension/blob/main/LICENSE

## Use

- Sidebar: Air Traffic Control, with Flights and the Hangar. A Flight Plan file starts each flight.
- Source: https://github.com/JohnThre/AirTrafficControl.novaextension

Programming language: JavaScript.

Author: Pengfan Chang (Swipht Group). https://swiphtgroup.com/
