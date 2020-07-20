# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution:
    def reverse(self, x: int) -> int:
        absx = abs(x)
        num = 0
        while (absx != 0):
            temp = absx % 10
            num = num * 10 + temp
            absx = absx // 10
            
        if x >= 0 and num < 2**31:
            return num
        elif x < 0 and num <= 2**31:
            return -num
        else:
            return 0
    
        
