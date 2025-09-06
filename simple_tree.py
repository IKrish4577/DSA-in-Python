class Node:        #defined a node
    def __init__(self, data):    
        self.data = data
        self.right = None
        self.left = None
root = Node(24)             #created root as object
root.left = Node(25)
root.right = Node(27)

root.left.left = Node(26)
root.left.left.right = Node(30)

root.right.right = Node(28)
root.right.left = Node(27)
root.right.left.left = Node(41)
#tree traversal
#1. Inorder traversal (left, root, right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
print("Inorder Traversal: ", end= "")
inorder(root)
#preorder root left right
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
print("\npreorder traversal: ", end="")
preorder(root)
#left right root 
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end= " ")
print("\npostorder traversal :", end="")
postorder(root)