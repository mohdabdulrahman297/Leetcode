class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int count = 0;
        int result = 0;
            
        for(int i : nums){
            if(count == 0 ){
                result = i;
            }
            count += (i == result) ? 1 : -1;
        }
        return result;
    }
};

/*
int main() {
    Solution solution;

    // Test case 1
    vector<int> nums1 = {1, 2, 2, 2, 3};
    cout << solution.majorityElement(nums1) << endl;  // Output: 2

    // Test case 2
    vector<int> nums2 = {3, 3, 4, 2, 4, 4, 2, 4, 4};
    cout << solution.majorityElement(nums2) << endl;  // Output: 4

    // Test case 3
    vector<int> nums3 = {1, 1, 1, 2, 3, 4};
    cout << solution.majorityElement(nums3) << endl;  // Output: 1

    return 0;
}
*/