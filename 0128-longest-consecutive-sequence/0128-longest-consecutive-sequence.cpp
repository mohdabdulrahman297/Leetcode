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