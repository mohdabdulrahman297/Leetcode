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

/*
int main() {
    // Example input
    std::vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;

    // Create an instance of the Solution class
    Solution solution;

    // Call the topKFrequent method to find the top k frequent elements
    std::vector<int> top_k_frequent = solution.topKFrequent(nums, k);

    // Print the result
    for (int num : top_k_frequent) {
        std::cout << num << " ";
    }

    return 0;
}
*/