tekst = input("Sisesta tekst: ")

tahemarke_kokku = len(tekst)
ilma_tuhikuteta = len(tekst.replace(" ", ""))
sonu = len(tekst.split())

taishaalikud = "aeiouõäöüuAEIOUÕÄÖÜ"
taishaalikute_arv = 0
numbrite_arv = 0

for sumbol in tekst:
    if sumbol in taishaalikud:
        taishaalikute_arv = taishaalikute_arv + 1
    elif sumbol.isdigit():
        numbrite_arv = numbrite_arv + 1

print(f"\nTähemärke kokku: {tahemarke_kokku}")
print(f"Tähemärke ilma tühikuteta: {ilma_tuhikuteta}")
print(f"Sõnu: {sonu}")
print(f"Täishäälikuid: {taishaalikute_arv}")
print(f"Numbreid: {numbrite_arv}")
