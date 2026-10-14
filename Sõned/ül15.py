küsimus = input("Sisesta parool: ")
pikkus = len(küsimus)

if pikkus < 8:
    print("Parool on liiga lühike.")
elif 8 <= pikkus <= 11:
    print("Parooli pikkus on sobiv.")
else:
    print("Parool on pikk parool.")
