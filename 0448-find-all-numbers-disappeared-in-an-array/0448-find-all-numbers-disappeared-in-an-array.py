#time: o(n)
#space : o(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # multiply all values of nums with -1
        for n in nums:
            
            i = abs(n) -1
            nums[i] = -1*abs(nums[i])
        
        result = []
        for i , n  in enumerate(nums):
            if(n > 0):
                result.append(i+1)
                
        return result
        
        
#ums = [4, 3, 2, 7, 8, 2, 3, 1]
#olution = Solution()
#esult = solution.findDisappearedNumbers(nums)
#rint(result)
#       