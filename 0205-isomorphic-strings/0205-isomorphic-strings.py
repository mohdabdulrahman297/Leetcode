## time: o(n)
## space : o(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}  # Create two hash maps for character mappings
        
        for i in range(len(s)):  # Iterate through the strings
            c1, c2 = s[i], t[i]  # Get the current characters from s and t
            
            # Check if the current mappings violate isomorphism
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False
            
            # Update the hash maps with the mappings from s to t and t to s
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True  # If all characters are validly mapped, return True
