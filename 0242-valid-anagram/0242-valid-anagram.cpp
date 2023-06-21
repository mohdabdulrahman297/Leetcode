// time:o(s+t)
// space:o(s+t)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        
        unordered_map<char,int> smap;
        unordered_map<char,int> tmap;
        
        for(int i=0;i<t.size();i++){
            smap[s[i]]++;
            tmap[t[i]]++;
            
            }
        return smap == tmap;
        
        
    }
};

/*
int main() {
    string input1, input2;
    cout << "Enter the first string: ";
    getline(cin, input1);
    cout << "Enter the second string: ";
    getline(cin, input2);

    Solution solution;
    bool result = solution.isAnagram(input1, input2);

    cout << "Are the strings anagrams? " << (result ? "Yes" : "No") << endl;

    return 0;
}
*/