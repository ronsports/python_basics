arvud = [-12, 5, 0, 18, -7, 23, -3, 9]

positiivsed_arv = 0
negatiivsed_arv = 0
nullid_arv = 0
positiivsed_summa = 0
negatiivsed_jarjend = []

for arv in arvud:
    if arv > 0:
        positiivsed_arv = positiivsed_arv + 1
        positiivsed_summa = positiivsed_summa + arv
    elif arv < 0:
        negatiivsed_arv = negatiivsed_arv + 1
        negatiivsed_jarjend.append(arv)
    else:
        nullid_arv = nullid_arv + 1

print("Positiivsed arvud:", positiivsed_arv)
print("Negatiivsed arvud:", negatiivsed_arv)
print("Nullid:", nullid_arv)
print("Positiivsete summa:", positiivsed_summa)
print("Negatiivsete järjend:", negatiivsed_jarjend)