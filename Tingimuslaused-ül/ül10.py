küsimus = int(input("sisesta täisarv1: "))
küsimus2 = int(input("sisesta täisarv2: "))

if küsimus > küsimus2:
    print("Suurem arv on:", küsimus)
elif küsimus < küsimus2:   
    print("Suurem arv on:", küsimus2)
else:
    print("Arvud on võrdsed:", küsimus)
