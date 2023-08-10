// space : o(n)
// time : o(n)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> res(nums.size() , -1);
        
        int prefix = 1;
        for(int i=0;i<nums.size();i++){
            res[i] = prefix;
            prefix = prefix* nums[i];
        }
        
        int postfix = 1;
        for(int i = nums.size()-1; i>=0 ; --i){
            res[i] = res[i]*postfix;
            postfix = postfix* nums[i];
       }
    return res;
        
    }    
};

/*
int main() {
    std::vector<int> nums = {1, 2, 3, 4};
    Solution solution;
    std::vector<int> result = solution.productExceptSelf(nums);
    
    for (int num : result) {
        std::cout << num << " ";
    }
    // Output: 24 12 8 6
    
    return 0;
}
*/