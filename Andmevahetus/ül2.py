fail = open("tervitus.txt", "r", encoding="utf-8")
number = 1

for rida in fail:
    print(str(number) + ": " + rida.strip())
    number += 1

fail.close()
