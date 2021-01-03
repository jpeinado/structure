#. class TreeNode what represent ADT structure
class TreeNode:
        ''' method create instance of TreeNode [Object]. Setvalue of type Object'''
        def __init__(self, value):
            self.__left = None
            self.__right = None
            self.__data = value
        ''' Arguments of class TreeNode.
        Note: 
            include arguments of type object. 
        Args:
            value(obj): first data of TreeNode.
        Returns:
            data(obj): first value of class TreeNode.
        '''
#. Methods of class TreeNode
#. Method getter y setter of class TreeNode  
        
        def getData(self):
            ''' Este metodo devuelve como valor un dato de tipo Objeto '''
            return self.__data; 
        def setData(self, x):
            ''' Este metodo recibe como valor un dato de tipo Objeto '''
            self.__data = x;
        ''' Method getter y setter for return data and set data
        Args:
            x(object): first data of TreeNode.
        Returns:
            data(object): value of field data. 
        '''
        def getLeft(self):
            return self.__left
        def setLeft(self, node):
            self.__left = node
        '''
        Method return node left of data structure treeNode.
        '''
        
        def getRight(self):
            return self.__right
        def setRight(self,node):
            self.__right = node