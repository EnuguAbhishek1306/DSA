class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += " -> "
        return result
     
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node

        self.length +=1
    def prepend(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.tail.next=new_node
            self.head=new_node
        self.length +=1
    def insert(self,index,value):
        
        if index<0 or index >= self.length:
            return None
        if index ==0:
            return self.prepend(value)
        elif index == self.length-1:
            return self.append(value)
        else:
            new_node=Node(value)
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def traversal(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            
            temp=temp.next
            if temp == self.head:
                break
    def search(self,value):
        temp=self.head
        while temp is not None:
            if temp.value==value:
                return True
            temp=temp.next
            if temp == self.head:
                break
        return False
    def get(self,index):
        
        if index<0 or index>self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set(self,index,value):
        if index < 0 or index >self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
    def popfirst(self):
        if self.head is None:
            return None
        poped_node=self.head
        self.tail.next=poped_node.next
        self.head=poped_node.next
        poped_node.next=None
        self.length -=1
    def pop(self):
        if self.head is None:
            return None
        if self.head==self.tail:
            self.head=None
            self.tail=None   
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            poped=self.tail
            temp.next=self.head
            self.tail=temp
            poped.next=None
        self.length -=1  

    def remove(self,index):
        if index <0 or index > self.length:
            return None
        if index == 0:
            self.popfirst()
        elif index == self.length-1:
            self.pop()
        else:
            prev=self.get(index-1)
            curr=self.get(index)
            prev.next=curr.next
            curr.next=None
        self.length-=1
    def delete(self):
        self.head=None
        self.tail=None
        self.tail.next=None
        self.length=0



cll=CircularLinkedList()
cll.append(10)
cll.append(30)
cll.append(50)
cll.append(50)
cll.append(40)
cll.prepend(100)
cll.insert(0,1000)
print(cll)

cll.pop()
# print(cll.get(3).value)

print(cll)


