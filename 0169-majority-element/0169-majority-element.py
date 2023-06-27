class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## bayer moore algorithm
        result = 0
        count = 0
        
        for i in nums:
            if(count == 0):
                result =i
            ## increament count by 1 if result = element else decreament count by 1
            count += (1 if i == result else -1)
        return result    
        