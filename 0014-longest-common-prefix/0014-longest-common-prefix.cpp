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






