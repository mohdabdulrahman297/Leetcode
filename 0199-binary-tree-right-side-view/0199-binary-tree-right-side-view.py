# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ## intialize a empty result
        res = []
        ## queue initizlized with the root of the tree
        q = collections.deque([root])
        
        ## iterate and pop elements if the queue is not null
        
        while q:
            rightSide = None
            qLength = len(q)
            
            for i in range(qLength):
                node = q.popleft()
                ## check the node should be not null and if not null update the rightSide
                if node:
                    rightSide = node
                    ## append the nodes children
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightSide:
                res.append(rightSide.val)
                
        return res      
        
        