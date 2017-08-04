class Node:
    def __init__(self, elem, _next):
        self.elem = elem
        self.next = _next

class LinkedList:
    def __init__(self):
        '''
        Initialize the Linked List
        We create an empty head variable which tracks the first
        element in the list. The size of the Linked List is defaulted to 0.
        '''
        self.head = None
        self.size = 0

    def isEmpty(self):
        '''
        @return true if the LinkedList is empty (has no elements)
        '''
        return self.size == 0

    def addFirst(self, elem):
        '''
        Adds an element to the beginning of the list.
        @param elem: the element to add to the list.
        '''
        self.head = Node(elem, self.head)
        self.size += 1

    def append(self, elem):
        '''
        Appends an item to the end of the list.
        @param elem: the element to add to the list.
        '''
        temp = self.head

        while (temp.next != None):
            temp = temp.next

        temp.next = Node(elem, None)

    def add(self, elem, index):
        '''
        Adds an element to the specified position in the list.

        @param elem: the element to add to the list
        @param index: the position in the list where the
                element will be inserted
        '''

        temp = self.head                # Create a temporary copy of the head

        for i in range(1, self.size):   # Go through list until index reached
            if i == index:
                temp.elem = elem        # Replace the element with param
                self.size += 1
                return
            else:
                temp = temp.next
            
                
        
    def remove(self):
        '''
        Removes the first item in the list.
        '''
        if self.isEmpty():
            return None
        else:
            item = self.head.elem
            self.head = self.head.next
            self.size -= 1
            return item

    def toString(self):
        temp = self.head

        while(temp != None):
            print(temp.elem)
            temp = temp.next
