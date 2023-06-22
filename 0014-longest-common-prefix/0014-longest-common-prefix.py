class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        
        result = ""
        v.sort()
        n = len(v)
        first = v[0]
        last = v[n-1]
        for i in range(min(len(first) , len(last))):
            if(first[i] != last[i]):
                return result
            result+=first[i]
        return result
        