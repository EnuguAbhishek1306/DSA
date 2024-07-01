class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp=self.head
        result=""
        while temp is not None:
            result+= str(temp.value)
            if temp.next is not None:
                result += "->"
            temp=temp.next
        return result
            
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1 
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1
    def insert(self,index,value):
        new_node=Node(value)
        if index <0 or index>self.length:
            return False
        elif index == 0:
            new_node.next=self.head
            self.head=new_node
        
        else:
            temp=self.head
            for _ in range(index-1):
                temp =temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length +=1
        return True
    def search(self,target):
        temp=self.head
        while temp is not None:
            if target== temp.value:
               return True
            temp=temp.next 
        return False
    def get(self,index):
        if index == -1:
            return self.tail 
        if index<-1 or index>=self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp=temp.next
            return temp
    def setMethod(self,index,newValue):
        if index < 0 or index>= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp=temp.next
        temp.value=newValue
        return temp.value
    def traverse(self):
        temp=self.head
        while temp is not None:
        
            print(temp.value)
            temp=temp.next

    def popfirst(self):
        if self.length == 0:
            return None
        poped_node=self.head
        if self.head.next is None:
            self.head=None
            self.tail=None
        else:
           self.head=self.head.next
           poped_node.next=None
        self.length -=1
        return poped_node.value
    def pop(self):
        if self.length==0:
            return None
        poped_node=self.tail
        if self.head.next==None:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=None
            self.tail=temp
        self.length -=1
        return poped_node.value
    def remove(self,index):
        if index ==0:
            return self.popfirst()
        if index < 0 or index >= self.length:
            return None
        if index == self.length-1:
            return self.pop()
        else:
            prevnode=self.get(index-1)
            removenode=self.get(index)
            prevnode.next=removenode.next
            removenode.next=None
            self.length -=1
            return removenode
    def removeval(self,target):
        currentNode=self.head
        preNode=None
        while currentNode is not None :
            if currentNode.value==target:
                if preNode is None:
                    self.head=currentNode.next
                else:

                   preNode.next=currentNode.next
                if currentNode.next is None:
                    self.tail=preNode
                currentNode.next=None
                self.length-=1
                return currentNode
            preNode=currentNode
            currentNode=currentNode.next
        return None
    def reverse(self):
        temp=self.head
        prev=None
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head,self.tail=self.tail,self.head
        
        
    def deleteall(self):
        self.head = None
        self.tail = None
        self.length=0
            
            
            


        
               

       
           
        
linked_list=LinkedList()
linked_list.append(10)
linked_list.prepend(30)
linked_list.append(50)
linked_list.append(60)
linked_list.setMethod(2,100)


# print(linked_list.search(30))
# print(linked_list.get(-1))




linked_list.reverse()
print(linked_list)
# linked_list.traverse()