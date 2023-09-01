## time:o(n)
## space:o(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ##create two pointers
        
        l , r = 0, len(numbers)-1
        
        while(l<r):
            
            # calculate the current sum at pointers
            curSum = numbers[l] + numbers[r]
            
            ## if sum is greater than target decreament right pointer because the array is in sorted order
            if(curSum > target):
                r-=1
                
            ## if sum is less than target decreament left pointer because the array is in sorted order    
            elif(curSum < target):
                l+=1
                
            else:
                return [l+1 , r+1]
            
        return []   
        