failinimi = "kontaktid.txt"

while True:
    otsitav_nimi = input("\nSisesta otsitav nimi (või lõpetamiseks 'stopp'): ").strip()
    
    if otsitav_nimi.lower() == "stopp":
        print("Programmi töö on lõpetatud.")
        break
        
    if len(otsitav_nimi) == 0:
        print("Palun sisesta otsinguks mõni tähemärk.")
        continue
        
    leitud = False
    
    with open(failinimi, "r", encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.strip().split(";")
            if len(osad) == 3:
                nimi = osad[0]
                email = osad[1]
                telefon = osad[2]
                
                if otsitav_nimi.lower() in nimi.lower():
                    print(f"\nKontakt: {nimi}")
                    print(f"E-post: {email}")
                    print(f"Telefon: {telefon}")
                    leitud = True
                    
    if not leitud:
        print("Kontakti ei leitud.")
