import sys 
import Queue as queue
class NodoMVias:

    def __init__(self, orden, dato):

        self.maxValue = sys.maxsize
        self.orden = orden
        self.ListaDeDatos = []
        self.ListaDeHijos = []

        for i in range(0, self.orden):

            self.ListaDeHijos.append(None)

            if (i < (self.orden - 1)):

                self.ListaDeDatos.append(None)

        self.ListaDeDatos[0] = dato

    def setDato(self, posicion, dato):

        self.ListaDeDatos[posicion] = dato

    def getDato(self, posicion):

        return self.ListaDeDatos[posicion]

    def setHijo(self, posicion, hijo):

        self.ListaDeHijos[posicion] = hijo

    def getHijo(self, posicion):

        return self.ListaDeHijos[posicion]

    def esHijoVacio(self, posicion):

        return self.ListaDeHijos[posicion] == None

    def esDatoVacio(self, posicion):

        return self.ListaDeDatos[posicion] == None

    def setHijoVacio(self, posicion):

        self.ListaDeHijos[posicion] = None

    def setDatoVacio(self, posicion):

        self.ListaDeDatos[posicion] = None

    def getNroDeHijosNoVacio(self):

        cantidadHijosNoVacio = 0

        for i in range(0, len(self.ListaDeHijos)):

            hijo = self.ListaDeHijos[i]

            if (hijo != None):

                cantidadHijosNoVacio = cantidadHijosNoVacio + 1

        return cantidadHijosNoVacio

    def getNroDeDatosNoVacio(self):

        cantidadDeDatosNoVacio = 0

        for i in range(0, len(self.ListaDeDatos)):

            dato = self.ListaDeDatos[i]

            if (dato != None):

                cantidadDeDatosNoVacio = cantidadDeDatosNoVacio + 1

        return cantidadDeDatosNoVacio

    def estaDatoLleno(self):

        return (self.getNroDeDatosNoVacio() == len(self.ListaDeDatos))

