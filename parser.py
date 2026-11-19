import re

patron = r"(Failed|Accepted) password for (?:invalid user )?(\S+) from (\S+) port (\d+)"

def parsear_linea(linea):
    m = re.search(patron, linea)
    if m is None:
        return None
    return {
        "resultado": m.group(1),
        "usuario": m.group(2),
        "ip": m.group(3),
        "puerto": m.group(4),
    }

eventos = []
with open("sample/auth.log") as f:
    for linea in f:
        evento = parsear_linea(linea)
        if evento is not None:
            eventos.append(evento)

print(len(eventos))
for e in eventos:
    print(e)
