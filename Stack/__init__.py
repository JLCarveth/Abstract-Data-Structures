class Stack:

    def __init__(self):
        self.stack = []
        self.top = 0
        
    def isEmpty(self):
        return (self.top == 0)

    def push(self, elem):
        if self.top < len(self.stack):
            self.stack[self.top] = elem
        else:
            self.stack.append(elem)

        self.top += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.top -= 1
            return self.stack[self.top]
