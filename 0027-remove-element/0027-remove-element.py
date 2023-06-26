class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count =0
        
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[i] , nums[count] = nums[count] , nums[i]
                count+=1
                
        return count        
  ##Input code
##nums = [3, 2, 2, 3, 4, 5, 6]
##val = 3

##solution = Solution()
##new_length = solution.removeElement(nums, val)

##print("Modified list:", nums[:new_length])
##print("New length:", new_length)
