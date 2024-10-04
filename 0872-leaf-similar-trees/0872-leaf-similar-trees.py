# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findLeaf(root1) == self.findLeaf(root2)
        
    def findLeaf(self, root):
        left_children = root.left
        right_children = root.right
        if left_children and  right_children:
            return list(self.findLeaf(left_children)) + list(self.findLeaf(right_children))
        elif left_children:
            return list(self.findLeaf(left_children))
        elif right_children:
            return list(self.findLeaf(right_children))
        else:
            return [root.val]

        
        