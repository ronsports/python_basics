parool = input("Sisesta parool: ")

punktid = 0
puudused = []

# 1. Pikkuse kontroll
if len(parool) >= 8:
    punktid += 1
else:
    puudused.append("Parool on liiga lühike (vähemalt 8 tähemärki).")

# 2. Suurtähe kontroll
on_suurtaht = False
for s in parool:
    if s.isupper():
        on_suurtaht = True

if on_suurtaht:
    punktid += 1
else:
    puudused.append("Puudub suurtäht.")

# 3. Väiketähe kontroll
on_vaiketaht = False
for s in parool:
    if s.islower():
        on_vaiketaht = True

if on_vaiketaht:
    punktid += 1
else:
    puudused.append("Puudub väiketäht.")

# 4. Numbri kontroll
on_number = False
for s in parool:
    if s.isdigit():
        on_number = True

if on_number:
    punktid += 1
else:
    puudused.append("Puudub number.")

# 5. Erimärgi kontroll (kõik, mis pole täht ega number)
on_erimark = False
for s in parool:
    if not s.isalnum():
        on_erimark = True

if on_erimark:
    punktid += 1
else:
    puudused.append("Puudub erimärk.")

# Hinnangu määramine punktide põhjal
if punktid <= 2:
    hinnang = "Nõrk parool"
elif punktid <= 4:
    hinnang = "Keskmine parool"
else:
    hinnang = "Kõik nõuded täidetud"

# Tulemuste väljastamine
print(f"\nTulemus: {punktid}/5")
print(f"Hinnang: {hinnang}")

if puudused:
    print()
    for puudus in puudused:
        print(puudus)
