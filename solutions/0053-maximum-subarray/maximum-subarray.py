# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 1
        max_sum = nums[0]
        cur_sum = nums[0]

        while i < len(nums):
            cur_sum = cur_sum + nums[i]
            
            if cur_sum < nums[i]:
                cur_sum = nums[i]             
                
            max_sum = max(cur_sum, max_sum)
            i += 1
                
        
        return max_sum
