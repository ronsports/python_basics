küsimus = input("Sisesta sõna: ")
madal_sõna = küsimus.lower()

if madal_sõna == madal_sõna[::-1]:
    print("Tegemist on palindroomiga.")
else:
    print("Tegemist ei ole palindroomiga.")
