# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxdepth = 0
    def depth(self, node):
        if not node:
            return 0   
        return 1 + max(self.depth(node.left), self.depth(node.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tmp = self.depth(root.left) + self.depth(root.right)
        if tmp > self.maxdepth:
            self.maxdepth = tmp
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.maxdepth