hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]

koguarv = len(hinded)
keskmine = sum(hinded) / koguarv

positiivsed = 0
mitterahuldavad = 0

for hinne in hinded:
    if hinne >= 3:
        positiivsed += 1
    else:
        mitterahuldavad += 1

sagedused = {}
for h in range(1, 6):
    sagedused[h] = hinded.count(h)

kige_sagedasem = 1
for h in range(2, 6):
    if sagedused[h] > sagedused[kige_sagedasem]:
        kige_sagedasem = h

print(f"Hinnete koguarv: {koguarv}")
print(f"Keskmine hinne: {keskmine:.2f}")
print(f"Kõige sagedamini esinev hinne: {kige_sagedasem}")
print(f"Positiivsete hinnete (3–5) arv: {positiivsed}")
print(f"Mitterahuldavate hinnete (1–2) arv: {mitterahuldavad}")

print("\nHinnete jaotus diagrammina:")
for h in range(1, 6):
    tarnid = "*" * sagedused[h]
    print(f"Hinne {h}: {tarnid} ({sagedused[h]} tk)")
