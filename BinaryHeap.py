class Heap():
    def __init__(self,size):
        self.customList=(size+1)*[None]
        self.heapSize=0
        self.maxSize=size+1
def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])
def heapifyTreeInsert(rootnode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=='Min':
        if rootnode.customList[parentIndex]>rootnode.customList[index]:
            temp=rootnode.customList[parentIndex]
            rootnode.customList[parentIndex]=rootnode.customList[index]
            rootnode.customList[index]=temp
        heapifyTreeInsert(rootnode,parentIndex,heapType) 
    elif heapType == "Max":
        if rootnode.customList[parentIndex]<rootnode.customList[index]:
            temp=rootnode.customList[parentIndex]
            rootnode.customList[parentIndex]=rootnode.customList[index]
            rootnode.customList[index]=temp
        heapifyTreeInsert(rootnode,parentIndex,heapType) 
def insertNode(rootnode,value,heaptype):
    if rootnode.heapSize+1==rootnode.maxSize:
        return "The Binary Heap is full"
    rootnode.customList[rootnode.heapSize+1]=value
    rootnode.heapSize +=1
    heapifyTreeInsert(rootnode,rootnode.heapSize,heaptype)
    return "inserted sucessfully"
def heapifyTreeExtract(rootnode,index,heapType):
    left=index*2
    right= index*2 +1
    swap=0
    if rootnode.heapSize<left:
        return
    elif rootnode.heapSize == left:
        if heapType == 'Min':
            if rootnode.customList[index]>rootnode.customList[left]:
                temp=rootnode.customList[index]
                rootnode.customList[index]=rootnode.customList[left]
                rootnode.customList[left]=temp
            return
        else:
            if rootnode.customList[index]<rootnode.customList[left]:
                temp=rootnode.customList[index]
                rootnode.customList[index]=rootnode.customList[left]
                rootnode.customList[left]=temp
            return
    else:
        if heapType== "Min":
            if rootnode.customList[left]<rootnode.customList[right]:
                swap=left
            else:
                swap=right

            if rootnode.customList[index]>rootnode.customList[swap]:
                temp=rootnode.customList[index]
                rootnode.customList[index]=rootnode.customList[swap]
                rootnode.customList[swap]=temp
        else:
            if rootnode.customList[left]>rootnode.customList[right]:
                swap=left
            else:
                swap=right
            if rootnode.customList[index]<rootnode.customList[swap]:
                temp=rootnode.customList[index]
                rootnode.customList[index]=rootnode.customList[swap]
                rootnode.customList[swap]=temp
    heapifyTreeExtract(rootnode,swap,heapType)
def extract(rootNode,heaptype):
    if rootNode.heapSize ==0:
        return
    else:
        extract=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heaptype)
        return extract
def delete(rootNode):  
    rootNode.customList=None
    rootNode.heapSize=0    

newheap=Heap(5)
insertNode(newheap,10,"Min")
insertNode(newheap,5,"Min")
insertNode(newheap,20,"Min")
insertNode(newheap,1,"Min")
delete(newheap)
levelOrderTraversal(newheap)