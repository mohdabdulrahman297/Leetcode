class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## convert nums array into a set
        NumSet = set(nums)
        longest = 0
        
        for n in nums:
            ## check if its the starting of a sequence
            if(n-1) not in NumSet:
                length = 0
                ##check current numer in numset or not
                while(n+length) in NumSet:
                    length+=1
                    
                longest  = max(length , longest)
                
        return longest      
     
# Example input
#nums = [100, 4, 200, 1, 3, 2]

#solution = Solution()
#result = solution.longestConsecutive(nums)
#print(f"Input: {nums}, Longest Consecutive Length: {result}")#        