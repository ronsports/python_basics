esimene = [12, 15, 18]
teine = [21, 24, 27]
res = 0
järjend1 = (esimene + teine)
järjend1.append(30)

print(järjend1)
print(järjend1[0])
print(järjend1[6])

for i in järjend1:
    res += i

print(res)