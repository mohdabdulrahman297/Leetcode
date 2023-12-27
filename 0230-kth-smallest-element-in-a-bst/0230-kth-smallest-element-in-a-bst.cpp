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
    int kthSmallest(TreeNode* root, int k) {
        int n = 0;
        stack<TreeNode*> stack;
        TreeNode* cur = root;
        
        while(cur || !stack.empty()){
            while(cur){
                stack.push(cur);
                cur = cur->left;
            }
            
            cur = stack.top();
            stack.pop();
            
            n += 1;
            if(n == k){
                return cur->val;
            }
            cur = cur->right;
        }
        
        return -1;
    }
};