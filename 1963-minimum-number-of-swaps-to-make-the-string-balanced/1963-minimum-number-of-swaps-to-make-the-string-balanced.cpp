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