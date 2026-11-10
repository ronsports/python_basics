def raha_eurodes(kastidearv, kilohindsentides):
    koguskg = kastidearv * 5
    eurot = koguskg * (kilohindsentides / 100)
    return round(eurot, 1)


def main():
    failinimi = input("Sisesta failinimi: ")
    kilohind = float(input("Sisesta kilohind (sendides): "))

    kokkueurodd = 0

    with open(failinimi, "r", encoding="UTF-8") as fail:
        for rida in fail:
            kastide_arv = int(rida.strip())
            kokkueurodd += raha_eurodes(kastide_arv, kilohind)

    print(f"Kokku: {round(kokkueurodd, 1)} eurot")



main()
