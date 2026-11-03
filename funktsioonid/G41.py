import tkinter as tk

def joonista_ring(canvas, x, y, raadius, varv):
    x1 = x - raadius
    y1 = y - raadius
    x2 = x + raadius
    y2 = y + raadius
    canvas.create_oval(x1, y1, x2, y2, fill=varv, outline="")

akna_laius = 600
akna_korgus = 400

aken = tk.Tk()
aken.title("Värvilised ringid")

tahvel = tk.Canvas(aken, width=akna_laius, height=akna_korgus, bg="white")
tahvel.pack()

# Joonistame tsükli abil 10 ringi, mille asukoht, suurus ja värv muutuvad
for i in range(10):
    kesk_x = 50 + i * 50
    kesk_y = 50 + i * 30
    raadius = 10 + i * 3
    
    if i % 2 == 0:
        varv = "cyan"
    else:
        varv = "magenta"
        
    joonista_ring(tahvel, kesk_x, kesk_y, raadius, varv)

aken.mainloop()
