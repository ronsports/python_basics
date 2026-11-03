a = float(input("Esimene arv: "))
tehe = input("Tehe (+, -, *, /): ")
b = float(input("Teine arv: "))

if tehe == "+":
    tulemus = a + b
    print(f"Tulemus: {tulemus}")
elif tehe == "-":
    tulemus = a - b
    print(f"Tulemus: {tulemus}")
elif tehe == "*":
    tulemus = a * b
    print(f"Tulemus: {tulemus}")
elif tehe == "/":
    if b == 0:
        print("Viga: Nulliga ei saa jagada!")
    else:
        tulemus = a / b
        print(f"Tulemus: {tulemus}")
else:
    print("Viga: Tundmatu tehe!")
