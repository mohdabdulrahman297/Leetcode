// time:o(n)
// space:o(n)
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        unordered_set<int> NumSet(nums.begin() , nums.end());
        int longest = 0;
            
        for(int n : nums){
            if(NumSet.find(n-1) == NumSet.end()){
                int length = 0;
                    
                while(NumSet.find(n+length) != NumSet.end()){
                    length++;
                }    
                longest = max(length , longest);
            }
        } 
        return longest;
        
    }
};

/*
int main() {
    // Example input
    std::vector<int> nums = {100, 4, 200, 1, 3, 2};

    Solution solution;
    int result = solution.longestConsecutive(nums);
    std::cout << "Input: ";
    for (int num : nums) {
        std::cout << num << " ";
    }
    std::cout << "\nLongest Consecutive Length: " << result << std::endl;
    
    return 0;
}
*/