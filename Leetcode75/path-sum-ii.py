# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = []

        def dfs(node, path_so_far):
            if (not node.left and not node.right) and sum(path_so_far) == targetSum:
                result.append(path_so_far)
            if node.left:
                dfs(
                    node.left, path_so_far + [node.left.val]
                )  # use + as append do not return anything
            if node.right:
                dfs(node.right, path_so_far + [node.right.val])

        if root:
            dfs(root, [root.val])
        return result
