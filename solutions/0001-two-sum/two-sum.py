# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_list = sorted(nums)
        i,j = 0, len(nums)-1
        while i < j:
            a = sorted_list[i]
            b = sorted_list[j]
            if a + b < target:
                i += 1
            elif a + b == target:
                if a != b:
                    return [nums.index(a),nums.index(b)]
                else:
                    c = nums.index(a)
                    nums[c] = None
                    d = nums.index(b)
                    return [c,d]
            else:
                j -= 1
                
