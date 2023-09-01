class Solution {
public:
    bool isPalindrome(string s) {
        
        int l = 0;
        int r = s.length()-1;
        
        while(l < r){
            while(l < r && !alphaNum(s[l])){
                l++;
            }
            while(l < r && !alphaNum(s[r])){
                r--;
            }
            
            if(tolower(s[l]) != tolower(s[r])){
                return false;
            }
            
            l++;
            r--;
        }
        return true;
        
    }
    
private:
    bool alphaNum(char c){
        return (isalpha(c) || isdigit(c));
    }
};

/*
int main() {
    Solution solution;

    std::string input1 = "A man, a plan, a canal: Panama";
    bool result1 = solution.isPalindrome(input1);
    std::cout << "Is \"" << input1 << "\" a palindrome? " << std::boolalpha << result1 << std::endl;

    std::string input2 = "race a car";
    bool result2 = solution.isPalindrome(input2);
    std::cout << "Is \"" << input2 << "\" a palindrome? " << std::boolalpha << result2 << std::endl;

    return 0;
}
*/