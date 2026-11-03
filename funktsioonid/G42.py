import tkinter as tk

def joonista_sein(canvas, x, y, laius, korgus, varv):
    canvas.create_rectangle(x, y, x + laius, y + korgus, fill=varv, outline="black")

def joonista_katus(canvas, x, y, laius, katuse_korgus, varv):
    x1 = x
    y1 = y
    x2 = x + laius / 2
    y2 = y - katuse_korgus
    x3 = x + laius
    y3 = y
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=varv, outline="black")

def joonista_aken(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv, outline="black")
    canvas.create_line(x + suurus / 2, y, x + suurus / 2, y + suurus)
    canvas.create_line(x, y + suurus / 2, x + suurus, y + suurus / 2)

def joonista_maja(canvas, x, y, laius, seina_korgus, seina_varv, katuse_varv):
    joonista_sein(canvas, x, y, laius, seina_korgus, seina_varv)
    
    katuse_korgus = laius * 0.5
    joonista_katus(canvas, x, y, laius, katuse_korgus, katuse_varv)
    
    akna_suurus = laius * 0.3
    akna_x = x + (laius - akna_suurus) / 2
    akna_y = y + (seina_korgus - akna_suurus) / 2
    joonista_aken(canvas, akna_x, akna_y, akna_suurus, "lightcyan")

akna_laius = 800
akna_korgus = 500

aken = tk.Tk()
aken.title("Maja joonistamine")

tahvel = tk.Canvas(aken, width=akna_laius, height=akna_korgus, bg="skyblue")
tahvel.pack()

joonista_maja(tahvel, x=50, y=250, laius=150, seina_korgus=150, seina_varv="khaki", katuse_varv="firebrick")
joonista_maja(tahvel, x=280, y=200, laius=220, seina_korgus=200, seina_varv="lightgray", katuse_varv="darkslategrey")
joonista_maja(tahvel, x=570, y=280, laius=120, seina_korgus=120, seina_varv="burlywood", katuse_varv="indianred")

aken.mainloop()
