## time: o(n^2)
## space:o(n)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        ## initialize count variable for counting unique characters in input
        count = 0
        
        ## use set() for extracting unique characters from the  input string
        
        chars = set(s)
        
        ## iterate
        for char in chars:
            
            
            # s.find(char) gets the index of first occurence of character and s.rfind(char) gets the index in reverse order i.e last 
            
            #For 'a', first would be 0 and last would be 3.
            #For 'b', first would be 1 and last would be 1.
            #For 'c', first would be 2 and last would be 2.
            first = s.find(char)
            last  = s.rfind(char)
            
            count += len(set(s[first+1:last]))
            
            
        return count     
    
    
# Example usage
#if __name__ == "__main__":
    #solution = Solution()
    #input_string = "aabca"
    #result = solution.countPalindromicSubsequence(input_string)
    #print("Result:", result)  
                         
                         
        