import TreeTraversal as treeTraversal

class AVLNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
def search(rootNode,value):
    if rootNode is None:
        return False
    if rootNode.data==value:
        return True
    elif value < rootNode.data:
        
        return search(rootNode.left,value)
    else:
        
        return search(rootNode.right,value)
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height
def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.left
    disbalanceNode.left=disbalanceNode.left.right
    newRoot.right=disbalanceNode
    disbalanceNode.height=1+max(getHeight(disbalanceNode.left),getHeight(disbalanceNode.right))
    newRoot.height=1+max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot
def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.right
    disbalanceNode.right=disbalanceNode.right.left
    newRoot.left=disbalanceNode
    disbalanceNode.height=1+max(getHeight(disbalanceNode.left),getHeight(disbalanceNode.right))
    newRoot.height=1+max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left)-getHeight(rootNode.right)
def insertNode(rootNode,value):
    if not rootNode:
        return AVLNode(value)
    elif value<rootNode.data:
        rootNode.left=insertNode(rootNode.left,value)
    else:
        rootNode.right=insertNode(rootNode.right,value)
    rootNode.height=1+max(getHeight(rootNode.left),getHeight(rootNode.right))
    balance=getBalance(rootNode)
    if balance>1 and value < rootNode.left.data:
        return rightRotate(rootNode)
    if balance >1 and value > rootNode.left.data:
        rootNode.left=leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance <-1 and value<rootNode.right.data:
        return leftRotate(rootNode)
    if balance <-1 and value> rootNode.right.data:
        rootNode.right=leftRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode
def getMinValueNode(rootNode):
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinValueNode(rootNode.left)
def Delete(rootNode,value):
    if rootNode is None:
        return rootNode
    elif value < rootNode.data:
        rootNode.left=Delete(rootNode.left,value)
    elif value>rootNode.data:
        rootNode.right=Delete(rootNode.right,value)
    else:
        if rootNode.left is None:
            temp=rootNode.right
            rootNode=None
            return temp
        elif rootNode.right is None:
            temp=rootNode.left
            rootNode=None
            return temp
        temp=getMinValueNode(rootNode.right)
        rootNode.data=temp.data
        rootNode.right=Delete(rootNode.right,temp.data)
    balance=getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.left)>=0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.right)<=0:
        return leftRotate(rootNode)
    if balance >1 and getBalance(rootNode.left)<0:
        rootNode.left=leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance <-1 and getBalance(rootNode.right)>0:
        rootNode.right=rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode
def Deletefull(rootNode):
    rootNode.left=None
    rootNode.right=None
    rootNode.data=None
    
    
    return ""
newavl=AVLNode(5)   
newavl=insertNode(newavl,10)
newavl=insertNode(newavl,20)
newavl=insertNode(newavl,30)
newavl=insertNode(newavl,40)
newavl=insertNode(newavl,50)
# treeTraversal.levelOrder(newavl)
# print("1st")
# newavl=Delete(newavl,30)
# treeTraversal.levelOrder(newavl)
# print("2nd")
newavl=Deletefull(newavl)
print('1st')



