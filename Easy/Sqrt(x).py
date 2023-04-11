###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(1)  #
###########################

class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1