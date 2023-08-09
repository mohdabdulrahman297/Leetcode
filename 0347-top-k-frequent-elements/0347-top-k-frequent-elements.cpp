// space:o(n)
// time:o(n)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int , int> count;
        vector<vector<int>> freq(nums.size()+1);
        
        for(int n : nums){
            count[n]++;
        }
        
        for(auto it : count){
            int num = it.first;
            int frequency = it.second;
            freq[frequency].push_back(num);
        }
        
        vector<int> result;
        
        for(int i = freq.size()-1 ;  i > 0 ; i--){
            for(int n : freq[i]){
                result.push_back(n);
                if(result.size() == k){
                    return result;
                }
            }
        }
        return result;
        
    }
};