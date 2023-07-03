#include <vector>

using namespace std;

class NumArray {
private:
    vector<int> prefix;

public:
    NumArray(vector<int>& nums) {
        prefix.resize(nums.size());
        int total = 0;
        for (int i = 0; i < nums.size(); i++) {
            total += nums[i];
            prefix[i] = total;
        }
    }

    int sumRange(int left, int right) {
        int rightSum = prefix[right];
        int leftSum = 0;

        if (left > 0) {
            leftSum = prefix[left - 1];
        }

        return rightSum - leftSum;
    }
};
/*
int main() {
    vector<int> nums = {-2, 0, 3, -5, 2, -1};
    NumArray obj(nums);

    // Example usage
    int sum1 = obj.sumRange(0, 2);
    cout << sum1 << endl;  // Output: 1

    int sum2 = obj.sumRange(2, 5);
    cout << sum2 << endl;  // Output: -1

    int sum3 = obj.sumRange(0, 5);
    cout << sum3 << endl;  // Output: -3

    return 0;
}
*/
