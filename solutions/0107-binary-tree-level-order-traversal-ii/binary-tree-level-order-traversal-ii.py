# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root]) 
        res = []
        
        while len(q) > 0:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val) 
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right) 
            res.append(temp)     
        res.reverse()
        return res
            
        
#         level = math.log2(len(List) + 1) 
#         res = [None] * level
        
#         index = level - 1
#         count = 1
#         while len(List) > 0:
#             for _ in range(count):
#                 node = List.pop(0)
#                 if res[index] is None and node is not None:
#                     res[index] = [node]
#                 if res[index] is not None and node is not None:
#                     res[index].append(node)
#             index -= 1
#             count = count * 2
        
#         return res
        
