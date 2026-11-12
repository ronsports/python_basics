import urllib.request

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

with urllib.request.urlopen(url) as vastus:
    baidid = vastus.read()

tekst = baidid.decode("utf-8")

print(tekst)
