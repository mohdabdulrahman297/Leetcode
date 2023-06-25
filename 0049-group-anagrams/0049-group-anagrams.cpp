class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // creating a hashmap to store the string as a key and those set of strings as values which has same character count as the key
        
        //ex: key : value
        //    1e ,1a, at : [eat , tea , ate]
        
        unordered_map<string , vector<string>> m;
// iterate over the list of strings and calculate the count of characters in a string 
        for(int i=0;i<strs.size();i++){
            string key  = getKey(strs[i]);
            m[key].push_back(strs[i]);
        }
        
        // create the output 
        vector<vector<string>> result;
        for(auto it=m.begin() ; it !=m.end() ; it++){
            result.push_back(it -> second);
        }
        return result;
    }
    
private:
    string getKey(string str){
        //create a vector matrix named count of 26 smallcase alphabets intialized as 0's
        vector<int> count(26);
        for(int j=0;j<str.size();j++){
            count[str[j] - 'a']++;
        }
        
        string key = "";
            for(int i=0;i<26;i++){
                key.append(to_string(count[i] + 'a'));
            }
        return key;
    }
    
    
};

/*
int main()
{
Solution solution;
vector<string> strs = ["eat","tea","tan","ate","nat","bat"];

vector<vector<string>> result = solution.groupAnagrams(strs);

for(const auto&group : result){
for(const string&str : group){
cout<<str<<" ";
}
cout<<endl;
}
return 0;
}
*/