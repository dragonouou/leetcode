# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# 	Given n will be between 1 and 9 inclusive.
# 	Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        sorted_list = list(range(1, n+1))        
        remainder = k
        ans = 0
        module = 1 
        for i in range(1, n):
            module = module * i
        
        while n > 0: 
            quotient = remainder // module 
            remainder = remainder % module
            if remainder == 0 and quotient > 0:
                quotient = quotient - 1
            ans = ans + sorted_list[quotient] * pow(10, n - 1)
            sorted_list.pop(quotient)                       
            n -= 1
            if remainder == 0:
                break
            if n != 0:
                module = module // n
        
        while len(sorted_list) > 0:
            ans = ans + sorted_list[-1] * pow(10, len(sorted_list)-1)
            sorted_list.pop(-1)
            
        return str(ans)

        
        
