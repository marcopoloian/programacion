import time
from tkinter import *
ventana = Tk()
lienzo = Canvas(ventana, width = 600,height = 500)
lienzo.pack()
lienzo.create_rectangle(250,250,280,280,fill="black")
Tk.update (ventana)
time.sleep(0.5)

w=input("presione una tecla")

if w=='w':
    lienzo.move(1,0,-30)
    time.sleep(0.1)

if w=='a':
    lienzo.move(1,-30,0)
    time.sleep(0.1)

if w=='d':
    lienzo.move(1,30,0)
    time.sleep(0.1)

if w=='s':
    lienzo.move(1,0,30)
    time.sleep(0.1)




Tk.update(ventana)
time.sleep(10)
