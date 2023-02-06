############################
# Author: Zachary Perales  #
#                          #
# Time  Complexity: O(n^2) #
# Space Complexity: O(n)   #
############################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        reverse = list(reversed(nums))
        for x in nums:
            for y in reverse:
                if x + y == target and nums.index(x) != len(nums) - 1 - reverse.index(y) and not result:
                    result = [nums.index(x), len(nums) - 1 - reverse.index(y)]
        return result
