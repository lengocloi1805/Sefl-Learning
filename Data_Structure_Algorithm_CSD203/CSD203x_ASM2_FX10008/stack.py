class Stack:
    def __init__(self):
        self.stack = []

    def add(self,product):
        self.stack.append(product)

    def peek(self):
        if (len(self.stack) <= 0):
            return None
        return self.stack[len(self.stack) -1]
    
    def remove(self):
        if (len(self.stack) <= 0):
            return None
        else:
            return self.stack.pop()