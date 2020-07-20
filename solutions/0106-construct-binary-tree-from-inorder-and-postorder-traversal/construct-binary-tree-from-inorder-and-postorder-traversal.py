# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#
# Return the following binary tree:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        
        root_value = postorder[-1]
        root_index = inorder.index(root_value)
        root = TreeNode(root_value)
        root.left = self.buildTree(inorder[:root_index],postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:],postorder[root_index:-1])
        return root