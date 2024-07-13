
import TreeTraversal as TreeTraversal
class BSTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(rootNode,value):
    if rootNode.data is None:
        rootNode.data=value
    elif value <= rootNode.data:
        if rootNode.left is None:
            rootNode.left=BSTreeNode(value)
        else:
            insert(rootNode.left,value)
    else: 
        if rootNode.right is None:
            rootNode.right=BSTreeNode(value)
        else:
            insert(rootNode.right,value)
def search(rootNode,value):
    if rootNode is None:
        return False
    if rootNode.data==value:
        return True
    elif value < rootNode.data:
        
        return search(rootNode.left,value)
    else:
        
        return search(rootNode.right,value)
def minvalueNode(rootNode):
    current=rootNode
    while current.left is not None:
        current=current.left
    return current
def Delete(rootNode,value):
    if rootNode is None:
        return None
    elif value < rootNode.data:
        rootNode.left=Delete(rootNode.left,value)
    elif value> rootNode.data:
        rootNode.right=Delete(rootNode.right,value)
    else: 
        if rootNode.left is None:
            temp= rootNode.right
            rootNode=None
            return temp
        if rootNode.right is None:
            temp=rootNode.left
            rootNode=None
            return temp
        temp=minvalueNode(rootNode.right)
        rootNode.data=temp.data
        rootNode.right=Delete(rootNode.right,temp.data)
    return rootNode
def Deleteall(rootNode):
    rootNode=None
    rootNode.left=None
    rootNode.right=None
# bst=BSTreeNode(None)
# insert(bst,70)
# insert(bst,50)
# insert(bst,90)
# insert(bst,30)
# insert(bst,60)
# insert(bst,80)
# insert(bst,100)
# insert(bst,20)
# insert(bst,40)
# Delete(bst,71)
# TreeTraversal.levelOrder(bst) 

