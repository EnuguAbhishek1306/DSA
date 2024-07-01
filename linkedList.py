class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
# class LinkedList:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
    def insert(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else: 
            new_node.next=self.head
            self.head=new_node
        self.length=+1
    def __str__(self) -> str:
        temp_node=self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result
            
new_linkedlist=LinkedList()
new_linkedlist.append(10)
new_linkedlist.append(20)
new_linkedlist.insert(30)
print(new_linkedlist)