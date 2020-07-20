# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#


class Solution:
    def isValid(self, s: str) -> bool:
        left_bracket = ["(","{","["]
        right_bracket = [")","}","]"]
        dict = {")":"(",
               "]":"[",
               "}":"{"}
        stack = []
        for e in s:
            if e in left_bracket:
                stack.append(e)
            if e in right_bracket:
                try:
                    value = stack.pop()
                except:
                    return False
                if dict[e] != value:
                    return False
        return len(stack) == 0
                
                
                
        
