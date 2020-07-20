# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #       此方法是o（n2），还可以通过o（logN）进行sort，通过3个指针进行一次loop实现o（nlogn）
        res = []
        new_list = copy.copy(nums)
        pop_list = []
        while len(new_list) >= 3:
            i = 0
            value = new_list.pop()
            pop_list.append(value)
            target = 0 - value
            two_sum_res = self.twoSum(new_list,target)
            for every_list in two_sum_res:
                every_list.append(value)
                res.append(every_list)
            while i < len(new_list):
                if new_list[i] == value:
                    del new_list[i]
                else:
                    i += 1
        return res
    
    def twoSum(self, nums, target):
        hash_map = {}
        res = []
        test_list = []
        for i in range(len(nums)):
            if (target - nums[i]) in hash_map and nums[i] not in test_list:
                res.append([(target - nums[i]), nums[i]])
                test_list.append(target-nums[i])
                test_list.append(nums[i])
            else:
                hash_map[nums[i]] = target - nums[i]
        return res
        
