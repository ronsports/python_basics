õige_parool = "python123"
kasutaja_parool = ""

while kasutaja_parool != õige_parool:
 küsimus = input("Sisesta parool")
 if küsimus != õige_parool:
  print("õige parool")
  break
 else:
  print("vale")




