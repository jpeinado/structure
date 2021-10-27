'''
Title: Manejo de interfaz grafica en python
Autor: Juan Carlos Peinado Pereira
Date : 05/09/19
'''
#import tk 
#from tk import *
import tkinter  # Libreria que maneja el entorno grafico en python
from tkinter import *

class main(Frame):# Definicion de la clase frame para la creacion del entorno visual
	def __init__(self,master):
		Frame.__init__(self,master=None)
		self.master.title("windows of test")
		self.valor = StringVar()
		self.valor.set("hello world")
		self.x = 100 #self.winfo_screenwidth
		self.y = 100 #self.winfo_screenheight
		#self.tamano = "%dX%d" % (self.x,self.y)
		#self.master.geometry("%dX%d" % (self.x,self.y))
		Label(self.master,textvariable=self.valor).pack()
		Entry(self.master).pack()
		Button(self.master,text="Dibujar",COMMAND=self.rectangulo()).pack()
	
	def rectangulo(self):
		canvas1=Canvas(self.master,width=300,height=210, bg='red')
		canvas1.pack(expand=YES,fill=BOTH)
		canvas1.create_rectangle(10,10,300,200)

Lienzo = Tk() # instancia del objeto frame para la visualizacion de la ventana en python
ventana = main(Lienzo) # Creacion de lla ventana segun parametizacion
Lienzo.mainloop()