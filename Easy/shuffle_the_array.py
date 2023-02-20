###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(n)  #
###########################

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s = []
        for n1,n2 in zip(nums[:n],nums[n:]):
            s.append(n1)
            s.append(n2)
        return s
