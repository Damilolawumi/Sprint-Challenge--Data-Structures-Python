from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
       
        #if not at capacity, append to the end of list
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item) # add item to the tail
            self.current = self.storage.tail #this is because it got added to the tail

        #if at capacity, connect storage head to tail
        if self.storage.length == self.capacity:  
            if self.current is self.storage.tail: 
                self.storage.tail.next = self.storage.head 

        self.current.value = item
        self.current = self.current.next        

            


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        current = self.storage.head #We set the current to the head of the storage.

        while current is not None: # as long as current has a value
            list_buffer_contents.append(current.value) #add value of current to end of empty list created

            current = current.next  #and repeat with each num

            if current is self.storage.head:
                break
            
        return list_buffer_contents
     
rb = RingBuffer(4)
rb.append(10)
rb.append(5)
rb.append(8)
rb.append(8)
print(rb.get())        

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
