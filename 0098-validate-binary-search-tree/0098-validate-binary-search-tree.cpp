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
    bool isValidBST(TreeNode* root) {
      return valid(root, numeric_limits<long>::min(), numeric_limits<long>::max());  
    }
    
private:
    bool valid(TreeNode* node, long left, long right){
        if(!node){
            return true;
        }
        
        if(!(node->val < right && node->val > left)){
            return false;
        }
        
        return valid(node->left, left, node->val) & valid(node->right, node->val, right);
    }
};


/*
int main() {
    // Example usage
    TreeNode* root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);

    Solution solution;
    bool result = solution.isValidBST(root);

    // Display the result
    cout << "Is Valid BST: " << (result ? "true" : "false") << endl;

    // Remember to free the allocated memory
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
*/