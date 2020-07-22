# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            if l1.val > l2.val:
                cur = l2
                nex2 = l2.next
                nex1 = l1
                res = l2
            else:
                cur = l1
                nex1 = l1.next
                nex2= l2
                res = l1

            while nex1 and nex2:
                if nex1.val >= nex2.val:
                    nex = nex2
                    nex2 = nex.next
                else:
                    nex = nex1
                    nex1 = nex.next
                cur.next = nex
                cur = nex

            if nex1:
                cur.next = nex1
            if nex2:
                cur.next = nex2

            return res
            
        

        
