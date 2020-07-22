# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Example: 
#
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
#
#
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #最开始想的算法是把所有null的节点都用list的null来表示，包括null的left和right节点
        #这样会导致有很多的null再result中，最后导致memory overflow
        #
        #新的算法同样采取bfs，但是对于空节点只记录自己本身一次null，并不再继续记录null的左右节点，节省了空间
        if not root:
            return None
        
        q = deque([root])
        res = []
        
        while q:
            curr = q.popleft()
            
            if curr:
                q.append(curr.left)
                q.append(curr.right)
            
            res.append(curr.val if curr else "null")
    
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        root = TreeNode(data[0])
        q = deque([root])
        i = 1
        
        while q:
            curr = q.popleft()
            
            if data[i] != "null":
                curr.left = TreeNode(data[i])
                q.append(curr.left)
            else:
                curr.left = None
                
            i += 1 
            
            if data[i] != "null":
                curr.right = TreeNode(data[i])
                q.append(curr.right)
            else:
                curr.right = None
            
            i += 1
                
        return root     
            
            

       

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
