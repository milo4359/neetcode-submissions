# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, node):
        tmp = node.left
        node.left = node.right 
        node.right = tmp
        if node.left:
            self.swap(node.left)
        if node.right:
            self.swap(node.right)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.swap(root) 
        return root