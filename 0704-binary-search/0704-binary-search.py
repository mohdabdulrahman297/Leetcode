## time: o(log n)
## space: o(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ##initialize the pointers
        l, r = 0, len(nums) - 1
        
        ## iterate such that l<=r
        while(l<=r):
            ##calculate the mid
            m = (l+r) // 2
            
            if(nums[m] > target):
                ## perform in the left half
                r = m-1
            elif(nums[m] < target):
                ## perform in the right half
                l = m+1
            else:
                return m
        return -1       