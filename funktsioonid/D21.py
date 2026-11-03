def on_paaris(arv):
    if arv % 2 == 0:
        return True
    else:
        return False

# Testimine ülesande näidetega
print(on_paaris(8))
print(on_paaris(13))

# Testimine nulli ja negatiivsete arvudega
print(on_paaris(0))
print(on_paaris(-4))
print(on_paaris(-7))
