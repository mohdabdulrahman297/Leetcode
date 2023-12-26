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
Time: O(n)
Space: O(n)
 */
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
    
private:
    int dfs(TreeNode* node, int maxVal){
        if(!node){
            return 0;
        }
        
        int res = (node->val >= maxVal) ? 1 : 0;
        
        maxVal = max(maxVal, node->val);
        
        res += dfs(node->left, maxVal);
        res += dfs(node->right, maxVal);
        
        return res;
    }
};


/*
int main() {
    // Example usage
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->left->left = new TreeNode(3);
    root->right->left = new TreeNode(1);
    root->right->right = new TreeNode(5);

    Solution solution;
    int result = solution.goodNodes(root);

    // Display the result
    cout << "Number of Good Nodes: " << result << endl;

    // Remember to free the allocated memory
    delete root->left->left;
    delete root->right->left;
    delete root->right->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
*/