# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## creating a dummy node with head as 0 and its next as head
        dummy = ListNode(0, head)
        ## creating two pointers left and right
        
        ## left starts from the dummy node and right from its next i,e head
        left = dummy
        right = head
        
        ## loop 
        while(n>0 and right):
            ## +1
            right = right.next
            ##-1
            n-=1
            
        ## loop again such that the difference between the two pointers is n
        while(right):
            left = left.next
            right = right.next
            
        ## delete the node
        ## shifting the pointer to the desired node , we're not keeping track and storing the pointer in some variable hence the node gets lost(Deleted)
        left.next = left.next.next
        return dummy.next
        