import Queue as queue

class Nodo:
    
    def __init__(self, dato):
        self.HijoIzquierdo = None
        self.data = dato
        self.HijoDerecho = None
        
        
    def getHijoIzquierdo(self):
        return self.HijoIzquierdo
    
    
    def setHijoIzquierdo(self, HI):
        self.HijoIzquierdo = HI
        
        
    def getData(self):
        return self.data
    
    
    def setData(self, dato):
        self.data = dato
        
        
    def getHijoDerecho(self):
        return self.HijoDerecho
    
    
    def setHijoDerecho(self, HD):
        self.HijoDerecho = HD


class ArbolAVL:
    
    def __init__(self):
        self.raiz = None
        self.Rango = 1
        
    
    def alturaRecursivo(self, nodo):
        
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
        
        if (self.existeDato(dato)):
            
            return
        
        else:
            
            self.raiz = self.insertarRecursivo(self.raiz, dato)


    def insertarRecursivo(self, nodo, dato):
        
        if (nodo == None):
            return Nodo(dato)
        
        else:
            
            if (dato < nodo.getData()):
                nodo.setHijoIzquierdo(self.insertarRecursivo(nodo.getHijoIzquierdo(), dato))
                
            else:
                
                if (dato > nodo.getData()):
                    nodo.setHijoDerecho(self.insertarRecursivo(nodo.getHijoDerecho(), dato))
                      
        return self.balancear(nodo)


    def balancear(self, nodo):
        
        alturaIzquierdo = self.alturaRecursivo(nodo.getHijoIzquierdo())
        alturaDerecho = self.alturaRecursivo(nodo.getHijoDerecho())
        
        if ((alturaIzquierdo - alturaDerecho) > self.Rango):
            nodoIzquierdo = nodo.getHijoIzquierdo()
            
            if (self.alturaRecursivo(nodoIzquierdo.getHijoDerecho()) > self.alturaRecursivo(nodoIzquierdo.getHijoDerecho())):
                
                return self.rotacionDobleDerecho(nodo) 
            
            else:
                
                return self.rotacionSimpleDerecho(nodo)
        
        else:
            
            if ((alturaDerecho - alturaIzquierdo) > self.Rango):
                nodoDerecho = nodo.getHijoDerecho()
                
                if (self.alturaRecursivo(nodoDerecho.getHijoIzquierdo()) > self.alturaRecursivo(nodoDerecho.getHijoDerecho())):
                    
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
        
        nodo.setHijoIzquierdo(self.rotacionSimpleIzquierdo(nodo.getHijoIzquierdo()))
        
        return self.rotacionSimpleDerecho(nodo)
     
        
    def recorridoPorNivelesIterativo(self):
        
        nodo = self.raiz
        
        if (nodo == None):
            return
        
        cola = queue.Queue()
        cola.put(self.raiz)
        
        while (not cola.empty()):
            nodoActual = cola.get()
            print(nodoActual.getData())
            
            if (nodoActual.getHijoIzquierdo() != None):
                cola.put(nodoActual.getHijoIzquierdo())
            
            if (nodoActual.getHijoDerecho() != None):
                cola.put(nodoActual.getHijoDerecho())
    
    
    def eliminar(self, dato):
        self.eliminarRecursivo(self.raiz, dato)
        
        
    def eliminarRecursivo(self, nodo, dato):
        
        if (nodo == None):
            return
        
        else:
            
            if (dato < nodo.getData()):
                nodo.setHijoIzquierdo(self.eliminarRecursivo(nodo.getHijoIzquierdo(), dato))
                
                return self.balancear(nodo)
            
            if (dato > nodo.getData()):
                nodo.setHijoDerecho(self.eliminarRecursivo(nodo.getHijoDerecho(), dato))
                
                return self.balancear(nodo)
            
            # caso 1 si es hoja el nodo
            
            if ((nodo.getHijoDerecho() == None) and (nodo.getHijoIzquierdo() == None)):
                
                return None
            
            # caso 2  si el nodo tiene solo izquierdo
            
            if ((nodo.getHijoIzquierdo() != None) and (nodo.getHijoDerecho() == None)):
                
                return nodo.getHijoIzquierdo()
            
            # caso  2  si el nodo tiene solo derecho
            
            if ((nodo.getHijoIzquierdo() == None) and (nodo.getHijoDerecho() != None)):
                
                return nodo.getHijoDerecho()
            
            # caso 3 si el nodo tienes ambos 
            
            datoSucesor = self.buscarDatoSucesor(nodo.getHijoDerecho())
            nodo.setHijoDerecho(self.eliminarRecursivo(nodo.getHijoDerecho(), datoSucesor))
            nodo.setData(datoSucesor)
            
            return nodo
            
                   
    def buscarDatoSucesor(self, nodo):
        nuevoNodo = None
        nuevoNodo = nodo
        while (nodo != None):
            nuevoNodo = nodo
            nodo = nodo.getHijoIzquierdo()
            
        return nuevoNodo.getData()
    
    def recorridoEnInorden(self, nodo):
        if (nodo == None):
            return
        self.recorridoEnInorden(nodo.getHijoIzquierdo())
        print(nodo.data)
        self.recorridoEnInorden(nodo.getHijoDerecho())
    
    
    def recorridoEnPreOrden(self, nodo):
        if (nodo == None):
            return
        else:
            print(nodo.data)
            self.recorridoEnPreOrden(nodo.getHijoIzquierdo())
            self.recorridoEnPreOrden(nodo.getHijoDerecho())
            
    
    def recorridoEnPostOrden(self, nodo):
        if (nodo == None):
            return
        else:
            self.recorridoEnPostOrden(nodo.getHijoIzquierdo())
            self.recorridoEnPostOrden(nodo.getHijoDerecho())
            print(nodo.data)
    
    
    def nivel(self):
            return self.nivelRecursivo(self.raiz)
            
    def nivelRecursivo(self, nodo):
        if (nodo == None):
            return -1
        else:
            nivelIzquierdo = self.nivelRecursivo(nodo.getHijoIzquierdo())
            nivelDerecho = self.nivelRecursivo(nodo.getHijoDerecho())
            
            if (nivelIzquierdo > nivelDerecho):
                return nivelIzquierdo + 1
            else:
                return nivelDerecho + 1
            
                
    def buscarRecursivo(self, nodo, dato):
        if (nodo == None):
            return None
        else:
            if (dato == nodo.data):
                return nodo.data
            else:
                if (dato < nodo.data):
                    return self.buscarRecursivo(nodo.getHijoIzquierdo(), dato)
                else:
                    return self.buscarRecursivo(nodo.getHijoDerecho(), dato)



def main():
    print(" clase Arbol Balanceado : ")
    
    a = ArbolAVL()
    a.insertar(100)
    a.insertar(50)
    a.insertar(110)
    a.insertar(25)
    a.insertar(55)
    a.insertar(15)
    a.insertar(28)
    a.insertar(29)
    a.insertar(26)
    a.insertar(105)
    a.insertar(130)
    a.insertar(135)
    a.insertar(109)
    a.insertar(131)
    print("nivel del Arbol: "+str(a.nivel()))
    a.recorridoPorNivelesIterativo()

if __name__ == "__main__":
   main()
