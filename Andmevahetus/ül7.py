küsimus = input("Sisesta faili nimi")


try:
    with open(küsimus, encoding="UTF-8") as f:
        read = f.readlines()
        print(read)


except FileNotFoundError:
    print("Pole")