
'''
Proyecto: Proyecto de Arbol Binario de busqueda
Autor: Juan Carlos Peinado Pereira
Version: 1.0
Fecha: 29/06/2021
'''
# Clase Nodo que representa una estructura base de un arbol binario
class Nodo:
    # Metodo constructor que permite crear una instancia de la clase nodo que lleva como parametro un valor
    '''
    Motodo constructor de la clase nodo : Paramero Value de tipo Object
    '''
    def __init__(self, value):
        ''' 
        Atributos del metodo constructor
        '''
        self.__left = None
        self.__right = None
        self.__data = value
    #Metodos getter y setter
    def d_Dato(self):
        '''
        Metodo que retorna un valor de tipo elemento de un nodo
        '''
        return self.__data
    def __i_Dato(self,value):
        self.__data = value
# Metodo que llama a las instancias de la clase Nodo
def main():
    myNodo = Nodo(10)
    x = myNodo.d_Dato()
    print(x)
if __name__ == '__main__':
    main()
