#time : o(n)
#space : o(n)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        ## add zeros in the first and last of the list or vector
        
        f = [0] + flowerbed + [0]
        
        #skip first and last element in the range beacuse we have already added zeros 
        for i in range(1, len(f)-1):
            if(f[i-1] == 0 and f[i] == 0 and f[i+1] == 0):
                f[i] = 1
                n-=1
             
        if(n<=0):
            return True
        return False
 # Create an instance of the Solution class
##solution = Solution()

# Test case 1
##flowerbed1 = [1, 0, 0, 0, 1]
##n1 = 1
#print(solution.canPlaceFlowers(flowerbed1, n1))  # Output: True

# Test case 2
##flowerbed2 = [1, 0, 0, 0, 1]
##n2 = 2
#print(solution.canPlaceFlowers(flowerbed2, n2))  # Output: False

# Test case 3
##flowerbed3 = [0, 0, 1, 0, 1]
##n3 = 1
##print(solution.canPlaceFlowers(flowerbed3, n3))  # Output: True
   
    
        