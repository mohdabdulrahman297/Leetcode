# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Time: O(max(m, n))
#Space: O(max(m, n))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## creating a dummy node
        
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        ## iterate unitl non null
        while(l1 or l2 or carry):
            ## get the digits
            ## if l1 is null then set the digit to zero
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            
            ## computing the digit
            val = v1 + v2 + carry
            ## if the computed digit is 2 digit ex: 15
            ##get the carry out of it
            carry = val // 10
            ## get the ones place digit
            val = val % 10
            ## insert
            cur.next = ListNode(val)
            
            ##update pointters
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next