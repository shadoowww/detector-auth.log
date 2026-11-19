import re

patron = r"^(\S+) .*?(Failed|Accepted) password for (?:invalid user )?(\S+) from (\S+) port (\d+)"

def parsear_linea(linea):
    m = re.search(patron, linea)
    if m is None:
        return None
    return {
	"fecha": m.group(1),
        "resultado": m.group(2),
        "usuario": m.group(3),
        "ip": m.group(4),
        "puerto": m.group(5),
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
