// space:o(1)
// time:o(n)
class Solution {
public:
    int trap(vector<int>& height) {
        
        if(height.empty()){
            return 0;
        }
        
        int l =0;
        int r = height.size() -1;
        int leftMax = height[l];
        int rightMax = height[r];
        
        int res = 0;
        
        while(l<r){
            if(leftMax < rightMax){
                l++;
                leftMax = max(leftMax , height[l]);
                res += leftMax -height[l];
            }
            else{
                r--;
                rightMax = max(rightMax, height[r]);
                res += rightMax - height[r];
            }
        }
        return res;
        
    }
};

/*
int main() {
    Solution solution;

    vector<int> heights = {0,1,0,2,1,0,1,3,2,1,2,1};

    int result = solution.trap(heights);

    cout << "Trapped water units: " << result << endl;

    return 0;
}
*/