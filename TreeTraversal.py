import queue1 as queue

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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