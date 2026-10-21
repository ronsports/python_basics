küsimus = input("Sisesta toode: ").strip()

try:
    with open("tooted.txt", encoding="UTF-8") as f:
        read = [rida.strip() for rida in f if rida.strip()]
        
    otsitav = küsimus.lower()
    read_vaiketähtedega = [toode.lower() for toode in read]
    
    indeks = read_vaiketähtedega.index(otsitav)
    print(f"Leitud toode: {read[indeks]}")

except FileNotFoundError:
    print("Viga: faili 'tooted.txt' ei leitud.")
    
except ValueError:
    print(f"Toodet '{küsimus}' ei leitud nimekirjast.")
