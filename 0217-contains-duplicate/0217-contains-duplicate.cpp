// brute force
//time complexity = o(nlogn)
//space complexity = o(1)

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
        
    }
};

/*
int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> nums(n);
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    Solution solution;
    bool containsDup = solution.containsDuplicate(nums);

    if (containsDup) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
*/
