# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        def check(node, maximum):
            nonlocal res
            if node.val >= maximum:
                res += 1
                maximum = node.val
            if node.left: check(node.left, maximum)
            if node.right: check(node.right, maximum)
        check(root, float('-inf'))
        return res
            