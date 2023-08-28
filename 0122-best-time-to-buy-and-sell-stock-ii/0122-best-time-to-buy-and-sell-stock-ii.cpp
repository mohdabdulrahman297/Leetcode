// space: o(1)
// time : o(n)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int profit = 0;
        
        for(int i=1;i<prices.size();i++){
            if(prices[i] > prices[i-1]){
                profit += prices[i] - prices[i-1];
            }
            
        }
        return profit;
        
    }
};

/*

int main() {
    Solution solution;
    
    // Create a vector representing stock prices
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    
    // Call the maxProfit function to calculate the maximum profit
    int result = solution.maxProfit(prices);
    
    // Print the result
    cout << "Maximum profit: " << result << endl;
    
    return 0;
}
*/