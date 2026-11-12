def taishaalikuid(tekst):
    taishaalikud = "aeiouõäöüuAEIOUÕÄÖÜ"
    loendur = 0
    
    i = 0
    while i < len(tekst):
        if tekst[i] in taishaalikud:
            loendur = loendur + 1
        i = i + 1
        
    return loendur

print(taishaalikuid("Arvuti"))
print(taishaalikuid("JÄÄÄÄR"))
print(taishaalikuid(""))
