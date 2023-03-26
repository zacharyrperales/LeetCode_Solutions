####################################################
# Author: Zachary Perales                          #
#                                                  #
# Time  Complexity: O(n)                           #
# Space Complexity: O(1)                           #
#                                                  #
# Note: There is an error preventing the solution  #
#       from being written more concisely.         #
####################################################

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_value_index = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                nums[i] = nums[valid_value_index]
                nums[valid_value_index] = 0
                valid_value_index = valid_value_index - 1

        return valid_value_index + 1
