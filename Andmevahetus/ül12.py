try:
    with open("hinded.txt", encoding="UTF-8") as f:
        õpilased = []
        hinded = []

        for rida in f:
            nimi, hinne_r = rida.split()
            hinne = int(hinne_r)

            õpilased.append((nimi, hinne))
            hinded.append(hinne)

    keskmine = round(sum(hinded) / len(hinded), 2)
    kõrg = max(hinded)
    minim = min(hinded)

    for hinne, nimi in õpilased:
        if hinne >= 4:

         print(nimi)


except FileNotFoundError:
    print("pole")


print(õpilased, hinded, keskmine, kõrg, minim)