class ArbolMViasDeBusqueda:

    def __init__(self, orden):

        self.raiz = None
        self.orden = 3

        if (orden < 3):

            print("Orden debe ser Mayor o igual a 3")

        else:

            self.orden = orden

    def esHoja(self, nodo):

        for i in range(0, self.orden):

            if (not nodo.esHijoVacio(i)):

                return False

        return True

    def estaDatoEnNodo(self, nodo, dato):

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                datoActual = nodo.getDato(i)

                if (datoActual == dato):

                    return True

        return False

    def posicionDelHijoPorDondeBajar(self, nodo, dato):

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                datoActual = nodo.getDato(i)

                if (dato < datoActual):

                    return i

        return self.orden - 1

    def insertarDatoEnNodo(self, nodo, dato):

        posicion = -1
        ultimaPosicion = -1

        for i in range(0,self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                datoActual = nodo.getDato(i)

                if ((dato < datoActual) and (posicion == -1)):

                    posicion = i

                ultimaPosicion = i

        if (posicion == -1):

            posicion = ultimaPosicion + 1

        i = ultimaPosicion

        while (i >= posicion):

            datoADesplazar = nodo.getDato(i)
            nodo.setDato(i + 1, datoADesplazar)
            i = i - 1

        nodo.setDato(posicion, dato)


    def insertar(self, dato):

        if (self.raiz == None):

            self.raiz = NodoMVias(self.orden, dato)

            return True

        nodoActual = self.raiz

        while (nodoActual != None):

            if (self.esHoja(nodoActual)):

                if (self.estaDatoEnNodo(nodoActual, dato)):

                    return False

                if (nodoActual.estaDatoLleno()):

                    nuevoHijo = NodoMVias(self.orden, dato)
                    posicionDelHijo = self.posicionDelHijoPorDondeBajar(nodoActual, dato)
                    nodoActual.setHijo(posicionDelHijo, nuevoHijo)

                else:

                    self.insertarDatoEnNodo(nodoActual, dato)

                return True

            else:

                if (self.estaDatoEnNodo(nodoActual, dato)):

                    return False

                posicionDelHijo = self.posicionDelHijoPorDondeBajar(nodoActual, dato)
                hijoPorDondeBajar = nodoActual.getHijo(posicionDelHijo)

                if (hijoPorDondeBajar == None):

                    nuevoHijo = NodoMVias(self.orden, dato)
                    nodoActual.setHijo(posicionDelHijo,nuevoHijo)

                    return True

                else:

                    nodoActual = hijoPorDondeBajar

        return False

    def recorridoPorNivel(self):

        recorrido = []

        if (self.raiz == None):

            return recorrido

        cola = queue.Queue()
        cola.put(self.raiz)

        while (not cola.empty()):

            nodo = cola.get()

            for i in range(0, self.orden - 1):

                if (not nodo.esDatoVacio(i)):

                    recorrido.append(nodo.getDato(i))

                if (nodo.getHijo(i) != None):

                    cola.put(nodo.getHijo(i))

            if (nodo.getHijo(self.orden - 1) != None):

                cola.put(nodo.getHijo(self.orden - 1))

        return recorrido

    def recorridoEnInOrden(self):

        recorrido = []
        self.recorridoEnInOrdenRecursivo(self.raiz, recorrido)
        return recorrido

    def recorridoEnInOrdenRecursivo(self, nodo, recorrido):

        if (nodo == None):

            return

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                self.recorridoEnInOrdenRecursivo(nodo.getHijo(i), recorrido)
                recorrido.append(nodo.getDato(i))

        self.recorridoEnInOrdenRecursivo(nodo.getHijo(self.orden - 1), recorrido)

    def recorridoEnPreOrden(self):

        recorrido = []
        self.recorridoEnPreOrdenRecursivo(self.raiz, recorrido)
        return recorrido

    def recorridoEnPreOrdenRecursivo(self, nodo, recorrido):

        if (nodo == None):

            return

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                recorrido.append(nodo.getDato(i))
                self.recorridoEnPreOrdenRecursivo(nodo.getHijo(i), recorrido)

        self.recorridoEnPreOrdenRecursivo(nodo.getHijo(self.orden - 1), recorrido)

    def recorridoEnPostOrden(self):

        recorrido = []
        self.recorridoEnPostOrdenRecursivo(self.raiz, recorrido)
        return recorrido

    def recorridoEnPostOrdenRecursivo(self, nodo, recorrido):

        if (nodo == None):

            return

        self.recorridoEnPostOrdenRecursivo(nodo.getHijo(0), recorrido)

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                self.recorridoEnPostOrdenRecursivo(nodo.getHijo(i + 1), recorrido)
                recorrido.append(nodo.getDato(i))

    def size(self):

        return self.sizeRecursivo(self.raiz)

    def sizeRecursivo(self, nodo):

        if (nodo == None):

            return 0

        cantidadDeNodo = 0

        for i in range(0, self.orden):

            cantidadDeNodo = cantidadDeNodo + self.sizeRecursivo(nodo.getHijo(i))

        return cantidadDeNodo + 1

    def altura(self):

        return self.alturaRecursivo(self.raiz)

    def alturaRecursivo(self, nodo):

        if (nodo == None):

            return 0

        alturaMayor = 0

        for i in range(0, self.orden):

            alturaDelhijo = self.alturaRecursivo(nodo.getHijo(i))

            if (alturaDelhijo > alturaMayor):

                alturaMayor = alturaDelhijo

        return alturaMayor + 1

    def nivel(self):

        return self.nivelRecursivo(self.raiz)

    def nivelRecursivo(self, nodo):

        if (nodo == None):

            return -1

        nivelMayor = -1

        for i in range(0, self.orden):

            nivelDelhijo = self.nivelRecursivo(nodo.getHijo(i))

            if (nivelDelhijo > nivelMayor):

                nivelMayor = nivelDelhijo

        return nivelMayor + 1

    def buscar(self, dato):

        if (self.raiz == None):

            return False

        cola = queue.Queue()
        cola.put(self.raiz)

        while ( not cola.empty()):

            nodo = cola.get()

            for i in range(0, self.orden - 1):

                if (not nodo.esDatoVacio(i)):

                    if (nodo.getDato(i) == dato):

                        return True

                if (nodo.getHijo(i) != None):

                    cola.put(nodo.getHijo(i))

            if (nodo.getHijo(self.orden - 1) != None):

                cola.put(nodo.getHijo(self.orden - 1))

        return False

    def eliminarDatoDeHoja(self, nodo, dato):

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                datoActual = nodo.getDato(i)

                if (dato == datoActual):

                    if (i < self.orden - 2):

                        for j in range(i, self.orden - 2):

                            if (not nodo.esDatoVacio(j)):

                                nodo.setDato(j, nodo.getDato(j + 1))

                        nodo.setDato(self.orden - 2, None)

                    else:

                        nodo.setDato(i, None)

    def tieneHijoAdelante(self, nodo, posicion):

        for i in range(posicion, self.orden):

            if (nodo.getHijo(i) != None):

                return True

        return False

    def obtenerSucesorDelDato(self, nodo, dato):

        posicion = 0

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                datoActual = nodo.getDato(i)

                if(datoActual == dato):

                    posicion = i

        i = posicion + 1

        if (nodo.getHijo(i) == None):

            return nodo.getDato(i)

        while ((i < self.orden) and (nodo.getHijo(i) == None)):

            i = i + 1

        return nodo.getHijo(i).getDato(0)

    def obtenerPredecesorDelDato(self, nodo, dato):

        posicion = 0

        for i in range(0, self.orden - 1):

            if (not nodo.esDatoVacio(i)):

                datoActual = nodo.getDato(i)

                if (dato == datoActual):

                    posicion = i

        i = posicion

        if (nodo.getHijo(i) == None):

            return nodo.getDato(i - 1)

        while ((i >= 0) and (nodo.getHijo(i) == None)):

            i = i - 1

        posicion = 0

        for j in range(0, self.orden - 1):

            if (not nodo.getHijo(i).esDatoVacio(j)):

                posicion = j

        return nodo.getHijo(i).getDato(posicion)

    def eliminar(self, dato):

        if (self.buscar(dato)):

            self.raiz = self.eliminarRecursivo(self.raiz, dato)

    def eliminarRecursivo(self, nodo, dato):

        if (nodo == None):

            return

        if (self.esHoja(nodo)):

            if (self.estaDatoEnNodo(nodo, dato)):

                self.eliminarDatoDeHoja(nodo, dato)

                if (nodo.getNroDeDatosNoVacio() == 0):

                    return None

                else:

                    return nodo

        for i in range(0, self.orden - 1):

            datoActual = nodo.getDato(i)

            if (dato < datoActual):

                hijoDePosicion = self.eliminarRecursivo(nodo.getHijo(i), dato)
                nodo.setHijo(i, hijoDePosicion)
                return nodo

            if (dato == datoActual):

                if (self.tieneHijoAdelante(nodo, i + 1)):

                    datoSucesor = self.obtenerSucesorDelDato(nodo, dato)
                    nodo = self.eliminarRecursivo(nodo, datoSucesor)
                    nodo.setDato(i, datoSucesor)
                    return nodo

                else:

                    datoPredecesor = self.obtenerPredecesorDelDato(nodo, dato)
                    nodo = self.eliminarRecursivo(nodo, datoPredecesor)
                    nodo.setDato(i, datoPredecesor)
                    return nodo

        ultimoHijo = self.eliminarRecursivo(nodo.getHijo(self.orden - 1), dato)
        nodo.setHijo(self.orden - 1, ultimoHijo)
        return nodo


def main():

    print("   ArbolMviasDeBusqueda   ")

    a = ArbolMViasDeBusqueda(4)

    a.insertar(40)
    a.insertar(20)
    a.insertar(30)
    a.insertar(10)
    a.insertar(5)
    a.insertar(25)
    a.insertar(28)
    a.insertar(22)
    a.insertar(21)
    a.insertar(27)
    a.insertar(26)
    a.insertar(70)
    a.insertar(60)
    a.insertar(90)
    a.insertar(72)
    a.insertar(75)
    a.insertar(78)
    a.insertar(140)
    a.insertar(120)
    a.insertar(100)
    a.insertar(110)
    a.insertar(105)
    a.insertar(71)
    a.insertar(15)
    a.insertar(12)
    a.insertar(14)

    print(a.recorridoPorNivel())
    print(a.recorridoEnInOrden())
    print(a.recorridoEnPreOrden())
    print(a.recorridoEnPostOrden())
    print(a.size())
    print(a.nivel())
    a.eliminar(1)
    print(a.recorridoPorNivel())
    print(a.size())

if __name__ == '__main__':
    main()
