import tkinter as tk

ruudu_suurus = 40
vahe = 10
algus_x = 20
algus_y = 50

aken = tk.Tk()
aken.title("Värvilised ruudud")

tahvel = tk.Canvas(aken, width=540, height=150, bg="white")
tahvel.pack()

for i in range(10):
    x1 = algus_x + i * (ruudu_suurus + vahe)
    y1 = algus_y
    x2 = x1 + ruudu_suurus
    y2 = y1 + ruudu_suurus
    
    if i % 2 == 0:
        varv = "red"
    else:
        varv = "blue"
        
    tahvel.create_rectangle(x1, y1, x2, y2, fill=varv, outline="")

aken.mainloop()
