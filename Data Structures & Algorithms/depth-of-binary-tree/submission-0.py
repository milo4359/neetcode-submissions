# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def travel(self, node, depth):
        if not node:
            return depth
        depth += 1
        return max(self.travel(node.left, depth), self.travel(node.right, depth))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.travel(root, 0)