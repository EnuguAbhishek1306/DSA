

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        
        self.head=None
        self.tail=None
        self.length=0
    def __str__(self):
        temp=self.head
        result=""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "<->"
            temp= temp.next
        return result
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            
        else:
            
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
        self.length +=1
    def prepend(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
        self.length+=1
    def traverse(self):
 
            temp=self.head
            while temp:
                print(temp.value)
                temp=temp.next
    def reverseTraverse(self):
        temp=self.tail
        while temp:
            print(temp.value)
            temp=temp.prev
    def search(self,value):
        temp=self.head
        index=0
        while temp:
            if temp.value == value:
                return index
            temp =temp.next
            index +=1
        return False
    def get(self,index):
        if index >=self.length or index<0:
            return None
        if index <self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    def set(self,index,value):
        node=self.get(index)
        if node:
            node.value=value
            return True
        return False
    def insert(self,index,value):
        

        if index == 0:
            return self.prepend(value)
        elif index == self.length-1:
            return self.append()
        else:
            new=Node(value)
            temp=self.get(index-1)
            new.next=temp.next
            new.prev=temp
            temp.next.prev=new
            temp.next=new
        self.length +=1
    def popfirst(self):
        if self.head is None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head.next.prev=None
            self.head=self.head.next
        self.length -=1
    def pop(self):
        if self.head is None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.tail.prev
            self.tail.prev.next=None
            self.tail=temp
        self.length -=1
    def remove(self,index):
        if index <0 and index>=self.length:
            return None
        else:
            if index==0:
                return self.popfirst()
            elif index== self.length-1:
                return self.pop()
            else :
                temp=self.get(index-1)
                curr=temp.next.next
                temp.next.next=None
                temp.next=curr
                temp.next.prev=temp
                


        
        

        

            

doublylist=DoublyLinkedList()
doublylist.append(5)
doublylist.append(10)
doublylist.append(15)
doublylist.append(20)
doublylist.append(25)
doublylist.append(30)
doublylist.prepend(30)
doublylist.insert(1,1000)
doublylist.remove(7)


print(doublylist)
        

    