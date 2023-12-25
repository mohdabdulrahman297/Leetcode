/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        // Recursive solution
        
        // Helper function for depth-first search
        std::function<std::pair<bool, int>(TreeNode*)> dfs = [&](TreeNode* node) -> std::pair<bool, int> {
            // If the node is null
            if (!node) return {true, 0};
            
            // Get the left and right nodes of the tree
            auto left = dfs(node->left);
            auto right = dfs(node->right);
            
            // Calculate if the tree is balanced (true or false)
            bool balanced = (left.first && right.first && abs(left.second - right.second) <= 1);
            
            // Return a pair of boolean and height
            return {balanced, 1 + std::max(left.second, right.second)};
        };
        
        // Return the boolean result
        return dfs(root).first;
    }
};