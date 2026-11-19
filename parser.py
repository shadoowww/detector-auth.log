import re
lineas = [
    "Failed password for invalid user user1123123 from ::1 port 39132 ssh2",
    "Failed password for kali from ::1 port 34090 ssh2",
    "Accepted password for kali from ::1 port 34090 ssh2",
    "Failed password for invalid user svc-backup from 203.0.113.5 port 40022 ssh2",
]
patron = r"(Failed|Accepted) password for (?:invalid user )?(\S+) from (\S+) port (\d+)"
 
for linea in lineas:
    m = re.search(patron, linea)
    print(m.groups())
