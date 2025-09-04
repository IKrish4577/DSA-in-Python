class queue:
    def __init__(self):
        self.queue = []
    #Enqueue -> insert at rear
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    #dequeue -> remove from front
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self.queue.pop(0) #pop the element of 0 index
    #peek -> get from element
    def peek(self):
        if self.is_empty():
            return "queue is empty"
        return self.queue[0]
    # check if empty
    def is_empty(self):
        return len(self.queue) == 0
    #display queue
    def display(self):
        print("queue", self.queue)    
    
q = queue()
while(True):
    print("CHOICES\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        val = int(input("Enter the number to Enqueue"))
        q.enqueue(val)
    if choice == 2:
        print(q.dequeue())
    if choice == 3:
        print(q.peek())
    if choice == 4:
        q.display()
    if choice == 5:
        break