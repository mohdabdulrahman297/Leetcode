class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> res;
        
        sort(nums.begin() , nums.end());
        
        for(int i=0;i<nums.size();i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            
            int a = nums[i];
            int l = i+1;
            int r = nums.size()-1;
            
            while(l<r){
                int threeSum = a + nums[l] + nums[r];
                
                if(threeSum > 0){
                    r--;
                }
                else if(threeSum < 0){
                    l++;
                }
                else{
                    res.push_back({a, nums[l], nums[r]});
                    l++;
                    while(l<r && nums[l] == nums[l-1]){
                        l++;
                    }
                }
            }
        }
        return res;
            
            
        
    }
};

/*
int main() {
    Solution solution;

    std::vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
    std::vector<std::vector<int>> result1 = solution.threeSum(nums1);
    for (const auto& triplet : result1) {
        for (int num : triplet) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
*/