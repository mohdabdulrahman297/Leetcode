class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        int i = 0;

        while (i <= r) {
            if (nums[i] == 0) {
                swap(nums[l], nums[i]);
                l++;
                i++;
            } else if (nums[i] == 2) {
                swap(nums[i], nums[r]);
                r--;
            } else {
                i++;
            }
        }
    }
};

/*
int main() {
    // Example input
    std::vector<int> nums = {2, 0, 2, 1, 1, 0};

    Solution solution;
    solution.sortColors(nums);

    std::cout << "Sorted Colors: ";
    for (int num : nums) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
*/
