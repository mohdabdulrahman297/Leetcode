class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## pointers that start with 0
        slow, fast = 0, 0
        ## iterate to detect loop in array
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
        ## another pointer to find entry point of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
                
        return slow        
        
        