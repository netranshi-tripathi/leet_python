class Solution:
    def maxLevelSum(self, root):
        sums = []
        
        def traverse(node, depth):
            if not node:
                return
            
            if len(sums) == depth:
                sums.append(0)
            
            sums[depth] += node.val
            
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
        
        traverse(root, 0)
        return sums.index(max(sums)) + 1