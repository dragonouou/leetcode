# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
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
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        q = deque([(root, 0)])
        res = []
        flag = -1
        temp = []
       
        while q:
            #可以用for loop的方法保证划分层，也可以用（root，level）标记每层的level来区分
            for _ in range(len(q)):
                node,level = q.popleft()
                if node:
                    temp.append(node.val)
                    q.append((node.left, level + 1))
                    q.append((node.right, level + 1))
            flag = flag * (-1)
            if temp:
                res.append(temp[::flag])
            temp = []
                
        return res
        
