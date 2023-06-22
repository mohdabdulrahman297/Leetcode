class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #initial max = -1
        #reverse iteration
        #new max = max(old max , arr[i])
        
        rightmax = -1
        
        for i in range(len(arr)-1 , -1 ,-1):
            newmax = max(rightmax,arr[i])
            arr[i] = rightmax
            rightmax = newmax
            
        return arr    
    
    
#solution = Solution()

#arr = [8,5,4,5,1]

#result = solution.replaceElements(arr)

#print(result)

        
        
        