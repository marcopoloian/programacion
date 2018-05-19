
import time
from tkinter import
import serial

puerto= serial.Serial("/dev/tty.usbmodem1411")

ventana=Tk()
lienzo=Canvas(ventana,width=500,height=500)

lienzo.pack()
lienzo.create_rectangle(200,350,300,450,fill="red")
Tk.update(ventana)
time.sleep(3)

mov="0"

while true:

    datos = str(serial.Serial.readline(puerto))
    if int(datos.find("arriba")) == 2:
        mov = (datos[2:len("arriba") + 2])
    if int(datos.find("abajo")) == 2:
        mov = (datos[2:len("abajo") + 2])
    if int(datos.find("derecha")) == 2:
        mov = (datos[2:len("derecha") + 2])
    if int(datos.find("izquierda")) == 2:
        mov = (datos[2:len("izquierda") + 2])

    if mov=="arriba":
        lienzo.move(1,0,-2)
        Tk.update(ventana)
        time.sleep(0.1)

    if mov=="abajo":
        lienzo.move(1,0,2)
        Tk.update(ventana)
        time.sleep(0.1)

    if mov=="izquierda":
        lienzo.move(1,-2,0)
        Tk.update(ventana)
        time.sleep(0.1)

    if mov=="derecha":
        lienzo.move(1,2,0)
        Tk.update(ventana)
        time.sleep(0.1)