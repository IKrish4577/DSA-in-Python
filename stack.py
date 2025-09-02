stack = []


print("1. Push  2. Pop  3. Display  4. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter element to push: ")
        stack.append(element)
        print(f"Pushed {element} to stack.")
    elif choice == 2:
        if stack:
            popped_element = stack.pop()
            print(f"Popped {popped_element} from stack.")
        else:
            print("Stack is empty. Cannot pop.")
    elif choice == 3:
        if stack:
            print("Current stack:", stack)
        else:
            print("Stack is empty.")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")







