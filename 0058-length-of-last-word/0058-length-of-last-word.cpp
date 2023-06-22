/*
    Approach: 
    Traverse from end to the first whitespace character and count the number of letters.
    Return the count as our pointer hits the whitespace character.
    
    Time complexity: O(n)
    Space complexity: O(1)
    */    
class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int n=s.length();
        
        int i = n-1;
        int len = 0;
        
        while(s[i] == ' '){
            i--;
            
        }
        while(i>=0 && s[i] !=' '){
            len++;
            i--;
        }
        
        return len;
        
    }
};

/*
int main() {
    Solution solution;
    string s = "Hello World";

    int result = solution.lengthOfLastWord(s);

    cout << "Length of the last word: " << result << endl;

    return 0;
}
*/
