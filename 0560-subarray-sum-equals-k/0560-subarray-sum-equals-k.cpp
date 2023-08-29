class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
        int count =0;
        int sum = 0;
        
        unordered_map<int , int> dic;
        
        dic[0] = 1;
        
        for(int i=0;i<nums.size();i++){
            sum = sum+nums[i];
            
            if(dic.find(sum - k) != dic.end()){
                count = count + dic[sum-k];
            }
            dic[sum]++;
        }
        return count;
    }
};

/*
int main() {
    Solution solution;
    
    // Input array and k value
    vector<int> nums = {1, 2, 3};
    int k = 3;
    
    // Call the subarraySum function and print the result
    int result = solution.subarraySum(nums, k);
    cout << result << endl;
    
    return 0;
}
*/