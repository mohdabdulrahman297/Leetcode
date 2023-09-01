class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int maxF = 0;
        int l = 0;
        int r; // Define r here
        
        for (r = 0; r < s.length(); r++) {
            count[s[r]]++;
            maxF = max(maxF, count[s[r]]);
            
            if (r - l + 1 - maxF > k) {
                count[s[l]]--;
                l++;
            }
        }
        
        return r - l; // Corrected to r - l instead of r - l + 1
    }
};
