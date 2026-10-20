def ruut(arv):
    arvutamine = arv ** 2
    return arvutamine

def kuup(arv):
    arvutamine = arv ** 3
    return arvutamine

tulemus = ruut(3) + ruut(4)
print(tulemus)

lopptulemus = ruut(3) + ruut(4) + kuup(4)
print(lopptulemus)