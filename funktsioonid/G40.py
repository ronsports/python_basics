import tkinter as tk

def joonista_ruut(canvas, x, y, suurus, varv):
    x1 = x
    y1 = y
    x2 = x + suurus
    y2 = y + suurus
    canvas.create_rectangle(x1, y1, x2, y2, fill=varv, outline="")

akna_laius = 600
akna_korgus = 400

aken = tk.Tk()
aken.title("Erinevad ruudud")

tahvel = tk.Canvas(aken, width=akna_laius, height=akna_korgus, bg="white")
tahvel.pack()

# Joonistame viis erinevat ruutu, andes kaasa tahvli, asukoha (x, y), suuruse ja värvi
joonista_ruut(tahvel, 50, 50, 80, "red")
joonista_ruut(tahvel, 200, 30, 120, "blue")
joonista_ruut(tahvel, 400, 80, 60, "green")
joonista_ruut(tahvel, 100, 220, 150, "yellow")
joonista_ruut(tahvel, 350, 200, 100, "purple")

aken.mainloop()
