class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        
        unordered_map<long double, int> count;
        
        long double ratio;
        
        long long res = 0;
        
        for(int i = 0; i < rectangles.size(); i++) {  // Fixed typo: changed ".ize()" to ".size()"
            ratio = (long double)(rectangles[i][0]) / (long double)(rectangles[i][1]);
            
            if(count.find(ratio) != count.end()) {
                count[ratio]++;
            }
            else {
                count[ratio] = 1;
            }
        }
        
        for(auto it : count) {
            res += (long long)(it.second) * (long long)(it.second - 1) / 2;
        }
        
        return res;  
    }
};


/*
int main() {
    Solution solution;

    // Define the input rectangles
    vector<vector<int>> rectangles = {{4, 8}, {3, 6}, {10, 20}, {15, 30}};

    // Call the interchangeableRectangles method with the input and print the result
    long long result = solution.interchangeableRectangles(rectangles);
    cout << result << endl;

    return 0;
}
*/