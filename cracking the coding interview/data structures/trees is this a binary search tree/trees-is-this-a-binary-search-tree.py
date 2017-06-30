
def check_bst(root, minval, maxval):
    if root is not None:
        if root.data > minval and root.data < maxval:
            return check_bst(root.left, minval, root.data) and check_bst(root.right, root.data, maxval)
        else:
            return False
    else:
        return True
        
    
def check_binary_search_tree_(root):
    return check_bst(root, float('-inf'), float('inf'))