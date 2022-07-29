# Definition for a binary tree node.
import math
from turtle import right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass

        def recursive(node, low=-math.inf, high=math.inf):

            # empty trees are valid BST
            if node is None:
                return True

            if not (low <= node.val <= high):
                return False

            return (
                recursive(node.left, low=low, high=node.val)
                and
                recursive(node.right, low=node.val, high=high)
            )
