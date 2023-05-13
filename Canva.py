from tkinter import *

#variables
BASE = 460
ALTURA = 220

#-----------------------------
# ventana principal de la app
#-----------------------------
ventana_principal = Tk()
ventana_principal.title("Canva")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

#------------------------------------
frame1 = Frame(ventana_principal)
frame1.config(width=480, height=240, bg="bisque")
frame1.place(x=10, y=10)

c = Canvas(frame1, width=BASE, height=ALTURA)
c.place(x=10,y=10)
c.config(bg="yellow")

#lineas
"""linea1= c.create_line(10,10, BASE-10,10, fill="red")
linea2= c.create_line(BASE-10, 10, BASE-10, ALTURA-10, fill="red")
linea3= c.create_line(BASE-10 , ALTURA-10, 10, ALTURA-10, fill="red")
linea4= c.create_line(10, ALTURA-10, 10, 10, fill="red")
linea5= c.create_line(10,10, BASE-10, ALTURA-10, fill="red")
linea5= c.create_line(BASE-10,10, 10, ALTURA-10, fill="red")"""


#cruz
linea1= c.create_line(190,40, 270,40, fill="red")
linea2= c.create_line(270,40, 270,80, fill="red")
linea3= c.create_line(270,80, 320,80, fill="red")
linea4= c.create_line(320,80, 320,140, fill="red")
linea5= c.create_line(320,140, 270,140, fill="red")
linea5= c.create_line(270,140, 270,180, fill="red")
linea6= c.create_line(270,180, 190,180, fill="red")
linea7= c.create_line(190,180, 190,180, fill="red")
linea8= c.create_line(190,180, 190,140, fill="red")
linea9= c.create_line(190,140, 140,140, fill="red")
linea10= c.create_line(140,140, 140,80, fill="red")
linea11= c.create_line(140,80, 190,80, fill="red")
linea12= c.create_line(190,80, 190,40, fill="red")

#----------------------------------------------------------------------------

ventana_principal.mainloop()


