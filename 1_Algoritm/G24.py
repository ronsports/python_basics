sekundid_kokku = int(input("Sisesta sekundid: "))

minutid = sekundid_kokku // 60
sekundid = sekundid_kokku % 60

print(f"{minutid} minutit ja {sekundid} sekundit")
