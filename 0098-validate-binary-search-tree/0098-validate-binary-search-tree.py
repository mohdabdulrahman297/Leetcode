# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        ## valid tree algo
        def valid(node, left, right):
            if not node:
                return True
            
            ## basic valid tree checking
            if not (node.val < right and node.val > left):
                return False
            
            ## recursive call for left and right
            ## since we're moving to left, make the right node as the main node to make the algo work properly, similarly for the right as well
            
            return valid(node.left, left, node.val ) and valid(node.right, node.val, right)
        
        
        return valid(root, float("-inf"), float("inf"))