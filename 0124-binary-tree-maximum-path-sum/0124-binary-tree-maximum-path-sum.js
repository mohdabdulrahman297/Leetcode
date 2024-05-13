/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
    let maxSum = -Infinity; // Initialize the maxSum with negative infinity

    // Helper function to traverse the tree and update maxSum
    const dfs = (node) => {
        if (!node) return 0; // Base case

        // Recursively calculate the sum of the left and right subtree
        const leftSum = Math.max(0, dfs(node.left)); // Ensure we don't consider negative values
        const rightSum = Math.max(0, dfs(node.right));

        // Update maxSum by considering the path that includes the current node
        maxSum = Math.max(maxSum, node.val + leftSum + rightSum);

        // Return the maximum sum that can be achieved from the current node
        return node.val + Math.max(leftSum, rightSum);
    };

    // Start the depth-first search from the root node
    dfs(root);

    return maxSum; // Return the maximum sum
};
