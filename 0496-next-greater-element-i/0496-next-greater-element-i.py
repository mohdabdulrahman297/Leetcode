#time: o(n+m)
#space: o(n+m)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Creating a map nums1Idx and mapping values to their indices
        nums1Idx = {}
        for i, n in enumerate(nums1):
            nums1Idx[n] = i

        # Create a result vector of size nums1 to store the output
        res = [-1] * len(nums1)
        
        # Create an empty stack
        stack = []
        
        for i in range(len(nums2)):
            curr = nums2[i]
            
            # Check if stack is not empty and curr is greater than the top element of the stack
            while stack and curr > stack[-1]:
                val = stack.pop()
                
                # Find the index of the value through the map
                idx = nums1Idx[val]
                
                # Store the next greater element, i.e., curr, at the index correlated to nums1
                res[idx] = curr
            
            # Check if curr (next greater element) exists in nums1 and add it to the stack
            if curr in nums1:
                stack.append(curr)
        
        return res
#solution = Solution()

# Example 1
#nums1 = [4, 1, 2]
#nums2 = [1, 3, 4, 2]
#output = solution.nextGreaterElement(nums1, nums2)
#print(output)  # Output: [-1, 3, -1]
