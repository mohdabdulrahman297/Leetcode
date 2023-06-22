// Time Complexity is O(N) where n is the size of the target string.
// Space Complexity is O(1)
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i=0 , j=0;
        
        while(i<s.size() && j<t.size()){
            if(s[i] == t[j]){
                i++;
            }
            j++;
        }
        if(i==s.size()){
            return true;
        }
        return false;
        
    }
};

/*
int main()
{
Solution soluiton;
string s = "abc";
string t = "ahbgdc";

bool result = solution.isSubsequence(s,t);

cout << "Is s a subsequence of t? " << (result ? "Yes" : "No") << endl;

return 0;
}
*/