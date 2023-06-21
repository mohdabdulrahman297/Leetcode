## time:o(s+t)
## space:o(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        