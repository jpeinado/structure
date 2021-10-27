from matplotlib import pyplot

class Graficar:
    def __init__(self):
        self.inicializar_gui()
    # Función cuadrática.
    def f1(self,x):
        return 2*(x**2) + 5*x - 2
    # Función lineal.
    def f2(self,x):
        return 4*x + 1    
    def inicializar_gui(self):
        # Valores del eje X que toma el gráfico.
        x = range(-10, 15)
        # Graficar ambas funciones.
        pyplot.plot(x, [self.f1(i) for i in x])
        pyplot.plot(x, [self.f2(i) for i in x])
        # Establecer el color de los ejes.
        pyplot.axhline(0, color="red")
        pyplot.axvline(0, color="blue")
        # Limitar los valores de los ejes.
        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)
        # Guardar gráfico como imágen PNG.
        pyplot.savefig("output.png")
        # Mostrarlo.
        pyplot.show()
    def pintar(self):
        pass
def main():
    ventana = Graficar()
if __name__ == "__main__":
    main()