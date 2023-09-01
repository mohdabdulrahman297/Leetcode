## time:o(n)
## space:o(26)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a hashmap to count occurrences of each character
        count = {}
        maxF = 0  # Initialize max frequency to 0
        l = 0
        
        for r in range(len(s)):
            # Count occurrences of character s[r]
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update max frequency within the window
            maxF = max(maxF, count[s[r]])
            
            # If the length of the window minus the max frequency is greater than k,
            # we need to shrink the window
            if (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
                
        # The result is the length of the valid window
        return r - l+1
