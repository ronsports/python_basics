try:
    ridade_arv = 0
    mittetühjade = 0
    sõnade_arv = 0
    tähemärkide_arv = 0

    with open("tekst.txt", "r", encoding="UTF-8") as f:
        for rida in f:
            ridade_arv += 1
            tähemärkide_arv += len(rida)
            
            sõnad = rida.split()
            if sõnad:
                mittetühjade += 1
                sõnade_arv += len(sõnad)

    if ridade_arv > 0:
        keskminesõnu = round(sõnade_arv / ridade_arv, 2)
    else:
        keskminesõnu = 0

    
    print(f"Ridade arv: {ridade_arv}")
    print(f"Mittetühjade ridade arv: {mittetühjade}")
    print(f"Sõnade arv: {sõnade_arv}")
    print(f"Tähemärkide arv (koos tühikutega): {tähemärkide_arv}")
    print(f"Keskmine sõnade arv rea kohta: {keskminesõnu}")

except FileNotFoundError:
    print("pole")
