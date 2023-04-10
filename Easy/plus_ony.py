###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(1)  #
###########################

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            digits.append(1)
        else:
            for i in reversed(range(len(digits))):
                digits[i] = 0 if digits[i] == 9 else digits[i] + 1
                if digits[i] != 0:
                    break
                elif i == 0:
                    digits.insert(0, 1)
        return digits