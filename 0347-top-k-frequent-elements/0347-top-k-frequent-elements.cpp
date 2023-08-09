class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## create a hashmap to map count of occurences
        count = {}
        ## create a empty array named frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        ## count occurences of elements in input array and append it into the newly created array
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n , c in count.items():
            freq[c].append(n)
            
            
            
        result = []
        ## looping  in reverse order(-1 indicates reverse looping)
        for i in range(len(freq)-1 , 0 , -1):
            for n in freq[i]:
                result.append(n)
                if(len(result) == k):
                    return result
   # Example input
#nums = [1, 1, 1, 2, 2, 3]
#k = 2

# Create an instance of the Solution class
#solution = Solution()

# Call the topKFrequent method to find the top k frequent elements
#top_k_frequent = solution.topKFrequent(nums, k)

# Print the result
#print(top_k_frequent)