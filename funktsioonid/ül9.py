def ristkulik(laius, korgus):
    ins1 = int(input("Sisesta laius"))
    ins2 = int(input("Sisesta korgus"))
    print(2 * (ins1 + ins2))
    print(ins1 * ins2)
    print("ümbermõõt:", 2* (laius + korgus))
    print("Pindala:", laius * korgus)

ristkulik(7,4)
ristkulik(9, 8)
ristkulik(5, 5)