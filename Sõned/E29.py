import tkinter as tk

lipu_laius = 600
lipu_korgus = 300
triibu_korgus = lipu_korgus / 3

sinine = "#0072CE"
must = "#000000"
valge = "#FFFFFF"

aken = tk.Tk()
aken.title("Eesti lipp")

tahvel = tk.Canvas(
    aken,
    width=lipu_laius,
    height=lipu_korgus,
    bg="gray"
)
tahvel.pack()

tahvel.create_rectangle(0, 0, lipu_laius, triibu_korgus, fill=sinine, outline="")
tahvel.create_rectangle(0, triibu_korgus, lipu_laius, triibu_korgus * 2, fill=must, outline="")
tahvel.create_rectangle(0, triibu_korgus * 2, lipu_laius, lipu_korgus, fill=valge, outline="")

aken.mainloop()
