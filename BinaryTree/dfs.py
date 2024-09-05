from binaryTree import root


def dfs_preorder(root):
    print(root.val)
    dfs_preorder(root.left)
    dfs_preorder(root.right)


def dfs_inorder(root):
    dfs_preorder(root.left)
    print(root.val)
    dfs_preorder(root.right)


def dfs_postorder(root):
    dfs_preorder(root.left)
    dfs_preorder(root.right)
    print(root.val)


dfs_preorder(root)
dfs_inorder(root)
dfs_postorder(root)
