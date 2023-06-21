## time:o(s+t)
## space:o(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False;
        
        mapS={}
        mapT={}
        
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i],0)
            mapT[t[i]] = 1 + mapT.get(t[i],0)
            
        return mapS == mapT 
    
    
# Get user input for s and t
##s = input("Enter the first string: ")
##t = input("Enter the second string: ")

##solution = Solution()
##print(solution.isAnagram(s, t))    
        