###################################
# Author: Zachary Perales         #
#                                 #
# Time  Complexity: O(n)          #
# Space Complexity: O(1)          #
###################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[k]:
                nums[k + 1] = nums[i]
                k += 1
        return k + 1
