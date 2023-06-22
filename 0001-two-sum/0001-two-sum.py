##time: o(n)
##space: o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hashmap:
                return [hashmap[difference] , i]
            hashmap[n] = i
        return   
    
    
#nums=[2,7,5,11]
#target = 9

#soluiton = Solution()

#result = solution.twoSum(nums,target)
#print(result)
        