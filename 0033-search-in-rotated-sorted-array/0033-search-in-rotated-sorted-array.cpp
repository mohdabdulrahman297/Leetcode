// space: o(1)
// time: o(logn)
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        
        while(l <= r){
            int m = l + (r-l)/2;
            if(target == nums[m]){
                return m;
            }
            
            if(nums[l] <= nums[m]){
                if(target > nums[m] || target < nums[l]){
                    l = m+1;
                }
                else{
                    r = m-1;
                }
            }
            else{
                if(target < nums[m] || target > nums[r]){
                    r = m-1;
                }
                else{
                    l = m+1;
                }
            }
        }
        return -1;
    }
};

/*
int main() {
    Solution sol;

    std::vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target1 = 0;
    int target2 = 3;

    int result1 = sol.search(nums, target1);
    int result2 = sol.search(nums, target2);

    // Print the results
    printf("Result for target1 (%d): %d\n", target1, result1);
    printf("Result for target2 (%d): %d\n", target2, result2);

    return 0;
}
*/