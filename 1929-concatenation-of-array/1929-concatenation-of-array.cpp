//time:o(n)
//space:o(n)
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        vector<int> ans;
        
        int len = nums.size();
        for(int i=0;i<2*len;i++){
            ans.push_back(nums[i%len]);
        }
        return ans;
        
    }
};

/*
int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5};
    vector<int> result = solution.getConcatenation(nums);
    
    // Print the concatenated list
    for (int num : result) {
        cout << num << " ";
    }
    
    return 0;
}
*/