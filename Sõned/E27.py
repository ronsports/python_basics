import tkinter as tk

akna_laius = 600
akna_korgus = 400
taustavarv = "white"

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=akna_laius,
    height=akna_korgus,
    bg=taustavarv
)

tahvel.pack()

aken.mainloop()
