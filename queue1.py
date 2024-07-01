class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
       
        self.length=0
    
    def __str__(self):
        temp=self.head
        res=""
        while temp is not None:
            res+= str(temp.value)
            temp=temp.next
            if temp is not None:
                res +="<-"
        return res
    def push(self,value):
        if self.head is None:
            new=Node(value)
            self.head=new
            self.tail=new

        else:
            new=Node(value)
            self.tail.next=new
            self.tail=new
    def pop(self):
        if self.head  is None:
            return None
        else:
            poppedNode=self.head
            self.head=self.head.next
            poppedNode.next=None


queue=Queue()
queue.push(5)
queue.push(15)
queue.pop()
queue.pop()
print(queue)