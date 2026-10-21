try:
    with open("arvud.txt", encoding="UTF-8") as f:
        read = [int(rida.strip()) for rida in f if rida.strip()]

    suurim = max(read)
    vaikseim = min(read)
    vahe = suurim - vaikseim

    print(f"Suurim arv: {suurim}")
    print(f"Väikseim arv: {vaikseim}")
    print(f"Vahe: {vahe}")

except FileNotFoundError:
    print("arvud.txt ei leitud.")
