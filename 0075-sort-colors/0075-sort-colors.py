class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ## initialize three pointers left, right and i
        
        l, r = 0, len(nums) - 1
        i = 0
        
        ## swap function
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        ## note out i pointer should not cross right pointer
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1  ## Increment i here
                
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                ## note if 2 is encountered we should not increment i
                
            else:
                i += 1  ## Increment i if the element is 1