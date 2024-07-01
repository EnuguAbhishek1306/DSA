class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class CircularLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        
        temp=self.head
        result=""
        while temp is not None:
            result += str(temp.value)
            temp=temp.next
            if temp==self.head:
                break
            result += "<->"
        return result
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
            self.head.prev=self.tail

        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.tail.next=self.head
            self.head.prev=self.tail
        self.length +=1
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.head.prev=new_node
            new_node.prev=self.tail
            self.head=new_node
        self.length +=1
    def traverse(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.value)
                temp=temp.next
                if temp== self.head:
                    break
    def revTraverse(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.tail
            while temp is not None:
                print(temp.value)
                temp=temp.prev
                if temp== self.tail:
                    break
    def search(self,value):
        if self.head is None:
            return False
        else:
            temp=self.head
            while temp is not None:
                if temp.value==value:
                    return True
                temp= temp.next
                if temp== self.head:
                    return False
    def get(self,index):
        if index<0 or index>=self.length or self.head is None:
            return None
        else:
            if index<self.length/2:
                temp=self.head
                for _ in range(index):
                    temp=temp.next
            else:
                temp =self.tail
                for _ in range(self.length-1,index,-1):
                    temp=temp.prev
            return temp
    def set (self,index,value):
        if index<0 or index>=self.length :
            return None
        else :
            if index<self.length/2:
                temp=self.head
                for _ in range(index):
                    temp=temp.next
                temp.value=value
            else:
                temp =self.tail
                for _ in range(self.length-1,index,-1):
                    temp=temp.prev
                temp.value=value
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length-1:
            return self.append(value)
        else:
            new_node=Node(value)
            temp=self.get(index-1)
            new_node.next=temp.next
            temp.next=new_node
            new_node.next.prev=new_node
            new_node.prev=temp
            self.length+=1
    def popFirst(self):
        if self.head is None:
            return None
        if self.head.next==self.head:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            self.tail.next=self.head.next
            self.head=self.head.next
            self.head.prev=self.tail
            temp.next=temp.prev=None
        self.length-=1
        
    def pop(self):
        if self.head is None:
            return None
        if self.head.next==self.head:
            self.head=None
            self.tail=None
        else:
            temp=self.tail
            self.tail.prev.next=self.head
            self.tail=self.tail.prev
            self.head.prev=self.tail
            temp.next=temp.prev=None
        self.length-=1
    def remove(self,index):
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        if index <0 and index >self.length-1:
            return None
        else:
            temp=self.get(index-1)
            curr=temp.next
            
            temp.next=temp.next.next
            temp.next.prev=temp
            curr.next=curr.prev=None
            self.length-=1
        
        
        
cll=CircularLinkedlist()

cll.append(5)
cll.append(10)
cll.append(15)
cll.append(20)
cll.append(25)
cll.append(30)
cll.append(35)
cll.prepend(100)
cll.insert(2,10000)
print(cll.length)
print(cll)
print("pop")
cll.popFirst()
print(cll.length)
print(cll)
cll.remove(1)
print(cll.length)

# print(cll.search(21))


