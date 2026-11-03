import urllib.request

url = "https://docs.channel.io/allow-ads-help/en/articles/Ad-permission-message-appears-when-no-adblocker-is-installed-ba6d2a48?device=pc&domain=newsinlevels.com"

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
