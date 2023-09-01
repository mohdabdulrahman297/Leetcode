class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int l = 0;
        int r = 1;
        
        int maxProfit = 0;
        
        while( r < prices.size()){
            if(prices[l] < prices[r]){
                int profit = prices[r] - prices[l];
                maxProfit = max(maxProfit , profit);
            }
            else{
                l=r;
            }
            r+=1;
        }
        return maxProfit;
        
    }
};

/*
int main() {
    Solution solution;

    vector<int> prices = {7, 1, 5, 3, 6, 4};

    int result = solution.maxProfit(prices);

    cout << "Maximum profit: " << result << endl;

    return 0;
}
*/