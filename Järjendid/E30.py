temperatuurid = []

with open("temperatuurid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        temperatuurid.append(int(rida.strip()))

mootmisi = len(temperatuurid)
keskmine = sum(temperatuurid) / mootmisi
korgeim = max(temperatuurid)
madalaim = min(temperatuurid)

miinuspaevad = 0
soojad_paevad = 0

for temp in temperatuurid:
    if temp < 0:
        miinuspaevad = miinuspaevad + 1
    if temp >= 5:
        soojad_paevad = soojad_paevad + 1

print(f"Mõõtmisi: {mootmisi}")
print(f"Keskmine temperatuur: {keskmine:.1f} °C")
print(f"Kõrgeim temperatuur: {korgeim} °C")
print(f"Madalaim temperatuur: {madalaim} °C")
print(f"Miinuskraadidega päevi: {miinuspaevad}")
print(f"Vähemalt 5-kraadiseid päevi: {soojad_paevad}")
