## space: o(1)
## time : o(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        
        ## interate from the first value in arrays beacuse we have to compare the previous value for the current ith , hence 0th value dosen't have any  previous value , start the iteration from 1st place
        for i in range(1 , len(prices)):
            ## the above conditional statement inidicates profit
            if(prices[i] > prices[i-1]):
                profit += (prices[i] - prices[i-1])
                
        return profit        
        
        
# Test the maxProfit function
#solution = Solution()

# Create a list representing the stock prices
#prices = [7, 1, 5, 3, 6, 4]

# Call the maxProfit function to calculate the maximum profit
#result = solution.maxProfit(prices)

# Print the result
#print("Maximum profit:", result)#        