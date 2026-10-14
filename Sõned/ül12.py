küsimus = input("Lause: ")
küsimus2 = input("Otsitav: ")

indeks = küsimus.find(küsimus2)

if indeks != -1:
    print(f"Leitud indeksilt {indeks}.")
else:
    print("Tekstiosa puudub lausest.")