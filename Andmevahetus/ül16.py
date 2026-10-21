f = open("Tooded.txt", "w", encoding="utf-8")

while True:
    küsimus = input("Sisesta toode: ")
    
    if küsimus == "stop":
        break
        
    f.write(küsimus + "\n")

f.close()
