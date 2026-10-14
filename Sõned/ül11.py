küsimus = input("Sisesta lause: ")
küsimus2 = input("Sisesta täht: ")

lause_madal = küsimus.lower()
täht_madal = küsimus2.lower()

kordi = lause_madal.count(täht_madal)
print("Täht {küsimus2} esineb {kordi} korda.")
