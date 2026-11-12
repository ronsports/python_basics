f = open("algtekst.txt", "r", encoding="utf-8")
sisu = f.read()
f.close()

f2 = open("suured_tahed.txt", "w", encoding="utf-8")
f2.write(sisu.upper())
f2.close()
