## time:o(n^2)
## space: o(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ## create an ouput vector
        res = []
        
        ## sort the array
        
        nums.sort()
        
        ## now for the first value i.e a 
        
        for i , a in enumerate(nums):
            
            ## if i > 0 means first value is positve and a is equal to previous value then do nothing and move on
            
            if i > 0 and a == nums[i-1]:
                continue
                
            ## initialize the pointers for second and third values i.e b and c
            
            l , r = i+1, len(nums)-1
            while l< r:
                ## calculate the current sum
                threeSum = a + nums[l] + nums[r]
                
                if(threeSum > 0):
                    r-=1
                elif(threeSum < 0):
                    l+=1
                    
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    ##update the pointers i.e only left is updated because if right pointer values are positive and might not be sumed to zero
                    l+=1
                    ## check for left pointer after increamenting that its previous value is duplicate or not
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                        
        return res           