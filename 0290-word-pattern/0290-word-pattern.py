## time: o(n+m)
## space: o(n+m)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        ## split the string based on spaces
        words = s.split(" ")
        if(len(pattern) != len(words)):
            return False
        
        ## use two hashmaps to map character to word and word to character to avoid overlapping
        CharToWord = {}
        WordToChar = {}
        
        ## if pattern and words are of same length iterate through them at once
        for c , w in zip(pattern , words):
            if c in CharToWord and CharToWord[c] != w:
                return False
            if w in WordToChar and WordToChar[w] != c:
                return False
            
            ## now simple map
            CharToWord[c] = w
            WordToChar[w] = c
            
        ## now we have iterated through the loop 
        return True
        