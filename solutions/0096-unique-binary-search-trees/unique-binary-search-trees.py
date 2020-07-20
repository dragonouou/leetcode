# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 19
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.numTreesMemo(n, memo)
    
    def numTreesMemo(self, n, memo):
        if n == 0 or n == 1:
            memo[n] = 1
        if memo[n] == 0:
            for i in range(0, (n-1)//2 + 1):
                memo[n] += self.numTreesMemo(i,memo) * self.numTreesMemo(n-1-i,memo)
            if n % 2 != 0:
                memo[n] = 2 * memo[n] - pow(self.numTreesMemo((n-1)//2,memo),2)
            else:
                memo[n] = 2 * memo[n]
        return memo[n]
        
    
    
