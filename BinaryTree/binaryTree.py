class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Initialize the nodes
root = TreeNode(val=1)
node2 = TreeNode(val=2)
node3 = TreeNode(val=3)
node4 = TreeNode(val=4)
node5 = TreeNode(val=5)
node6 = TreeNode(val=6)
node7 = TreeNode(val=7)

# Connect the nodes
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# The binary tree now looks like this:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
