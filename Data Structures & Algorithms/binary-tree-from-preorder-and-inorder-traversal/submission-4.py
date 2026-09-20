# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = 0
        idx = {v: i for i, v in enumerate(inorder)}
        def dfs(start, end):
            nonlocal p
            if end - start < 0: return None
            val = preorder[p]
            p += 1
            i = idx[val]
            node = TreeNode(val)
            node.left = dfs(start, i - 1)
            node.right = dfs(i + 1, end)
            return node
            
        return dfs(0, len(preorder) - 1)
