ventana = Tk()
btn1=Button(ventana,text="Arriba" , command=arriba)
btn1=Button(ventana,text="Abajo" , command=abajo)
btn1=Button(ventana,text="Izquierda" , command=izq)
btn1=Button(ventana,text="Derecha" , command=der)
btn1=Button(ventana,text="Salir" , command=salir)

lienzo = Canvas(ventana,width=400, height=400)
lienzo.pack()
lienzo.create_rectangle(190,190,210,210,fill="black")

Tk.update(ventana)

btn1.pack(side="top")
btn2.pack(side="bottom")
btn3.pack(side="left")
btn4.pack(side="right")
btn5.pack()

while(flag):
    Tk.uptade(ventana)