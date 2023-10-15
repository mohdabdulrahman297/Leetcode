## space: o(1)
## time: o(nlogm)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the pointers
        l, r = 1, max(piles)
        # Let the result be max in the beginning
        res = r
        # Apply binary search
        while l <= r:
            # Calculate the mid
            k = (l + r) // 2
            # Initialize hours to zero
            hours = 0
            # Iterate through the array
            for p in piles:
                # Calculate the hours and round off using math.ceil function
                hours += math.ceil(float(p) / k)
            if hours <= h:
                # Update the result and check if there exists another min value than the previous one
                res = k
                r = k - 1
            else:
                l = k + 1
        # Return the result
        return res
    
    
# Import the required libraries
#import math

# Define the input data
#piles = [3, 6, 7, 11]
#h = 8

# Create an instance of the Solution class
#solution = Solution()

# Call the minEatingSpeed function
#result = solution.minEatingSpeed(piles, h)

# Print the result
#print("Minimum Eating Speed:", result)
    
