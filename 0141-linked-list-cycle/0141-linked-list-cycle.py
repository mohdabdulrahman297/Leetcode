# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Time: O(n)
#Space: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## pointers
        slow, fast = head, head
        
        ## itearate until non null
        while fast and fast.next:
            ## slow = +1 
            ## fast = +2
            slow = slow.next
            fast = fast.next.next
            ## if a cycle exists then the two pointers will be at the same point at some certain time
            if slow == fast:
                return True
        
        
        return False