# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#  
#
# Follow up: Solve it both recursively and iteratively.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        q = deque([root])

        while q:
            test_list = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    test_list.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    test_list.append(None)
                
            
            if len(test_list) % 2 != 0 and len(test_list) != 1:
                return False
            i,j = 0,len(test_list)-1
            while i < j:
                if test_list[i] != test_list[j]:
                    return False
                i += 1
                j -= 1
        
        return True
                
               
            
        
        
        
        
