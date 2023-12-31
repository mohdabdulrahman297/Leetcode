class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        //multiply all indexes of nums with -1
        for(int n: nums){
            int i = abs(n) - 1;
            nums[i] = -1*abs(nums[i]);
        }
        
        vector<int> result;
        for(int i=0;i<nums.size();i++){
            if(nums[i] > 0){
                result.push_back(i+1);
            }
        }
        return result;
        
        
    }
};

/*
int main() {
    vector<int> nums = {4, 3, 2, 7, 8, 2, 3, 1};
    Solution solution;
    vector<int> result = solution.findDisappearedNumbers(nums);
    
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
*/