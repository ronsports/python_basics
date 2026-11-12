import urllib.request

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

with urllib.request.urlopen(url) as vastus:
    baidid = vastus.read()

tekst = baidid.decode("utf-8")
read = tekst.splitlines()

tahemarke = len(tekst)
ridu = len(read)
sonu = 0
tuhje_ridu = 0

i = 0
while i < ridu:
    rida = read[i]
    
    if len(rida.strip()) == 0:
        tuhje_ridu = tuhje_ridu + 1
        
    sonu = sonu + len(rida.split())
    i = i + 1

print("Veebiteksti statistika")
print("----------------------")
print(f"Ridu: {ridu}")
print(f"Sõnu: {sonu}")
print(f"Tähemärke: {tahemarke}")
print(f"Tühje ridu: {tuhje_ridu}")
