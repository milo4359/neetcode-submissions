# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def depth(node):
            if not node:
                return 0
            l, r = depth(node.left), depth(node.right)
            if abs(l - r) > 1:
                self.balanced = False
            return 1 + max(l, r)
        depth(root)
        return self.balanced