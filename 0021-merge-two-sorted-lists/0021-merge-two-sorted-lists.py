# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ## create a dummy node 
        dummy = ListNode()
        tail = dummy
        
        ## both linked lists should be not null
        while(list1 and list2):
            ## compare both the values in the lists and place the small one into the result which is tail
            if(list1.val < list2.val):
                tail.next = list1
                ## increament the pointer
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        ## if one of the list is non null
        if(list1):
            tail.next = list1
        elif(list2):
            tail.next = list2
            
        return dummy.next    
        