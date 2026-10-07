correct_username = "student"
correct_password = "python123"

küsimus = input("sisesta kasutajanimi: ")
küsimus2 = input("sisesta parool: ")

if küsimus == correct_username and küsimus2 == correct_password:
    print("Tere tulemast!")
else:
    print("Vale kasutajanimi või parool.")