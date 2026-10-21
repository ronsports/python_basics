with open("arvud.txt", encoding="UTF-8") as f:
    read = [int(rida.strip()) for rida in f if rida.strip()]

paaris = 0
paaritu = 0

for arv in read:
    if arv % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

print(f"paaris arve on {paaris}")
print(f"paaritu arve on {paaritu}")