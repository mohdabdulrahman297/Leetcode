## space:o(n)
## time:o(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # create two pointers left and right for the string
        
        l,r = 0 , len(s)-1
        
        ## both pointers should be in bound
        
        while(l<r):
            
            ## check if pointers are in bound(range) and not alphanumeric
            
            while l < r and not self.alphaNum(s[l]):
                
                l+=1
                
            while l < r and not self.alphaNum(s[r]):
                
                r-=1
                
            ## now check if first and last character are equal after converting them into lower case
            if s[l].lower() != s[r].lower():
                return False
            
            ## update the pointers
            l,r = l+1 , r-1
            
        return True    
                
            ## now check if both pointer values    
        
        
        
        
        
        
        
    ## create a function for checking alphnumeric or not
    def alphaNum(self,c):
        
        ## ord method return the ascii value of the character
        
        
        ##check if the value lies between ascii values of uppercase , lowercase , and integers 0 to 9
        return (ord('A') <= ord(c) <= ord('Z')
               or ord ('a') <= ord(c) <= ord('z')
               or ord('0') <= ord(c) <= ord('9'))
    
    
#solution_instance = Solution()
#result = solution_instance.isPalindrome("A man, a plan, a canal: #Panama")
#print(result)  # Should print True
#    
        