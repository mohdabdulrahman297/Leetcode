## linked list class
class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        ## create a array of linkedlist node of size 10000
        self.set = [ListNode(0) for i in range(10**4)]
        
        

    def add(self, key: int) -> None:
        ## this gives us the index
        curr = self.set[key% len(self.set)]
        ## iterate till next element of node is non zero
        
        while curr.next:
            ## check for duplicate key
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)    
        

    def remove(self, key: int) -> None:
        ## this gives us the index
        curr = self.set[key% len(self.set)]
        ## iterate till next element of node is non zero
        
        while curr.next:
            ## check for duplicate key
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next  
        

    def contains(self, key: int) -> bool:
        ## this gives us the index
        curr = self.set[key% len(self.set)]
        ## iterate till next element of node is non zero
        
        while curr.next:
            ## check for duplicate key
            if curr.next.key == key:
                return True
            curr = curr.next
        return False  
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)