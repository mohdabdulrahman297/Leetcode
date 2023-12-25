# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        
        ## if the subtree is empty then it is subtree
        
        if not t:
            return True
        
        ## the main tree is emptyh then not a subtree
        
        if not s:
            return False
        
        ## if both trees are equal then true
        if self.sameTree(s, t):
            return True
        
        ## if not the same subtree then move to the left or right node of the main tree
        return (self.isSubtree(s.left, t) or
        self.isSubtree(s.right, t))
        
        
        
        
        
        
        
        
        
        
        
    ## check same tree condition
    
    def sameTree(self, s, t):
        
        ## check if both are null
        if not s and not t:
            return True
        
        ## check if one of them is not null and both tree node values are equal
        ## if equal then move forward to other nodes i,e left and right recursively
        
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and (self.sameTree(s.right, t.right)))
        