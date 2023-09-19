class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
        vector<string> res;
        
        string current;
        backtrack(res, current, 0, 0, n);
        return res;
    }
    
private:
    void backtrack(vector<string> &res, string current, int openCount, int closeCount, int n){
        if(openCount == closeCount && openCount == n){
            res.push_back(current);
            return;
        }
        
        if(openCount < n){
            current += "(";
            backtrack(res, current, openCount + 1, closeCount, n);
            current.pop_back();
        }
        
        if(closeCount < openCount){
            current += ")";
            backtrack(res, current, openCount, closeCount + 1, n);
            current.pop_back();
        }
    }
};

/*
int main() {
    Solution solution;
    int n = 3; // You can change this value to test with different n
    vector<string> result = solution.generateParenthesis(n);

    // Print the generated parenthesis combinations
    for (const string& combination : result) {
        cout << combination << endl;
    }

    return 0;
}
*/