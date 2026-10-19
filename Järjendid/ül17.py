küsimus = int(input("Algus: "))
lopp = int(input("Lõpp: "))

summa = 0

for i in range(küsimus, lopp + 1):
    summa = summa + i

print("Summa:", summa)
