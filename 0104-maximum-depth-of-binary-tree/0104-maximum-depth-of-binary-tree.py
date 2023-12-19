# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## BFS (traversing by level) involves a queue
        if not root:
            return 0
        
        ## maintaining a level
        level = 0
        ## a deque(queue)
        q = deque([root])
        ## loop until queue is non null
        while q:
            for i in range(len(q)):
                ## pop the root from the queue and move on to the children if they are non null
                node = q.popleft()
                if node.left:
                    ## if non null then add them into the queue
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level+=1
        return level    
        
        