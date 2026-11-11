küsimus = input("Sisesta parool: ")

punktid = 0

if len(küsimus) >= 8:
    punktid = punktid + 1

on_suurtäht = False
for märk in küsimus:
    if märk.isupper():
        on_suurtäht = True

if on_suurtäht == True:
    punktid = punktid + 1

on_väiketäht = False
for märk in küsimus:
    if märk.islower():
        on_väiketäht = True

if on_väiketäht == True:
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
if on_suurtäht == False:
    print("Puudub suurtäht.")
if on_väiketäht == False:
    print("Puudub väiketäht.")
if on_number == False:
    print("Puudub number.")
if on_erimärk == False:
    print("Puudub erimärk.")
