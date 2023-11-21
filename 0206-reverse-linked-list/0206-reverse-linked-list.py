# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## initialize two pointers
        
        prev = None
        curr = head
        
        ## iterate if the head is not null
        
        while curr:
            temp = curr.next
            ## now this indicates the last element in the list 
            curr.next = prev
            ## shifitng the pointers forward
            prev = curr
            curr = temp
            
        return prev    