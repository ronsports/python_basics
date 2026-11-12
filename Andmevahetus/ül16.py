f = open("ostunimekiri.txt", "w", encoding="utf-8")

while True:
    küsimus = input("Sisesta toode: ")
    
    if küsimus == "stop" or küsimus == "STOP":
        break
        
    f.write(küsimus + "\n")

f.close()
