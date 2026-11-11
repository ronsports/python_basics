lause = input("Sisesta lause: ")

täishäälikud = "aeiouõäöü"
kokku = 0

a_arv = 0
e_arv = 0
i_arv = 0
o_arv = 0
u_arv = 0
õ_arv = 0
ä_arv = 0
ö_arv = 0
ü_arv = 0

for märk in lause.lower():
    if märk in täishäälikud:
        kokku = kokku + 1
        
        if märk == "a":
            a_arv = a_arv + 1
        elif märk == "e":
            e_arv = e_arv + 1
        elif märk == "i":
            i_arv = i_arv + 1
        elif märk == "o":
            o_arv = o_arv + 1
        elif märk == "u":
            u_arv = u_arv + 1
        elif märk == "õ":
            õ_arv = õ_arv + 1
        elif märk == "ä":
            ä_arv = ä_arv + 1
        elif märk == "ö":
            ö_arv = ö_arv + 1
        elif märk == "ü":
            ü_arv = ü_arv + 1

print(f"Täishäälikuid kokku: {kokku}")
print("Iga täishääliku arv:")
print(f"a: {a_arv}")
print(f"e: {e_arv}")
print(f"i: {i_arv}")
print(f"o: {o_arv}")
print(f"u: {u_arv}")
print(f"õ: {õ_arv}")
print(f"ä: {ä_arv}")
print(f"ö: {ö_arv}")
print(f"ü: {ü_arv}")
