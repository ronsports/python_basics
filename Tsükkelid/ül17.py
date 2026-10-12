oige_parool = "python123"
katsed = 0
maksimaalselt_katseid = 3

while katsed < maksimaalselt_katseid:
    Küsimus = input("Sisesta parool: ")
    katsed += 1
    
    if Küsimus == oige_parool:
        print("Ligipääs lubatud!")
        break
    else:
        if katsed < maksimaalselt_katseid:
            print("Vale parool!")
        else:
            print("Ligipääs blokeeritud!")