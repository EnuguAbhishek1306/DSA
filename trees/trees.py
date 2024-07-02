class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=Treenode(data)
        self.right=Treenode(data)
newBt=Treenode("Drinks")

