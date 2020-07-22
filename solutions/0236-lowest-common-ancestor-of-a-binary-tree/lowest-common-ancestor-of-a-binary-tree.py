# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#  
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#
#
#  
#
# Note:
#
#
# 	All of the nodes' values will be unique.
# 	p and q are different and both values will exist in the binary tree.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
          
        queue = deque([root])
        p_parent = []
        q_parent = []
        hash_map = {}
        found = 2
        
        while (queue and found > 0):
            curr = queue.popleft()

            if curr.val == p.val:
                p_parent.append(p)
                found -= 1
                temp = curr
                while temp in hash_map:
                    p_parent.append(hash_map[temp])
                    temp = hash_map[temp]
                    
            if curr.val == q.val:
                q_parent.append(q)
                found -= 1
                temp = curr
                while temp in hash_map:
                    q_parent.append(hash_map[temp])
                    temp = hash_map[temp]
                    
            if curr.left:
                queue.append(curr.left)
                hash_map[curr.left] = curr
            if curr.right:
                queue.append(curr.right)
                hash_map[curr.right] = curr
        
        for i in p_parent:
            if i in q_parent:
                return i
            
        
       
        
