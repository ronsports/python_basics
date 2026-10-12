küsimus = int(input("Mitu arvu soovid sisestada? "))

summa = 0

for i in range(küsimus):
    arv = int(input("Sisesta arv: "))
    summa += arv

keskmine = summa / küsimus

print(f"Summa: {summa}")
print(f"Keskmine: {keskmine}")
