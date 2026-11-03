linnade_arv = 0

with open("linnad.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        linn = rida.strip()
        print(linn)
        linnade_arv = linnade_arv + 1

print(f"\nKokku on failis {linnade_arv} linna.")
