arvud = []

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        arvud.append(int(rida.strip()))

print(f"Järjend: {arvud}")

suurim = max(arvud)
vaikeim = min(arvud)
keskmine = sum(arvud) / len(arvud)

arvud.sort()

print(f"Suurim arv: {suurim}")
print(f"Väikseim arv: {vaikeim}")
print(f"Keskmine: {keskmine}")
print(f"Kasvavas järjekorras: {arvud}")
