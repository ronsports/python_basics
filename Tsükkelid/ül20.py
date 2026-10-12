raha = 1000.0
aasta = 1

while aasta <= 10:
    raha = raha * 1.05
    print(f"{aasta}. aasta: {round(raha, 2)} €")
    aasta += 1
