## time: o(2^n)
## space: o(2^n)
class Solution:
    def maxProduct(self, s: str) -> int:
        
        n = len(s);
        
        ##create a hashmap as follows
        
        pali = {} # bitmask of sub pailndrome : length of that palindrome
        
        for mask in range(1 , 1<<n): # 1<<n == 1<<2**n
            
            ## create an empyty string to convert back the bitmask
            subseq = ""
            for i in range(n):
                
                ## the above line inidcates that and operation gives 1 
                if(mask & (1<<i)):
                    subseq += s[i];
            ## check if the subsequnce string is palindrome        
            if subseq == subseq[::-1]:
                ##then assing the key and value in hashmap
                pali[mask] = len(subseq)
                
                
        res = 0
        
        for m1 in pali:
            for m2 in pali:
                if(m1 & m2) == 0: #disjoint
                    res = max(res , pali[m1] * pali[m2])
        return res         
                
        
# Create an instance of the Solution class
#solution = Solution()

# Define the input string
#input_string = "ababbb"

# Call the maxProduct method with the input and print the result
#result = solution.maxProduct(input_string)
#print(result)#        