# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## track that number of elements visited from the tree
        
        n = 0
        stack = []
        ## pointer initialized to root of tree
        cur = root
        
        ## current pointer is not null and stack not empty
        while cur or stack:
            ## add the node to stack and move to left of tree
            while cur:
                stack.append(cur)
                cur = cur.left
                
           ## when cur reaches to null then pop the recent node to which cur is pointing 
            cur = stack.pop()
            ## update n and return kth smallest
            n += 1
            if n == k:
                return cur.val
            
          ## if thats not the case we already processed the cur node so move to right 
            cur = cur.right
           
        