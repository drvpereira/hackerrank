void leftPostOrder(Node root) {
    if (root != null) {
        leftPostOrder(root.left);
        System.out.print(root.data + " ");
    }
}
void rightPreOrder(Node root) {
    if (root != null) {
        System.out.print(root.data + " ");
        rightPreOrder(root.right);
    }
}

void topView(Node root) {
    leftPostOrder(root.left);
    System.out.print(root.data + " ");
    rightPreOrder(root.right);
}
