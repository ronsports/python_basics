try:
    with open("tekst.txt", encoding="UTF-8") as f:
        read = [rida.strip() for rida in f if rida.strip()]

        sõnadkokku = 0
        for text in read:
            sõnadeloend = len(text.split())
            sõnadkokku += sõnadeloend

except FileNotFoundError:
    print("pole")

print(f"Kokku sõnu: {sõnadkokku}")

