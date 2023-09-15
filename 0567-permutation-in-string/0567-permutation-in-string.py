##time : o(n)
##space : o(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        ##initialize two hahsmaps for both the strings with 26 numbers set to '0'
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for i in range(len(s1)):
            ##get the ascii value
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            if(s1Count[i] == s2Count[i]):
                matches += 1
            else:
                matches += 0
                
        ##initialize left and right pointer for the sliding window
        
        l = 0
        for r in range(len(s1), len(s2)):
            
            if(matches == 26):
                return True
            
            ##get the index from the hashmaps for the right pointer
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            
            ##check if the count for the characters are equal , if equal increament else decreament
            
            if s1Count[index] == s2Count[index]:
                matches += 1
                
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
                
            ##get the index from the hashmaps for the left pointer
            
            index = ord(s2[l]) - ord('a')
            
            s2Count[index] -= 1
            
            if s1Count[index] == s2Count[index]:
                matches += 1
                
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
                
            l += 1
            
        return matches == 26    
            
        
        
# Create an instance of the Solution class
##solution = Solution()

# Test cases
##s1 = "ab"
##s2 = "eidbaooo"
##result = solution.checkInclusion(s1, s2)
##print(f"Is '{s1}' a permutation of a substring of '{s2}'? ##{result}")  # Should print True##        