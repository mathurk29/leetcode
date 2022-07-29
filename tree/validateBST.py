# Definition for a binary tree node.

import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recursive(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BST
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (
                recursive(node.left, low, node.val)
                and
                recursive(node.right, node.val, high)
            )

        return recursive(root)
