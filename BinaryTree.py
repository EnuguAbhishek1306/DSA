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
print("levelorder")
levelOrder(root)