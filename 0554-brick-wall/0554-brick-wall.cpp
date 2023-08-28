//Time complexity : O(n x m)
//Space complexity: O(n x m)

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        
        unordered_map<int , int> countGap;
        
        int rows = wall.size();
        int cols;
        int maxGap = 0;
        
        for(int i=0;i<rows;i++){
            int total = 0;
            
            // '-1' because edge of the wall is not considered
            cols = wall[i].size() - 1;
            
            for(int j=0;j<cols;j++){
                total += wall[i][j];
                
                if(countGap.find(total) != countGap.end()){
                    countGap[total]++;
                }
                else{
                    countGap[total] = 1;
                }
                
                maxGap = max(maxGap , countGap[total]);
            }
            
            
        }
        return rows - maxGap;
        
    }
};