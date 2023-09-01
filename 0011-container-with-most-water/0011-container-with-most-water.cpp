class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        
        int curr = 0;
        int result = 0;
        
        while (l < r) {
            curr = (r - l) * min(height[l], height[r]);
            result = max(result, curr);
            
            if (height[l] <= height[r]) {
                l++;
            } else {
                r--;
            }
        }
        
        return result;
    }
};

/*
int main() {
    Solution solution;

    vector<int> heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};

    int result = solution.maxArea(heights);

    cout << "Maximum area: " << result << endl;

    return 0;
}
*/
