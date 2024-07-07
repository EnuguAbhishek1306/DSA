class BinaryTree:
    def __init__(self,size):
        self.customsize=size *[None]
        self.lastUsedIndex=0
        self.maxSize=size
    def insertNode(self,value):
        if self.lastUsedIndex +1==self.maxSize:
            return "The Binary Tree is full"
        self.custom list

root=BinaryTree(8)