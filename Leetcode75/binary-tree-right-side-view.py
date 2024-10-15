# https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        max_depth_so_far = 1
        node_queue = deque([root])

        while node_queue:
            node = node_queue.pop()
            result.append(node)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)

        return result
