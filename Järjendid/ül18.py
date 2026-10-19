arvud = [7, 12, 19, 24, 31, 46, 53, 60, 72]

paaris_arv = 0
paaritu_arv = 0
paaris_summa = 0
paaritu_summa = 0

for arv in arvud:
    if arv % 2 == 0:
        paaris_arv = paaris_arv + 1
        paaris_summa = paaris_summa + arv
    else:
        paaritu_arv = paaritu_arv + 1
        paaritu_summa = paaritu_summa + arv

print("Paarisarvude arv:", paaris_arv)
print("Paaritute arvude arv:", paaritu_arv)
print("Paarisarvude summa:", paaris_summa)
print("Paaritute arvude summa:", paaritu_summa)
