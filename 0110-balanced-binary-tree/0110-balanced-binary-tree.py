# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ## recursive solution
        
        def dfs(root):
            ## if null condition
            if not root: return [True, 0]
            
            ## now get the left and right nodes of tree
            left, right = dfs(root.left), dfs(root.right)
            
            ## calculate balanced (true or false)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            ## returns boolean and height
            return [balanced, 1+max(left[1], right[1])]
        
        
    
        ## return boolean         
        return dfs(root)[0]    