class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_set<char> charSet;
        
        int l = 0;
        
        int res = 0;
        
        for(int r=0; r<s.length();r++){
            while(charSet.find(s[r]) != charSet.end()){
                charSet.erase(s[l]);
                l++;
            }
            
            charSet.insert(s[r]);
            res = max(res , r-l+1);
        }
        return res;
        
    }
};

/*
int main() {
    Solution solution;

    string input_str = "abcabcbb";

    int result = solution.lengthOfLongestSubstring(input_str);

    cout << "Length of the longest substring without repeating characters: " << result << endl;

    return 0;
}
*/