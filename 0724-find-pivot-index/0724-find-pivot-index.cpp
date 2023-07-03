class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int total =0;
        for(int i : nums){
            total += i;
        }
        
        int leftsum = 0;
        for(int i=0;i<nums.size();i++){
            int rightsum = total - nums[i] - leftsum;
            if(leftsum == rightsum){
                return i;
                
            }
            leftsum += nums[i];
        }
        return -1;
    }
};

/*
int main() {
    Solution solution;

    // Example 1
    vector<int> nums = {1, 7, 3, 6, 5, 6};
    int output = solution.pivotIndex(nums);
    cout << output << endl;  // Output: 3

    // Example 2
    nums = {1, 2, 3};
    output = solution.pivotIndex(nums);
    cout << output << endl;  // Output: -1

    // Custom Test Case
    nums = {1, 2, 3, 4, 0, 6};
    output = solution.pivotIndex(nums);
    cout << output << endl;  // Output: 3

    return 0;
}
*/
