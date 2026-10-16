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

# RockyBack

Canonical: https://freew.org/rockyback/

Prepares Rocky Linux 9 or AlmaLinux 9 and installs ClambBack.

Prepares a Rocky Linux 9 or AlmaLinux 9 VPS and installs a verified ClambBack release.

It updates the host, hardens common attack surfaces, checks DNS and TLS, then installs a signed ClambBack RPM. On AWS, it reminds you to open matching ports in the AWS firewall.

## Host

- System: Rocky Linux 9 or AlmaLinux 9 on x86_64.
- Access: Root or sudo, with SELinux enabled.
- Name: A real hostname whose DNS matches the public address.

## Terms

- No public permission: The published license does not allow use, copying, or sharing. Written authorization from the author is required.
- Not free software: Proprietary. The license grants no other rights. https://github.com/JohnThre/rockyback/blob/main/LICENSE

## Use

These steps apply only with the author's written authorization.

- SSH key: Install an SSH public key and confirm key login before running the installer.
- Installer: Run `./install.sh`. Interactive, `--dry-run`, or `--yes`.
- Source: https://github.com/JohnThre/rockyback

Programming language: Shell.

Author: Pengfan Chang (Swipht Group). https://swiphtgroup.com/
