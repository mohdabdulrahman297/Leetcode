class Solution {
public:
    int maxProduct(string s) {
        
        int n = s.size();
        
        unordered_map<int , int> pali;
        
        for(int mask = 1; mask < (1 << n) ; mask++){
            string subseq = "";
            
            for(int i=0;i<n;i++){
                if(mask & (1<<i)){
                    subseq += s[i];
                }
            }
            if(subseq == string(subseq.rbegin() , subseq.rend())){
                pali[mask] = subseq.size();
            }
        }
        
        int res = 0;
        for(auto m1 : pali){
            for(auto m2 : pali){
                if((m1.first & m2.first) == 0){
                    res = max(res , m1.second * m2.second);
                }
            }
        }
        return res;
    }
};


/*
int main() {
    Solution solution;

    // Define the input string
    string input_string = "ababbb";

    // Call the maxProduct method with the input and print the result
    int result = solution.maxProduct(input_string);
    cout << result << endl;

    return 0;
}
*/