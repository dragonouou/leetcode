# Given a binary tree
#
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  
#
# Follow up:
#
#
# 	You may only use constant extra space.
# 	Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
#
#  
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the given tree is less than 6000.
# 	-100 <= node.val <= 100
#
#


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        curr = root
        
        dummy = Node()
        pre = dummy
        while curr:
            pre.next = curr.left
            if pre.next:
                pre = pre.next
            pre.next = curr.right
            if pre.next:
                pre = pre.next
            curr = curr.next
            #本层结束
            if not curr:
                curr = dummy.next
                pre = dummy
        return root
        
        
#         # initialize a virtual node
#         next_level = Node()
#         pre = next_level
#         dummy = next_level
        
#         #如果有下一层node，则继续；否则退出loop
#         while next_level:
#             next_level = None
#             while curr:
#                 if curr.left:
#                     #用pre来指向目前正在改变next pointer的node
#                     pre.next = curr.left
#                     #定位下一层node的起始点
#                     if not next_level:
#                         next_level = curr.left
#                     pre = pre.next
#                 if curr.right:
#                     pre.next = curr.right
#                     if not next_level:
#                         next_level = curr.right
#                     pre = pre.next
#                 #在本层循环
#                 curr = curr.next
#             # 本层结束，到下一层；set curr to the starting point of next-level nodes
#             curr = next_level
#             pre = dummy
            
#         return root
        
        
