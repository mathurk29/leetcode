# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(root, max_upto_now):
            nonlocal result
            if not root:
                return
            if root.val >= max_upto_now:
                result += 1
                max_upto_now = root.val
            if root.left:
                dfs(root.left, max_upto_now)
            if root.right:
                dfs(root.right, max_upto_now)

        dfs(root, root.val)
        return result


# changed func call - added default param
# 1 + True = 2 i.e. int(True) = 1


class Solution2:
    def goodNodes(self, r: TreeNode, ma=-10000) -> int:
        return (
            self.goodNodes(r.left, max(ma, r.val))
            + self.goodNodes(r.right, max(ma, r.val))
            + (r.val >= ma)
            if r
            else 0
        )
