# space: o(1)
# time: o(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ##left pointer indicates stock buy and right indicates stock sell(basic rule for profit)
        l,r = 0 , 1
        
        maxProfit = 0
        
        ##because the left will be at the minimum and the right is going to shift
        while(r < len(prices)):
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                
                maxProfit = max(maxProfit , profit)
            else:
                ## l=r because if at any instance l is increamented and it reahces a value greater than right then theres no profit
                
                l=r
            r+=1    
            
        return maxProfit   
    
    
    
# Create an instance of the Solution class
##solution = Solution()

# Define an input list of stock prices
##prices = [7, 1, 5, 3, 6, 4]

# Call the maxProfit function with the input list
##result = solution.maxProfit(prices)

# Print the result
#print("Maximum profit:", result)##    
        