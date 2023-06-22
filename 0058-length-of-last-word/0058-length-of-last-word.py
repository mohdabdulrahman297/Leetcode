
    ##Approach: 
    ##Traverse from end to the first whitespace character and count ##the number of letters.
    ##Return the count as our pointer hits the whitespace character.
    
    ##Time complexity: O(n)
    ##Space complexity: O(1)  
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s) - 1
        length = 0
        
        while(s[i] == " "):
            i-=1
        while(i>=0 and s[i] != " "):
            length+=1
            i-=1
        return length    
    
    
#solution  = Solution()
#s="hello world"

#result = solution.lenghtOfLastWord(s)
#print(result)