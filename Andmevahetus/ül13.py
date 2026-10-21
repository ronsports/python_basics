try:
    enim_hindeid_arv = 0
    enim_hindeid_õpilane = ""

    with open("õpilased.txt", encoding="UTF-8") as f:
        for rida in f:
            tükid = rida.split()
            if tükid: 
                nimi = tükid[0] 
                hinded = [int(h) for h in tükid[1:]] 
                
                kesk = round(sum(hinded) / len(hinded), 2)
                
                print(f"Õpilane: {nimi}, hinded: {hinded}, keskmine: {kesk}")
                
                if len(hinded) > enim_hindeid_arv:
                    enim_hindeid_arv = len(hinded)
                    enim_hindeid_õpilane = nimi

        print("-" * 40)
        print(f"Kõige rohkem hindeid on õpilasel: {enim_hindeid_õpilane} ({enim_hindeid_arv} hinnet)")

except FileNotFoundError:
    print("pole")
