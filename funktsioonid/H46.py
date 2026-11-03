def liida(a, b):
    return a + b

def lahuta(a, b):
    return a - b

def korruta(a, b):
    return a * b

def jaga(a, b):
    if b == 0:
        return "Viga: Nulliga ei saa jagada!"
    return a / b

while True:
    print("\n--- Taskukalkulaator ---")
    print("1. Liitmine (+)")
    print("2. Lahutamine (-)")
    print("3. Korrutamine (*)")
    print("4. Jagamine (/)")
    print("5. Lõpeta programm")
    
    valik = input("Vali tehe (1-5): ")
    
    if valik == "5":
        print("Kalkulaatori töö on lõpetatud. Head päeva!")
        break
        
    if valik in ("1", "2", "3", "4"):
        arv1 = float(input("Sisesta esimene arv: "))
        arv2 = float(input("Sisesta teine arv: "))
        
        if valik == "1":
            tulemus = liida(arv1, arv2)
            print(f"Tulemus: {arv1} + {arv2} = {tulemus}")
        elif valik == "2":
            tulemus = lahuta(arv1, arv2)
            print(f"Tulemus: {arv1} - {arv2} = {tulemus}")
        elif valik == "3":
            tulemus = korruta(arv1, arv2)
            print(f"Tulemus: {arv1} * {arv2} = {tulemus}")
        elif valik == "4":
            tulemus = jaga(arv1, arv2)
            if isinstance(tulemus, str):
                print(tulemus)
            else:
                print(f"Tulemus: {arv1} / {arv2} = {tulemus}")
    else:
        print("Vigane valik! Palun vali number vahemikus 1-5.")
