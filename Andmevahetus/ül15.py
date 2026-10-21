


küsimus = input("Sisesta nimi: ")
küsimus2 = input("Sisesta vanus: ")
küsimus3 = input("Sisesta gmail: ")
f = open("andmed.txt", "w")
f.write(küsimus)
f.write(küsimus2)
f.write(küsimus3)
f.close()
