# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
#
#
# 	A rather straight forward solution is a two-pass algorithm using counting sort.
# 	First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# 	Could you come up with a one-pass algorithm using only constant space?
#
#


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,cur = 0, 0
        right = len(nums) - 1
        while cur <= right:
            if nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
                
                                   
        # i,j,k = 0,0,0
        # index = 0
        # for e in nums:
        #     if e == 0:
        #         i += 1
        #     elif e == 1:
        #         j += 1
        #     else:
        #         k += 1
        # while index < i:
        #     nums[index] = 0
        #     index += 1
        # while index < i + j:
        #     nums[index] = 1
        #     index += 1
        # while index < i + j + k:
        #     nums[index] = 2
        #     index += 1
        
            
                
        
