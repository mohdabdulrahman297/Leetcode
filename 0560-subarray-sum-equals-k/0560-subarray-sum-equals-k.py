## time:o(n)
## space: o(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ## count for counting subarrays in the input array
        count = 0
        
        sum = 0
        
        ## create a dic to store the frequency as values
        dic = {}
        
        ## initialize 1st value as {0:1}
        dic[0] = 1
        
        for i in range(len(nums)):
            
            sum = sum + nums[i]
            
            ## check sum-k already exists in dic or not  , if exists then increament count
            if(sum-k) in dic:
                count = count + dic[sum-k]
                
            ## update dic
            dic[sum] = dic.get(sum,0) + 1
            
        return count    
        
        
        
        