summa = 0.0
tooteid = 0

hind = float(input("Sisesta hind: "))

while hind != 0:
    summa = summa + hind
    tooteid = tooteid + 1
    hind = float(input("Sisesta hind: "))

print(f"Tooteid: {tooteid}")
print(f"Kokku: {summa:.2f} €")
