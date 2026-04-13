class Node:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

def find_max(root):
    if root is None:
        return float("-inf")
    
    left_max = find_max(root.left)
    right_max = find_max(root.right)

    return max(root.data, left_max, right_max)

root = Node(10)
root.left = Node(20)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(25)

result = find_max(root)
print("Maximum value in the tree is: ", result)