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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        
        if(!root){
            return result;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){
            TreeNode* rightSide = nullptr;
            int qSize = q.size();
            
            for(int i=0; i<qSize; ++i){
                TreeNode* node = q.front();
                q.pop();
                
                if(node){
                    rightSide = node;
                    if(node->left){
                        q.push(node->left);
                    }
                    if(node->right){
                        q.push(node->right);
                    }
                }
            }
            if(rightSide){
                    result.push_back(rightSide->val);
                }
        }
        return result;
    }
};

/*
int main() {
    // Example usage
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(4);

    Solution solution;
    vector<int> result = solution.rightSideView(root);

    // Display the result
    cout << "Right Side View: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    // Remember to free the allocated memory
    delete root->left->right;
    delete root->right->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
*/