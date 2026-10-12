kogus = 0
summa = 0
positiivsed = 0
negatiivsed = 0
paaris = 0
paaritud = 0

while True:
    arv = int(input("Sisesta arv: "))
    
    if arv == 0:
        break
        
    kogus += 1
    summa += arv
    
    if arv > 0:
        positiivsed += 1
    else:
        negatiivsed += 1
        
    if arv % 2 == 0:
        paaris += 1
    else:
        paaritud += 1

if kogus > 0:
    keskmine = round(summa / kogus, 2)
    
    print("\n--- TULEMUSED ---")
    print(f"Sisestatud arve: {kogus}")
    print(f"Summa: {summa}")
    print(f"Keskmine: {keskmine}")
    print(f"Positiivseid arve: {positiivsed}")
    print(f"Negatiivseid arve: {negatiivsed}")
    print(f"Paarisarve: {paaris}")
    print(f"Paarituid arve: {paaritud}")
else:
    print("Ühtegi arvu ei sisestatud.")