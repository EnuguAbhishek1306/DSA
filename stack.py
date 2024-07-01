class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.length=0

    def __str__(self):
        temp=self.head
        res=""
        while temp is not None:
            res+= str(temp.value)
            temp=temp.next
            if temp is not None:
                res +="->"
        return res
    def push(self,value):
        
        if self.head is None:
            self.head=Node(value)
            self.head.next=None
        else:
            new=Node(value)
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            
            temp.next=new
            new.next=None
        self.length +=1
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def isEmpty(self):
        return self.head == None
    def peek(self):
        if self.head is None:
            return None
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        return temp.value
    def delete(self):
        self.head.next=None
        self.head=None
        
        self.length=0
stack=Stack()
print(stack.isEmpty())
stack.push(5)
stack.push(10)
stack.push(15)
stack.delete()
stack.pop()
print(stack)