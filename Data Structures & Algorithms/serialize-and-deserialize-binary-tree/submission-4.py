# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node: return ""
            string = "[" + str(node.val)
            if node.left:
                string += "l" +  dfs(node.left)
            if node.right:
                string += "r" + dfs(node.right)
            string += "]"
            return string

        return dfs(root)
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        s = 0
        def dfs():
            nonlocal s
            if s >= len(data): return None
            
            if data[s] == "[":
                s += 1
                sign = 1
                if data[s] == "-":
                    sign = -1
                    s += 1
                start = s
                while data[s].isdigit():
                    s += 1
                val = sign * int(data[start:s])
                node = TreeNode(val)
                if data[s] == "l": 
                    s += 1
                    node.left = dfs()
                if data[s] == "r":
                    s += 1
                    node.right = dfs()
                if data[s] == "]": s += 1
                return node

        return dfs()
        
        






