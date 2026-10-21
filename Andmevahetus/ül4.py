with open("/home/ron/repositories/python_work/Andmevahetus/nimed.txt", encoding="UTF-8") as f:
    read = f.readlines()

    if read:
        esimene_nimi = read[0].strip()
        viimane_nimi = read[-1].strip()

print("Esimene nimi:", esimene_nimi)
print("Viimane nimi:", viimane_nimi)
