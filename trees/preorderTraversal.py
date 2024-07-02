class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
newBt=Treenode("Drinks")
leftchild=Treenode("Hot")
rightchild=Treenode("cold")

newBt.left=leftchild
newBt.right=rightchild
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right) 
preOrderTraversal(newBt)

