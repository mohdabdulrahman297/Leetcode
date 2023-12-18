# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time : o(nlogk)
# space : o(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ## if the list is empty 
        if not lists or len(lists) == 0:
            return None
        
        ## iterate until there's one linked list left in the array of linked lists(cutting in half)
        
        while len(lists) > 1:
            mergedLists = []
            
            ## now iterate through each of these lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                ## check for non null
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists    
        return lists[0]    
        
    ## merge two lists    
    def mergeList(self, l1, l2):
        # todo
        ## create a dummy node
        dummy = ListNode()
        tail = dummy
        
        ## iterate until non null
        while l1 and l2:
            
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next    