import urllib.request

url = "https://www.postimees.ee/8576230/raimond-kaljulaid-poliitikast-lahkumise-otsus-tuli-lihtsalt"

with urllib.request.urlopen(url) as vastus:
    baidid = vastus.read()

tekst = baidid.decode("utf-8")
read = tekst.splitlines()

loendur = 1
while loendur <= 10 and loendur <= len(read):
    print(f"{loendur}. {read[loendur - 1]}")
    loendur = loendur + 1
