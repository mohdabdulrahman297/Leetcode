## time:o(n)
## space: o(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a hashset to avoid duplicates
        charSet = set()
        
        # Initialize the result variable
        res = 0
        
        # Initialize the left pointer
        l = 0
        
        # Iterate through every character (right pointer)
        for r in range(len(s)):
            # Check if the character is already in the set
            while s[r] in charSet:
                # Remove the leftmost character from the set
                charSet.remove(s[l])
                # Increment the left pointer
                l += 1
                
            # Add the current character to the set
            charSet.add(s[r])
            
            # Update the result with the maximum length
            res = max(res, r - l + 1)
                
        return res
