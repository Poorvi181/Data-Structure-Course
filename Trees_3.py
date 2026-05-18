class TreeNode:
    def __init__(self, x):
        self.data = x
        self.leftchild = None
        self.rightchild = None

def InorderTransversal(root):
    if root is not None:
        if root.leftchild is not None:
            InorderTransversal(root.leftchild)

        print(root.data)

        if root.rightchild is not None:
            InorderTransversal(root.rightchild)

def Insert(root, k):
    if root == None:
        return TreeNode(k)
    
    if root.data > k:
        root.leftchild = Insert(root.leftchild, k)
    else:
        root.rightchild = Insert(root.rightchild, k)

    return root

def Search(root, key):
    if root.data == key:
        return root
    elif root.data > key and root.leftchild is not None:
        return Search(root.leftchild, key)    
    elif root.data > key and root.rightchild is not None:
        return Search(root.rightchild, key) 
    else:
        return -1
    
n = int(input("Enter the enumber of elements you want in the tree: "))

root = None

for i in range(n):
    x = int(input("Enterthe node values: "))
    root = Insert(root, x)

InorderTransversal(root)

key = int(input("Enter the key to be searched: "))

keyNode = Search(root,key)
if keyNode == 1:
    print("Key does not exist in the tree.")
else:
    print("Key Exists", keyNode.data)



