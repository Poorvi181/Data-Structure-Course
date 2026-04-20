class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(count_nodes(root))  