# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        ## two pointers fast and slow
        ## slow and fast these are used to separate the list into two halfs
        
        slow, fast = head, head.next
        ## fast is not null and fast has not reached the end of entire list
        while(fast and fast.next):
            ## slow is +1 and fast is +2
            slow = slow.next
            fast = fast.next.next
            
            ## now the fast has reached end and slow.next is the beginning of the second half of the list
        second = slow.next
        ## reverse the second half
        prev = None
        slow.next = None
        
        while(second):
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        ## merge two halfs (now the prev is the new head og the seoncd half of the list)
        
        first, second = head, prev
        while(second):
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        first, second = head, prev
        