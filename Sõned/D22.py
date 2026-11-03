email = input("Sisesta e-post: ")

if " " in email:
    print("Aadressi kuju ei sobi: sisaldab tühikuid.")
elif email.count("@") != 1:
    print("Aadressi kuju ei sobi: peab olema täpselt üks @ märk.")
else:
    kasutaja, domeen = email.split("@")
    
    if len(kasutaja) == 0:
        print("Aadressi kuju ei sobi: @ ees peab olema vähemalt üks tähemärk.")
    elif "." not in domeen:
        print("Aadressi kuju ei sobi: domeeniosas puudub punkt.")
    elif domeen.startswith(".") or domeen.endswith("."):
        print("Aadressi kuju ei sobi: domeeniosa ei tohi alata ega lõppeda punktiga.")
    else:
        print("Aadressi kuju on sobiv.")
