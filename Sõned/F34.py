import tkinter as tk

ruudu_suurus = 50
ridu = 8
veergusid = 8

aken = tk.Tk()
aken.title("Malelaud")

tahvel = tk.Canvas(
    aken, 
    width=veergusid * ruudu_suurus, 
    height=ridu * ruudu_suurus, 
    bg="white"
)
tahvel.pack()

for rida in range(ridu):
    for veerg in range(veergusid):
        x1 = veerg * ruudu_suurus
        y1 = rida * ruudu_suurus
        x2 = x1 + ruudu_suurus
        y2 = y1 + ruudu_suurus
        
        if (rida + veerg) % 2 == 0:
            varv = "#F0D9B5"
        else:
            varv = "#B58863"
            
        tahvel.create_rectangle(x1, y1, x2, y2, fill=varv, outline="")

aken.mainloop()
