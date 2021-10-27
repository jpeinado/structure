# Library Local
from dNodo import TreeNode
#. class what manager the structure treenode        
class MyTree:
    root = TreeNode # None
#. Constructor of class MyTree 
    ''' Clase MyTree '''   
    def __init__(self, value):
        self.__root = TreeNode(value)
        self.__Nivel = None
        self.__Altura = None
        self.__Amplitud = None
        self.__Cantidad = None
    ''' Arguments of class MyTree
    Note:
        Esta es una clase que permite manejar nodos jerarquicos
    Args:

    Returns:

    '''
    def setRoot(self,link):
        self.__root = link
    def getRoot(self):
        return self.__root


#. definition of method of class MyTree

    def addNode(self, node, value): 
        ''' Methos create node, parameter node and value.
        Args:
        node estructure of type node class.
        Returns:
        Node with value of elements, left,rigth and data.
        '''
        if(node==None):
            self.setRoot(TreeNode(value))
        else:
            if(value<node.getData()):
                if(node.getLeft()==None):
                    node.setLeft(TreeNode(value))
                else:
                    self.addNode(node.getLeft(), value)
            else:
                if(node.getRight()==None):
                    node.setRight(TreeNode(value))
                else:
                    self.addNode(node.getRight(), value)
                    
#. Method printing the data of class mytree
   
    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.getLeft())
            print(node.getData())
            self.printInorder(node.getRight())
    def printPreorder(self, node):
        if(node!=None):
            print(node.getData())
            self.printInorder(node.getLeft())
            self.printInorder(node.getRight())
    def printPostorden(self, node):
        if(node!=None):
            self.printInorder(node.getLeft())
            self.printInorder(node.getRight())
            print(node.getData())