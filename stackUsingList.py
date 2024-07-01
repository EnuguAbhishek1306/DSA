class Stack:
    def __init__(self):
        self.list =[]
    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return "\n".join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
        self.list.append(value)
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "there is no element"
        else:
            return self.list[len(self.list)-1] 
    def delete(self):
        self.list=[]
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.delete()

print(stack)
