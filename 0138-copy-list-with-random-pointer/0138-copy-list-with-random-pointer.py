"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

## space : o(n)
## time : o(n)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ## a hashmap with null pointing to null for mapping old node to the copy of that node
        oldToCopy = {None: None}
        
        ## iterating and cloning each node(1st pass)
        cur = head
        while(cur):
            copy = Node(cur.val)
            ## map the old node to the copy created
            oldToCopy[cur] = copy
            ## update pointer until it reaches null
            cur = cur.next
            
        ## iterating  and setting the pointers
        cur = head
        while(cur):
            copy = oldToCopy[cur]
            ## using the copy to set the pointers
            copy.next = oldToCopy[cur.next]
            ## same for random
            copy.random = oldToCopy[cur.random]
            ## updating the pointers
            cur = cur.next
            
        return oldToCopy[head]   
        