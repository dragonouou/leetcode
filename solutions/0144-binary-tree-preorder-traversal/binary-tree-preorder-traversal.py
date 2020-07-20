# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #         recursion
        # if not root:
        #     return []
        # res = [root.val]
        # if root.left:
        #     res += self.preorderTraversal(root.left)
        # if root.right:
        #     res += self.preorderTraversal(root.right)
        # return res
        
#           iteration
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
                
        return res
