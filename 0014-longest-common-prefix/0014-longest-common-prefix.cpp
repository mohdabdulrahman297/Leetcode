//time:o(n*mlog(n))
//space:o(m)
// where n is no of strings and m is length of strings
class Solution {
public:
    string longestCommonPrefix(vector<string>& v) {
        
        string result = "";
        sort(v.begin(),v.end());
        
        int size = v.size();
        
        string first = v[0];
        string last =  v[size-1];
        
        for(int i=0;i<min(first.size() , last.size());i++){
            if(first[i] != last[i]){
                return result;
            }
            result+=first[i];
            
        }
        return result;
        
        
    }
};

/*
int main() {
    vector<string> v = {"flower", "flow", "flight"};
    Solution s;
    string longestPrefix = s.longestCommonPrefix(v);
    cout << "Longest common prefix: " << longestPrefix << endl;
    return 0;
}
*/






