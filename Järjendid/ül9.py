ostukorv = []

for i in range(1, 6):
    küsimus = input(f"Sisesta toote {i}. nimi: ")
    ostukorv.append(küsimus)

print("Sinu ostukorv:", ostukorv)

toodete_arv = len(ostukorv)
print("Ostukorvis on tooteid:", toodete_arv)
