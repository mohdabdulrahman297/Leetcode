# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        ## check both tree nodes are null
        if not p and not q:
            return True
        
        ## check if one of then is null or the node values are not equal
        if not p or not q or p.val != q.val:
            return False
        
        ## same recursive call for left and right subtrees
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
        