'''
Title: Estructura que me permite almacenar datos que se pueden vincular entre si,
denominda Nodo. Estructura dinamica
Autor: Juan Carlos Peinado Pereira
Fecha: 30/09/2021
Version : 1.0
'''
#. class TreeNode what represent ADT structure
class TreeNode:
        ''' method create instance of TreeNode [Object]. Setvalue of type Object'''
        def __init__(self, value):
            self.__left = None
            self.__right = None
            self.__father = None
            self.__data = value
        ''' Arguments of class TreeNode.
        Note: 
            include arguments of type object. 
        Args:
            value(obj): first data of TreeNode.
        Returns:
            data(obj): first value of class TreeNode.
        '''
        def __init__(self, value, Hizq, Hder, fat):
            pass
#. Methods of class TreeNode
#. Method getter y setter of class TreeNode  
        @property
        def __getData(self):
            ''' Este metodo devuelve como valor un dato de tipo Objeto '''
            return self.__data 
        @data.setter #propiedad SETTER
        def __setData(self, x):
            ''' Este metodo recibe como valor un dato de tipo Objeto '''
            self.__data = x
        ''' Method getter y setter for return data and set data
        Args:
            x(object): first data of TreeNode.
        Returns:
            data(object): value of field data. 
        '''
        def __getLeft(self):
            return self.__left
        ''' Method getter y setter for return data and set data'''
        def __setLeft(self, node):
            self.__left = node
        '''
        Method return node left of data structure treeNode.
        '''
        
        def __getRight(self):
            return self.__right
        def __setRight(self,node):
            self.__right = node

def main():
    myNodo = TreeNode()
    myNodo.setData(10)
    myNodo.data = 20
    print(myNodo.getData())
    print(myNodo.data)
    pass

if __name__ == '__main__':
    main()