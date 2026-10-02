n = input("sisesta oma nimi:")
v = int(input("sisesta oma vanus:"))

koolipikkus = float(input("sisesta koolipikkus kilomeetrites:"))
kooliteemin = int(input("sisesta koolitee minutites:"))

print(f"Tere {n}!")

vans_jarka = v + 1
print(f"järgmine aasta oled {vans_jarka} aastat vana")

koolitee_m = koolipikkus * 1000
print(f"koolitee pikkus on: {koolitee_m} meetrit")

t = kooliteemin // 60
min = kooliteemin % 60
print(f"koolitee kestab: {t} tundi ja {min} minutit")

kmh = koolipikkus / (kooliteemin / 60)
print(f"koolitee kiirus on: {kmh} km/h")