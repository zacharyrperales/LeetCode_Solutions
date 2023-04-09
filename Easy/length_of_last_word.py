###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(1)  #
###########################

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().rpartition(" ")[2])