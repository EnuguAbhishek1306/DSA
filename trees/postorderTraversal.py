class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
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
def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)
postOrder(root)