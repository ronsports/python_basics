küsimus = (int(input("mis on õhutemp? ")))

if küsimus < 0:
    print("külmub")
elif küsimus > 0 and küsimus < 15:
    print("jahe")
elif küsimus > 16 and küsimus < 25:
    print("soe")
else:
    print("kõrge")

