# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        start = float('-inf')
        valid = True
        def dfs(node):
            nonlocal start, valid
            if not node or not valid: return
            dfs(node.left)
            if node.val <= start: valid = False
            start = node.val
            dfs(node.right)
        dfs(root)
        return valid
            
            
            
        