class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def is_bst(node, min_val, max_val):
    if node is None:
        return True
    
    if node.data <= min_val or node.data >= max_val:
        return False
    
left_check = is_bst(node.left, min_val, node.data)
right_check = is_bst(node.right, min_val, node.data)
return left_check and right_check

def check_bst(root):
    return is_bst(root, float("-int"))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

if check_bst(root):
    print("This is a valid BST.")
else:
    print("This is not a valid BST")