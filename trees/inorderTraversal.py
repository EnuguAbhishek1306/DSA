class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=TreeNode("Drinks")
leftchild=TreeNode("hot")
rightchild=TreeNode("cold")
root.left=leftchild
root.right=rightchild
def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)
inOrder(root)
