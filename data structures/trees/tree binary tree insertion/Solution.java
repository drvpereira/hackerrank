static Node Insert(Node root, int value) {
    if (root == null) {
        root = new Node();
        root.data = value;
        return root;
    }
    
    if (value > root.data) {
        root.right = Insert(root.right, value);
    } else {
        root.left = Insert(root.left, value);
    }
    
    return root;    
}
