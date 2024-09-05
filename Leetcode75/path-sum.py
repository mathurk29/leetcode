# https://leetcode.com/problems/path-sum/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cumulative_sum):
            if not node:
                return False
            cumulative_sum += node.val
            if not node.left and not node.right:
                return cumulative_sum == targetSum
            return dfs(node.left, cumulative_sum) or dfs(node.right, cumulative_sum)

        return dfs(root, 0)
