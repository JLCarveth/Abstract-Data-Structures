class Queue:

    def __init__(self):
        self.stack = []
        self.back = 0

    def isEmpty(self):
        return (self.back == 0)
    
    def enqueue(self, elem):
        self.stack.append(elem)

        self.back += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        
        elem = self.stack[0]

        self.stack = self.stack[1:]
        
        self.back -= 1
        
        return elem
