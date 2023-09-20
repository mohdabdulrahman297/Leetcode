// space:o(n)
// time:o(n)

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // pair: [index, height]
        stack<pair<int, int>> stk;
        int result = 0;
        
        for (int i = 0; i < heights.size(); i++) {
            int start = i;
            
            while (!stk.empty() && stk.top().second > heights[i]) {
                int index = stk.top().first;
                int width = i - index;
                int height = stk.top().second;
                stk.pop();
                
                result = max(result, height * width);
                start = index;
            }
            
            stk.push({start, heights[i]});
        }
        
        while (!stk.empty()) {
            int width = heights.size() - stk.top().first;
            int height = stk.top().second;
            stk.pop();
            
            result = max(result, height * width);
        }
                          
        return result;
    }
};

/*
int main() {
    Solution solution;

    // Define the input values (list of heights)
    vector<int> heights = {2, 1, 5, 6, 2, 3};  // Example input

    // Call the largestRectangleArea function with the provided input
    int result = solution.largestRectangleArea(heights);

    // Print the result
    cout << "Largest rectangle area: " << result << endl;

    return 0;
}
*/