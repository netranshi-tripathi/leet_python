# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_zigzag = 0

    def dfs(self, node, last, length):
        if not node:
            return
        
        self.max_zigzag = max(self.max_zigzag, length)
        
        self.dfs(node.left, 'l', length + 1 if last != 'l' else 1)
        self.dfs(node.right, 'r', length + 1 if last != 'r' else 1)

    def longestZigZag(self, root):
        self.dfs(root, 'l', 0)
        return self.max_zigzag