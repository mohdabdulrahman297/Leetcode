# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ## queue follows a FIFO order
        
        ## array to store result
        res = []
        
        ##queue
        q = collections.deque()
        ## initialize the queue with the root
        q.append(root)
        
        ## iterate for q is not null
        while q:
            ##lenth of the queue
            qLength = len(q)
            ## level array
            
            level = []
            
            ## iterate and pop nodes from the queue
            
            for i in range(qLength):
                node = q.popleft()
                ## check if the node is null
                if node:
                    ## append to the level array
                    level.append(node.val)
                    ## now after the root add its left and right children to the queue
                    q.append(node.left)
                    q.append(node.right)
            ## append the level to the main result list
            ## level list should be not null
            if level:
                res.append(level)
        return res