#Implementacion de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.HijoIzquierdo = None
        self.data = dato
        self.HijoDerecho = None

    #Setters
    def setData(self, dato):
        self.data = dato

    def setHijoDerecho(self, HD):
        self.HijoDerecho = HD

    def setHijoIzquierdo(self, HI):
        self.HijoIzquierdo = HI

    #Getters
    def getData(self):
        return self.data

    def getHijoIzquierdo(self):
        return self.HijoIzquierdo

    def getHijoDerecho(self):
        return self.HijoDerecho


#Implementacion del arbol balanceado
class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.Rango = 1

    def setRoot(self, link):
        self.raiz = link

    def getRoot(self):
        return self.raiz

    def alturaRecursivo(self, nodo):
        """Devuelve la altura del arbol"""
        if (nodo == None):
            return 0
        else:
            alturaIzquierdo = self.alturaRecursivo(nodo.getHijoIzquierdo())
            alturaDerecho = self.alturaRecursivo(nodo.getHijoDerecho())

            if (alturaIzquierdo > alturaDerecho):
                return alturaIzquierdo + 1
            else:
                return alturaDerecho + 1

    def existeDato(self, dato):
        """Busca si existe el dato en el árbol"""
        if (self.raiz == None):
            return False
        nodo = self.raiz
        while (nodo != None):
            if (dato == nodo.getData()):
                return True
            else:
                if (dato < nodo.getData()):
                    nodo = nodo.getHijoIzquierdo()
                else:
                    nodo = nodo.getHijoDerecho()
        return False

    def insertar(self, dato):
        """Inserta un nodo si no existe en el arbol"""
        if (self.existeDato(dato)):
            return None
        else:
            self.raiz = self.insertarRecursivo(self.raiz, dato)

    def insertarRecursivo(self, nodo, dato):
        if (nodo == None):
            return Nodo(dato)
        else:
            if (dato < nodo.getData()):
                nodo.setHijoIzquierdo(
                    self.insertarRecursivo(nodo.getHijoIzquierdo(), dato))
            else:
                if (dato > nodo.getData()):
                    nodo.setHijoDerecho(
                        self.insertarRecursivo(nodo.getHijoDerecho(), dato))
        return self.balancear(nodo)

    def balancear(self, nodo):
        alturaIzquierdo = self.alturaRecursivo(nodo.getHijoIzquierdo())
        alturaDerecho = self.alturaRecursivo(nodo.getHijoDerecho())

        if ((alturaIzquierdo - alturaDerecho) > self.Rango):
            nodoIzquierdo = nodo.getHijoIzquierdo()
            if (self.alturaRecursivo(nodoIzquierdo.getHijoDerecho()) >
                    self.alturaRecursivo(nodoIzquierdo.getHijoDerecho())):
                return self.rotacionDobleDerecho(nodo)
            else:
                return self.rotacionSimpleDerecho(nodo)
        else:
            if ((alturaDerecho - alturaIzquierdo) > self.Rango):
                nodoDerecho = nodo.getHijoDerecho()

                if (self.alturaRecursivo(nodoDerecho.getHijoIzquierdo()) >
                        self.alturaRecursivo(nodoDerecho.getHijoDerecho())):

                    return self.rotacionDobleIzquierdo(nodo)
                else:
                    return self.rotacionSimpleIzquierdo(nodo)
        return nodo

    def rotacionSimpleIzquierdo(self, nodo):
        nuevoNodo = nodo.getHijoDerecho()
        nodo.setHijoDerecho(nuevoNodo.getHijoIzquierdo())
        nuevoNodo.setHijoIzquierdo(nodo)
        return nuevoNodo

    def rotacionSimpleDerecho(self, nodo):
        nuevoNodo = nodo.getHijoIzquierdo()
        nodo.setHijoIzquierdo(nuevoNodo.getHijoDerecho())
        nuevoNodo.setHijoDerecho(nodo)
        return nuevoNodo

    def rotacionDobleIzquierdo(self, nodo):
        nodo.setHijoDerecho(self.rotacionSimpleDerecho(nodo.getHijoDerecho()))
        return self.rotacionSimpleIzquierdo(nodo)

    def rotacionDobleDerecho(self, nodo):
        nodo.setHijoIzquierdo(
            self.rotacionSimpleIzquierdo(nodo.getHijoIzquierdo()))
        return self.rotacionSimpleDerecho(nodo)

    def printInorder(self, node):
        if (node != None):
            self.printInorder(node.getHijoIzquierdo())
            print(node.getData())
            self.printInorder(node.getHijoDerecho())

    def printPreorder(self, node):
        if (node != None):
            print(node.getData())
            self.printPreorder(node.getHijoIzquierdo())
            self.printPreorder(node.getHijoDerecho())
