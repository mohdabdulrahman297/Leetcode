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
    
 # Create an instance of the Solution class
##solution = Solution()

# Test case 1
##nums1 = [1, 2, 2, 2, 3]
##print(solution.majorityElement(nums1))  # Output: 2

# Test case 2
##nums2 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
##print(solution.majorityElement(nums2))  # Output: 4

# Test case 3
##nums3 = [1, 1, 1, 2, 3, 4]
##print(solution.majorityElement(nums3))  # Output: 1   
        