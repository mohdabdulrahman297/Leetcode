// time: o(n+m)
// space: o(n+m)
class Solution {
public:
    bool wordPattern(string pattern, string s) {
         // This creates a stringstream object named str using the input string s. This object is used to extract words from the string.
         stringstream str(s);
         //  This declares a string variable named word which will be used to store individual words extracted from the stringstream.
         string word ; 
         // This initializes an empty vector named words. This vector will store the individual words extracted from the input string s.
         vector<string> words;
        
        
         while(str >> word){
             words.push_back(word);
         }
        
        if(pattern.size() != words.size()){
            return false;
        }
        
        unordered_map<char , string> CharToWord;
        unordered_map<string , char> WordToChar;
        
        for(int i=0;i<pattern.size();i++){
            char c = pattern[i];
            string w = words[i];
            
            if(CharToWord.find(c) == CharToWord.end() && WordToChar.find(w) == WordToChar.end()){
                
                CharToWord[c] = w;
                WordToChar[w] = c;
            }
            else if(CharToWord[c] != w && WordToChar[w] != c){
                return false;
            }
    
            
        }
        return true;
        
        
             
            
    }
};


/*
int main() {
    Solution solution;
    std::cout << solution.wordPattern("abba", "dog cat cat dog") << std::endl;  // Output: 1 (true)
    std::cout << solution.wordPattern("abba", "dog cat cat fish") << std::endl; // Output: 0 (false)
    
    return 0;
}
*/