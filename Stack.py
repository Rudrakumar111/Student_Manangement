class Stack:
    def __init__(self, hlength):
        self.stack = []
        self.hlength = hlength

    def pop1(self):
        if self.isEmpty() :
            return "Stack is Empty"
        return self.stack.pop()
         

    def push(self,element):
        if self.isFull():
            return "Stack is Full"
        self.stack.append(element)
        return "add Successfully"
        
    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[len(self.stack) - 1]
    
    def isEmpty(self):
        return len(self.stack) == 0 
            

    def isFull(self):
        return (len(self.stack) == self.hlength)
            
    def length(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)


s = Stack(10)
print(s.push(3))
print(s.push(4))
print(s.push(1))
print(s)

print(s.length())

print("remove this element",s.pop1())
s.pop1()
s.pop1()
s.pop1()

print(s.top())
print(s.length())

