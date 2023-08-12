//space : o(9) or o(1)
//  time: o(81) or o(1)
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> squares;

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') {
                    continue;
                }

                if (rows[r].find(board[r][c]) != rows[r].end() ||
                    cols[c].find(board[r][c]) != cols[c].end() ||
                    squares[3 * (r / 3) + c / 3].find(board[r][c]) != squares[3 * (r / 3) + c / 3].end()) {
                    return false;
                }

                cols[c].insert(board[r][c]);
                rows[r].insert(board[r][c]);
                squares[3 * (r / 3) + c / 3].insert(board[r][c]);
            }
        }
        
        return true;
    }
};
