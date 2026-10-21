fail = open("sisestatud_arvud.txt", "w")
for i in range(1, 6):
    küsimus = int(input(f"Sisesta {i}. täisarv: "))
    fail.write(str(küsimus) + "\n")
fail.close()

arvud = []
fail = open("sisestatud_arvud.txt", "r")
for rida in fail:
    arvud.append(int(rida))
fail.close()

summa = sum(arvud)
keskmine = summa / 5

print("\nSisestatud arvud:", arvud)
print("Summa:", summa)
print("Keskmine:", keskmine)
