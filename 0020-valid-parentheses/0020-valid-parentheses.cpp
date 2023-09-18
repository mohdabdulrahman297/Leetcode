class Solution {
public:
    bool isValid(string s) {
        
        stack<char> stack;
        
        unordered_map<char,char> closeToOpen = {{')', '('}, {']', '['}, {'}', '{'}};
        
        for(char c : s){
            if(closeToOpen.find(c) != closeToOpen.end()){
                if(!stack.empty() && stack.top() == closeToOpen[c]){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(c);
            }
        }
        return stack.empty();
        
    }
};

/*
int main() {
    Solution solution;

    // Test cases
    std::string input_str1 = "()";
    std::string input_str2 = "({[()]})";

    // Check if the input strings have valid brackets
    std::cout << std::boolalpha;  // Print "true" or "false" instead of 1 or 0
    std::cout << solution.isValid(input_str1) << std::endl;  // Should print true
    std::cout << solution.isValid(input_str2) << std::endl;  // Should print true

    return 0;
}
*/