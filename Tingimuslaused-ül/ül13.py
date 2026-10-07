küsimus = float(input("sisesta punktid:"))

if küsimus >= 90:
    print("hinnet on 5")
elif küsimus >= 75:
    print("hinnet on 4")
elif küsimus >= 50:
    print("hinnet on 3")
elif küsimus >= 49:
    print("hinnet on 2")
else:
    print("hinnet on 1")