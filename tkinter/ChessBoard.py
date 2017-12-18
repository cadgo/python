from Tkinter import *
from time import sleep
from PIL import ImageTk, Image
import copy

C_height = 500
C_widht = 500
C_Rows = 8
C_Lines = 8
Grab=0
master = Tk()
master.title("Chess Board")
master.resizable(False, False)
w = Canvas(master, width= C_widht, height= C_height )

w.pack(expand=YES, fill=BOTH )
padding = C_widht / C_Rows

def motion(event):
    w.coords(item, (event.x, event.y))

def nomotion(event):
    return
    
    
def callback(event):
    itemX, itemY = w.coords(item)
    if event.x <= itemX + 50 and event.y <= itemY + 50:
        print("click en X dentro de la imagen")
        w.bind("<B1-Motion>", motion)
    else:
        w.bind("<B1-Motion>", nomotion)
        
    
def DrawBoard(Lines, padding):
    a = y = 0
    Color = 1
    p = padding
    for z in range(Lines):
        for x in range(Lines):
            if Color == 0:
                w.create_rectangle(a, y, a + padding, p, fill='blue')
                Color = 1
            else:
                w.create_rectangle(a, y, a + padding, p, fill='white')
                Color = 0
            a += padding
        if Color == 0:
            Color = 1
        else:
            Color = 0
        a = 0
        y += padding
        p += p
 
#         
DrawBoard(C_Rows, padding)
img = ImageTk.PhotoImage(Image.open("horse.png").resize((50,50), Image.ANTIALIAS))
item = w.create_image(0,0, image= img, anchor='nw')
w.bind("<Button-1>", callback)
#w.bind("<B1-Motion>", callback)
#w.pack()
mainloop()
