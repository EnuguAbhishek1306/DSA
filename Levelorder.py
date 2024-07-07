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