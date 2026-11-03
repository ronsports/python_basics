arvude_arv = 0
summa = 0

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        arv = int(rida.strip())
        summa = summa + arv
        arvude_arv = arvude_arv + 1

print(f"Arvude arv: {arvude_arv}")
print(f"Arvude summa: {summa}")
