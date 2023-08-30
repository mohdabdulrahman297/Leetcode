class Solution {
public:
    int minSwaps(string s) {
        
        int extraClose = 0;
        int maxClose = 0;
        
        for(char c : s){
            if(c == '['){
                extraClose--;
                
            }
            else{
                extraClose++;
            }
            
            maxClose = max(extraClose , maxClose);
                
        }
        return (maxClose + 1)/2;
        
    }
};

/*

int main() {
    Solution solution;
    std::string input_string = "[]][[]";
    int result = solution.minSwaps(input_string);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
*/