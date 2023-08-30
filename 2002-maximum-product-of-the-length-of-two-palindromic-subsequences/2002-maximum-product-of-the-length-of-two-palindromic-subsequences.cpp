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