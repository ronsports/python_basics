with open ("/home/ron/repositories/python_work/Andmevahetus/arvud.txt") as f:
 read = [int(line) for line in f.readlines()]

for num in read:
  print(num)

print(f"Teisentatud arvud: {read} ")
print(f"arvud {sum(read)}")