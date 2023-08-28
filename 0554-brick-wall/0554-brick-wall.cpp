// Time complexity: O(n x m)
// Space complexity: O(n x m)
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        
        // Create a hashmap to count gaps in each row
        unordered_map<int, int> countGap;
        
        int rows = wall.size();  // Get the number of rows in the wall
        int cols;  // Initialize variable to store the number of columns in each row
        int maxGap = 0;  // Initialize a variable to track the maximum gap count
        
        // Iterate through each row in the wall
        for (int i = 0; i < rows; i++) {
            int total = 0;  // Initialize a variable to keep track of the current total
            
            // '-1' because the edge of the wall is not considered
            cols = wall[i].size() - 1;  // Calculate the number of columns in the current row
            
            // Iterate through the columns in the current row
            for (int j = 0; j < cols; j++) {
                total += wall[i][j];  // Increment the total with the current brick's width
                
                // Check if the current total already exists in the hashmap
                if (countGap.find(total) != countGap.end()) {
                    countGap[total]++;  // If yes, increment the gap count at that position
                } else {
                    countGap[total] = 1;  // If not, create a new entry with gap count 1
                }
                
                // Update the maximum gap count with the current gap count
                maxGap = max(maxGap, countGap[total]);
            }
        }
        
        // Return the difference between the total number of rows and the maximum gap count
        return rows - maxGap;
    }
};

/*

int main() {
    Solution solution;
    
    // Create a 2D vector representing the wall
    vector<vector<int>> wall = {
        {1, 2, 2, 1},
        {3, 1, 2},
        {1, 3, 2},
        {2, 4},
        {3, 1, 2},
        {1, 3, 1, 1}
    };
    
    // Call the leastBricks function to find the minimum number of bricks to cross
    int result = solution.leastBricks(wall);
    
    // Print the result
    cout << "Minimum number of bricks to cross: " << result << endl;
    
    return 0;
}
*/


