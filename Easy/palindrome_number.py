###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(n)  #
###########################

class Solution:
    def isPalindrome(self, x: int) -> bool:
        unreversed = str(x)
        reversed = ""
        i = 0
        for digit in unreversed:
            reversed = reversed + unreversed[len(unreversed)- 1 - i]
            i = i + 1
        if unreversed.__eq__(reversed):
            return True
        return False
