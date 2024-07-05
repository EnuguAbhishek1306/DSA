import queue1 as queue

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right) 

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        custom=queue.Queue()
        custom.enqueue(rootNode)
        while not (custom.isempty()):
            root=custom.dequeue()
            print(root.data)
            if root.left:
                custom.enqueue(root.left)
            if root.right:
                custom.enqueue(root.right)
root=TreeNode("Drinks")
leftside=TreeNode("Hot")
rightside=TreeNode("cold")
leftlchild=TreeNode("coffee")
leftrchild=TreeNode("Tea")
rightlchild=TreeNode("beer")
rightrchild=TreeNode("cool drink")
root.left=leftside
root.right=rightside
leftside.left=leftlchild
leftside.right=leftrchild
rightside.left=rightlchild
rightside.right=rightrchild

# print("Inorder")
# inOrder(root)
# print("postorder")
# postOrder(root)
# print("preorder")
# preOrderTraversal(root)
# print("levelorder")
# levelOrder(root)
def search(rootNode,value):
    if rootNode is None:
        return "Not BT not exist"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isempty() :
            root=customQueue.dequeue()
            if root.data == value:
                return "success"
            
            if root.left:
                customQueue.enqueue(root.left)
            if root.right:
                customQueue.enqueue(root.right)
        return "Not Found"
def insert(rootNode,newNode):
    if rootNode is None:
        rootNode=newNode
    else:
        cqueue=queue.Queue()
        cqueue.enqueue(rootNode)
        while not cqueue.isempty():
            root=cqueue.dequeue()
            if root.left:
                cqueue.enqueue(root.left)
            else:
                root.left=newNode
                return "successfully insereted"
            if root.right:
                cqueue.enqueue(root.right)
            else:
                root.right=newNode
                return "successfully insereted"
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not customqueue.isempty():
            root =customqueue.dequeue()
            if root.left:
                customqueue.enqueue(root.left)
            if root.right:
                customqueue.enqueue(root.right)
        
        return root
def deletedeepNode(rootNode,DNode):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not customqueue.isempty():
            root = customqueue.dequeue()
            if root==DNode:
                root.data=None
                return
            if root.right:
                if root.right is DNode:
                    root.right=None
                    return
                else:
                    customqueue.enqueue(root.right)
            if root.left:
                if root.left is DNode:
                    root.left=None
                    return
                else:
                    customqueue.enqueue(root.left)
def deleteNode(rootNode,node):
    if not rootNode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootNode)
        while not customqueue.isempty():
            root = customqueue.dequeue()
            if root.data==node:
                dNode=getDeepestNode(rootNode)
                root.data=dNode.data
                deletedeepNode(rootNode,dNode)
                return "The node as been success fully deleted"
            if root.left:
                customqueue.enqueue(root.left)
            if root.right:
                customqueue.enqueue(root.right)
        return "Failed to delete"
def delete(rootNode):
        rootNode.data=None
        rootNode.left=None
        rootNode.right=None
        return "deleted succesfully"

postOrder(root)

