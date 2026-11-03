from random import randint

salajane = randint(1, 10)
pakkumine = 0

while pakkumine != salajane:
    pakkumine = int(input("Arva arv 1–10: "))
    
    if pakkumine != salajane:
        print("Vale!")

print("Õige!")
