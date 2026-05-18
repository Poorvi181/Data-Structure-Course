class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
    
def Insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.data:
        root.left = Insert(root.left, value)
    
    else:
        root.right = Insert(root.right, value)

    return root

def find_min(root):
    if root is None:
        return None
    
    current = root

    while current.left is not None:
        current = current.left

    return current.data

n = int(input("Enter number of elements: "))
root = None
for i in range(n):
    value = int(input("Enter values: "))
    root = Insert(root, value)

minimum = find_min(root)
print("Minimum value of BST is: ", minimum)