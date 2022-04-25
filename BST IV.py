# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, s, k):
        if root is None:
            return False
        if (k - root.val) in s:
            return True
        else:
            s.add(root.val)

        # Note - the following return statement is inroder traversal

        return self.dfs(root.left, s, k) or self.dfs(root.right, s, k)

    def findTarget(self, root: TreeNode, k: int):
        s = set()
        return self.dfs(root, s, k)
