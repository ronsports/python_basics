a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
c = float(input("Kolmas arv: "))

if a >= b and a >= c:
    suurim = a
elif b >= a and b >= c:
    suurim = b
else:
    suurim = c

print(f"Suurim arv on {suurim}.")
