class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None  #first node is null
    def delete(self):
        if self.head is None:
            print("There are no elements in the linked list")
            return
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            return print(f"{l.display()} is the resultant linkedList")

    def insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
        return f"{self.display()} is the resultant linkedList"
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
        print(None)
l = LinkedList()
choice = True
while choice:
    print("1.Insert\n2.Delete\n3.Display\n4.Exit")
    choice = int(input("\nEnter the choice"))
    if choice == 1:
        value = int(input("Enter the number to insert"))
        l.insert(value)
    if choice == 2:
        l.delete()
    if choice == 3:
        l.display()
    if choice == 4:
        exit()


