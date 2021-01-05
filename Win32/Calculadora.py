'''
Autor: Juan Carlos Peinado Pereira
Date: 28/12/2020
Proyect: Implement of class graphics for win32
'''
import tkinter
from tkinter import *
#import tkMessageBox
	
def Suma():	
	n1=float(caja1.get())	
	n2=float(caja2.get())
	suma=n1+n2
	var3.set(suma)
	#tkMessageBox.showinfo("Mensaje","El resultado es: %.2f"%suma)
boot=Tk()
boot.title("Interfaz Grafica")
boot.geometry("400x200")
#CREACION DE UNA ETIQUETA
var1=StringVar()
var1.set("Escribe el primer numero: ")
label1=Label(boot,textvariable=var1,height=2)
label1.pack()

numero1=StringVar()
caja1=Entry(boot,bd=4,textvariable=numero1)
caja1.pack()

var2=StringVar()
var2.set("Escribe el segundo numero: ")
label2=Label(boot,textvariable=var2,height=2)
label2.pack()

numero2=StringVar()
caja2=Entry(boot,bd=4,textvariable=numero2)
caja2.pack()


boton1=Button(boot,text="calcular",command=Suma,width=15)
boton1.pack()

var3=StringVar()
label3=Label(boot,textvariable=var3,height=2)
label3.pack()

boot.mainloop()