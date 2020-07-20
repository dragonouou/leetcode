# We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
#
#
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#
#  
#
# Note: The length of the input array will not exceed 20,000.
#


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        low = 0
        fast = 1
        result = 0
        while fast < len(nums):
            if sorted_list[fast] - sorted_list[low] == 1:
                length = fast - low + 1
                if length > result:
                    result = length
                fast += 1
            elif sorted_list[fast] == sorted_list[low]:
                fast += 1
            else:
                low += 1
            
            if fast == low:
                fast += 1
                continue
            
        
        return result
                
