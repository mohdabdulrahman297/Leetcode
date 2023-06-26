// time:o(n^2)
// space: o(n^2)
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        vector<vector<int>> result;
        
        for(int i=0;i<numRows;i++){
            vector<int> row(i+1 , 1);
            for(int j=1;j<i;j++){
                row[j] = result[i-1][j-1] + result[i-1][j];
            }
            result.push_back(row);
            
        }
        return result;
        
    }
};

/*
int main() {
    Solution solution;

    int numRows = 5;
    vector<vector<int>> result = solution.generate(numRows);

    // Print the generated Pascal's Triangle
    for (const auto& row : result) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
*/