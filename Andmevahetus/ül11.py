try:
    with open("tekst.txt", encoding="UTF-8") as f:
        kõik_sõnad = []
        
        for rida in f:
            sõnad = rida.split()
            kõik_sõnad.extend(sõnad)

    if kõik_sõnad:
        pikk_sõna = max(kõik_sõnad, key=len)
        lühike_sõna = min(kõik_sõnad, key=len)
        
        print(f"Kõige pikem sõna: {pikk_sõna} ({len(pikk_sõna)} tähte)")
        print(f"Kõige lühem sõna: {lühike_sõna} ({len(lühike_sõna)} tähte)")
    else:
        print("Fail on tühi.")

except FileNotFoundError:
    print("Faili ei leitud!")
