nimi = input("sisesta oma nimi: ")
punktisumma = int(input("sisesta punktisumma: "))
puudumiste_arv = int(input("sisesta puudumiste arv: "))
kas_kõik_tööd_tehtud = input("kas kõik tööd on tehtud? (jah/ei): ")

print("Tere, " + nimi + "!")

if punktisumma >= 90:
    print("hinnet on 5")
elif punktisumma >= 75:
    print("hinnet on 4")
elif punktisumma >= 50:
    print("hinnet on 3")
elif punktisumma >= 49:
    print("hinnet on 2")
else:
    print("hinnet on 1")

    if puudumiste_arv > 10:
        print("hoiatus!")

if kas_kõik_tööd_tehtud == "ei":
    print("kõik tööd pole esitatud")
else:
    print("kõik tööd on esitatud")

    if punktisumma >= 3 and puudumiste_arv < 10 and kas_kõik_tööd_tehtud == "jah":
        print("Aine on läbitud")
    else:
        print("aine ei ole läbitud")