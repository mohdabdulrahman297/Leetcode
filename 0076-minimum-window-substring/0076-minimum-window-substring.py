class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Check if the t string is empty
        if t == "":
            return ""
        
        # Initialize two hashmaps for storing counts of s and t
        countT, window = {}, {}
        
        for c in t:
            # Store character count of t string in hashmap
            countT[c] = 1 + countT.get(c, 0)
        
        # Initialize have and need to compare
        have, need = 0, len(countT)
        
        # Result is left and right pointers, initialize them as -1 in the beginning
        result = [-1, -1]
        
        # Length of the result is set to infinity initially
        resLength = float("infinity")
        
        # Pointers left and right
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # Check if character count is the same in both the hashmaps
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:
                # Update our result
                if (r - l + 1) < resLength:
                    result = [l, r]
                    resLength = (r - l + 1)
                    
                # Popping from the left of the window
                window[s[l]] -= 1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                # Move the left pointer
                l += 1
                
        l, r = result  
        if resLength != float("infinity"):
            return s[l : r + 1]
        else:
            return ""
