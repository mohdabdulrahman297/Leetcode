class Solution {
public:
    int countPalindromicSubsequence(string s) {
        
        int count = 0;
        
        unordered_set<char> chars;
        
        for(char c : s){
            chars.insert(c);
        }
        
        for(char c : chars){
            size_t first = s.find(c);
            size_t last = s.rfind(c);
            
            if(last > first+1){
                
                unordered_set<char> uniqueChars(s.begin() + first+1 , s.begin() + last);
                
                count += uniqueChars.size();
            }
        }
        
        return count;
        
    }
};