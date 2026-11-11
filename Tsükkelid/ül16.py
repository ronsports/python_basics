õige_parool = "python123"
kasutaja_parool = ""

while kasutaja_parool != õige_parool:
    kasutaja_parool = input("Sisesta parool: ")
    if kasutaja_parool == õige_parool:
        print("õige parool")
        break
    else:
        print("vale")




