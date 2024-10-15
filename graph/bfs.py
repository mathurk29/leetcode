# https://www.youtube.com/watch?v=pcKY4hjDrxk Abdul Bari


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_traversal(root):
    if not root:
        return []

    bfs = []
    node_queue = deque([root])  # cause we will have to pop from left

    while node_queue:
        node = node_queue.popleft()
        bfs.append(node.val)

        if node.left:
            node_queue.append(node.left)
        if node.right:
            node_queue.append(node.right)

    return bfs
