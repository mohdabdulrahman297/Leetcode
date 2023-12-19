# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## creating a dummy node initialized with 0 and its nextpointer pointing towards head
        dummy = ListNode(0, head)
        ## another pointer that starts before the group such that we can access the group 
        groupPrev = dummy
        
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            ## pointer that is from kth next
            groupNext = kth.next
            
            # reverse group
            # we're not setting the prev to null because it will spilt the list and groupPrev is now the head
            prev, curr = kth.next, groupPrev.next
            
            ## normal reversing
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            ## updating the groupPrev and putting kth at the beginning of this group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next     
            
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr       
        
        
        