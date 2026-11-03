vanus = int(input("Vanus: "))
opilane = input("Kas oled õpilane (jah/ei): ")

if vanus < 7:
    hind = 0
elif 7 <= vanus <= 17:
    hind = 5
elif vanus >= 18 and opilane == "jah" and vanus < 65:
    hind = 8
elif vanus >= 65:
    hind = 6
else:
    hind = 12

print(f"Pileti hind on: {hind} €")
