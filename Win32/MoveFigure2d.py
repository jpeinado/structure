# importacion de la libreria Tkinter
from tkinter import *
# Implementacion de la clase grafica dibujar
class Dibujar(object):

    def __init__(self,master):
        self.master = master
        self.inicializar_gui()
        
    def inicializar_gui(self):
        self.lienzo = Canvas(self.master,width=100,height=100)
        self.lienzo.pack(expand=YES,fill=BOTH)
        self.lienzo.bind('<ButtonPress-1>',self.iniciar_dibujo)
        self.lienzo.bind('<B1-Motion>',self.dibujar)
        self.lienzo.bind('<Double-1>',self.limpiar)
        self.lienzo.bind('<ButtonPress-3>',self.mover)

        Button(self.master,text='Dibujar',command=lambda: self.rectangulo()).pack()
        self.tipos_figuras = [self.lienzo.create_rectangle, self.lienzo.create_oval, self.lienzo.create_line]
        self.dibujo = None

    def iniciar_dibujo(self,evento):
        self.figura = self.tipos_figuras[0]
        self.tipos_figuras = self.tipos_figuras[1:] + self.tipos_figuras[:1]
        self.inicio = evento
        self.dibujo = None

    def dibujar(self,evento):
        self.lienzo = evento.widget 
        if self.dibujo:
            self.lienzo.delete(self.dibujo)
        id_figura = self.figura(self.inicio.x, self.inicio.y, evento.x, evento.y)
        self.dibujo = id_figura    
    def limpiar(self,evento):
        evento.widget.delete('all')
    def mover(self,evento):
        if self.dibujo:
            self.lienzo = evento.widget
            diferencia_x = evento.x - self.inicio.x
            diferencia_y = evento.y - self.inicio.y
            self.lienzo.move(self.dibujo, diferencia_x, diferencia_y)
            self.inicio = evento
    
    def rectangulo(self):
        self.lienzo.pack(expand=YES,fill=BOTH)
        self.lienzo.create_rectangle(10,10,100,100,width=10,fill='red')

    def linea(self):
        self.lienzo.pack(expand=YES,fill=BOTH)
        self.lienzo.create_line(0, 200, 200, 0, width=5, fill='green')

def main():
    master = Tk()
    master.title("Mis dibujos") 
    master.geometry('300x300') 
    
    ventana = Dibujar(master)
    
    master.mainloop()     

if __name__ == "__main__":
    main()     