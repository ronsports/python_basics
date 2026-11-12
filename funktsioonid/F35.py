arv = 100

def muuda():
    arv = 20
    print("Funktsioonis:", arv)

muuda()
print("Põhiprogrammis:", arv)

## Eraldi mäluruumid selleparast lokaalne ei muuda globaalset muutujat.
## Funktsioonis: 20
## Põhiprogrammis: 100