import tkinter as tk

akna_laius = 600
akna_korgus = 400
taustavarv = "white"

aken = tk.Tk()
aken.title("Minu kujundid")

tahvel = tk.Canvas(
    aken,
    width=akna_laius,
    height=akna_korgus,
    bg=taustavarv
)
tahvel.pack()

# 1. Punane ristkülik (algus_x, algus_y, lõpp_x, lõpp_y)
tahvel.create_rectangle(50, 50, 200, 150, fill="red")

# 2. Sinine ring (ovaal, mille laius ja kõrgus on võrdsed)
tahvel.create_oval(250, 50, 350, 150, fill="blue")

# 3. Roheline joon (algus_x, algus_y, lõpp_x, lõpp_y)
tahvel.create_line(50, 250, 200, 350, fill="green", width=3)

# 4. Kollane ovaal
tahvel.create_oval(250, 250, 450, 350, fill="yellow")

# 5. Tekst „Minu kujundid“ (keskkoha_x, keskkoha_y)
tahvel.create_text(450, 100, text="Minu kujundid", font=("Arial", 16, "bold"), fill="black")

aken.mainloop()
