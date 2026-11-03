minutid_kokku = int(input("Sisesta minutid: "))

tunnid = minutid_kokku // 60
minutid = minutid_kokku % 60

print(f"{tunnid} tundi ja {minutid} minutit")
