def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
