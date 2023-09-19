class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        vector<int> res(temperatures.size(), 0);
        
        stack<pair<int, int>> st;
        
        for(int i=0;i<temperatures.size();i++){
            
            int t = temperatures[i];
            
            while(!st.empty() && t > st.top().first){
                
                int stackTop = st.top().first;
                int stackIndex = st.top().second;
                
                st.pop();
                
                res[stackIndex] = i - stackIndex;
            }
            
            st.push({t, i});
        }
        return res;
    }
};

/*
int main() {
    Solution solution;
    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73}; // You can change this list to test with different temperatures
    vector<int> result = solution.dailyTemperatures(temperatures);

    // Print the result, which contains the number of days to wait for a warmer temperature
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
*/