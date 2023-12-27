# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ## preorder traversal : root, left, right
        ## inorder traversal : left, root, right
        
        ## base case
        if not preorder or not inorder:
            return None
        
        ## first value in preorder array is root of the tree
        
        root = TreeNode(preorder[0])
        ## find that value in inorder
        mid = inorder.index(preorder[0])
        ## partitioning the left and right
        ## left = start from the 1st value of preorder because the 0th value is taken as root(preorder) and for inorder 0th to value before mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        ## right = start from mid+1 and to the end of preorder array, for inorder mid+1 to the end
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        