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
    bool valid(TreeNode* node, long left, long right) {
        if (!node) {
            return true;
        }

        // Basic valid tree checking
        if (!(node->val < right && node->val > left)) {
            return false;
        }

        // Recursive call for left and right
        // Since we're moving to the left, make the right node as the main node to make the algorithm work properly, similarly for the right as well
        return valid(node->left, left, node->val) && valid(node->right, node->val, right);
    }
};