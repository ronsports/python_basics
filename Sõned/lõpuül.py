küsimus = input("Sisesta parool: ")

punktid = 0

if len(küsimus) >= 8:
    punktid = punktid + 1

if not küsimus.islower():
    punktid = punktid + 1

if not küsimus.isupper():
    punktid = punktid + 1

on_number = False
for märk in küsimus:
    if märk.isdigit():
        on_number = True

if on_number == True:
    punktid = punktid + 1

on_erimärk = False
for märk in küsimus:
    if not märk.isalnum():
        on_erimärk = True

if on_erimärk == True:
    punktid = punktid + 1

print(f"Tulemus: {punktid}/5")

if punktid <= 2:
    print("Hinnang: Nõrk parool")
elif punktid <= 4:
    print("Hinnang: Keskmine parool")
else:
    print("Hinnang: Kõik nõuded täidetud")

if len(küsimus) < 8:
    print("Vähem kui kaheksa tähemärki.")
if küsimus.islower():
    print("Puudub suurtäht.")
if küsimus.isupper():
    print("Puudub väiketäht.")
if on_number == False:
    print("Puudub number.")
if on_erimärk == False:
    print("Puudub erimärk.")
