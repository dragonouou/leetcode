# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 100
# 	0 <= nums[i] <= 400
#
#


class Solution:
    def rob(self, nums: List[int]) -> int:
        #dynamic programming step1 base case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        # method1:  bottom-up, use list to store cache values, use too much memory   
        # memo = [0 for _ in range(len(nums))]
        # memo[0] = nums[0]
        # memo[1] = max(nums[0],nums[1])
        # memo[2] = max(nums[1], nums[0]+nums[2]) 
        # for i in range(3,len(nums)):
        #     memo[i] = max(memo[i-2]+nums[i],memo[i-3]+nums[i-1],memo[i-3]+nums[i])
        
        # method2: bottom-up, we only need memo[i-2] and memo[i-3] for memo[i];
        #after that, we don't need them anymore, save memory
        a = nums[0]
        b = max(nums[0],nums[1])
        c = max(nums[1],nums[0]+nums[2])
        for i in range(3, len(nums)):
            d = max(b+nums[i],a+nums[i-1],a+nums[i])
            a = b
            b = c
            c = d
        return d if len(nums) > 3 else c
        
        #method3: recursion too deep, time limit exceeded
        # return max(self.rob(nums[:-2])+ nums[-1], self.rob(nums[:-3])+nums[-2])
            
