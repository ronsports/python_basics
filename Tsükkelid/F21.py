raha = 1000.0
aastad = 0

while raha < 2000:
    raha = raha * 1.05
    aastad = aastad + 1

print(f"Kontol on vähemalt 2000 eurot {aastad} aasta pärast.")
print(f"Lõppsumma on {round(raha, 2)} eurot.")
