# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ## start at the root node as current
        
        curr = root
        
        ## iterate until curr is not null
        
        while curr:
            ## if the p, q values are greater than the root(curr) move to the right subpart of the tree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
             
            ## same if less than root value then move to the left subpart of the tree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            
            ## if one of the values (p,q) matches the root then itself is the lca
            else:
                return curr
        
        