arv = 100

def muuda():
    global arv  
    arv = 20
    print("Funktsioonis:", arv)

muuda()
print("Põhiprogrammis:", arv)

## Funktsioonis: 20
## Põhiprogrammis: 100