##Time: O(n x l) -> n = length of strs, l = max length of a string in strs
##Space: O(n x l)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    
##solution = Solution()
##strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

##result = solution.groupAnagrams(strs)

# Print the grouped anagrams
##for group in result:
##    print(group)
    
            
        