def height(root):
    if root == None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))
        