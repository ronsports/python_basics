fail_sisse = open("arvud.txt", "r")
fail_valja = open("paarisarvud.txt", "w")
mitu = 0

for rida in fail_sisse:
    arv = int(rida)
    if arv % 2 == 0:
        fail_valja.write(str(arv) + "\n")
        mitu = mitu + 1

fail_sisse.close()
fail_valja.close()

print(f"paaris arve:", mitu)
