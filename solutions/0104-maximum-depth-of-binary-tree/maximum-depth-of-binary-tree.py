# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node,level = stack.pop()
            if node:
                max_depth = max(max_depth, level)
                stack.append((node.right,level + 1))
                stack.append((node.left,level + 1))
        return max_depth
        
        # if not root:
        #     return 0
        # height_left = self.maxDepth(root.left) + 1
        # height_right = self.maxDepth(root.right) + 1
        # return max(height_left,height_right) 
        
        
