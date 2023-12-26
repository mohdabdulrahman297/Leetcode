# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            ## empty node is a good node
            if not node:
                return 0
            
            ## result is 1  if node value is greater then maxVal encountered so far
            
            res = 1 if node.val >= maxVal else 0
            ## update maxVal
            maxVal = max(maxVal, node.val)
            
            ## recursive call on the children(left, right) and add to the result value
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            
            return res
        
        ## call the dfs and pass the maxVal as root.val default
        
        return dfs(root, root.val)
        