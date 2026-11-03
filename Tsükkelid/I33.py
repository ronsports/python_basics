from random import randint

salajane = randint(1, 100)
pakkumine = 0

while pakkumine != salajane:
    pakkumine = int(input("Arva arv 1–100: "))
    
    if pakkumine < salajane:
        print("Salajane arv on suurem.")
    elif pakkumine > salajane:
        print("Salajane arv on väiksem.")

print("Õige!")
