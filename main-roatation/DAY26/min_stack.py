class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push_num(self,num):
        if self.minstack and self.minstack[-1] < num:
            self.stack.append(num)
            self.minstack.append(self.minstack[-1])
        else:
            self.stack.append(num)
            self.minstack.append(num)
        

    def pop_num (self):
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
            return self.minstack
        else:
            return 0
    
    def getMin(self):

        num = self.minstack[-1]

        return num
    

stack = MinStack()
stack.push_num(2)
stack.push_num(3)
stack.push_num(1)
stack.push_num(5)
stack.push_num(6)
stack.push_num(7)
stack.push_num(8)
print(stack.stack)
print(stack.minstack)


