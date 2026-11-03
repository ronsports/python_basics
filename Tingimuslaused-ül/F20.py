a = float(input("Sisesta esimene külg: "))
b = float(input("Sisesta teine külg: "))
c = float(input("Sisesta kolmas külg: "))

if a + b > c and a + c > b and b + c > a:
    print("Kolmnurk on võimalik.")
else:
    print("Kolmnurk ei ole võimalik.")
