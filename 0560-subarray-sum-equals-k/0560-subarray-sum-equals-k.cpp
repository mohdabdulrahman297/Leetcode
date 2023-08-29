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