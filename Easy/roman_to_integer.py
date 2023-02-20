###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(1)  #
###########################

class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for i in enumerate(s):
            if (i[0] < len(s) - 1) and numerals.get(i[1]) < numerals.get(s[i[0] + 1]):
                value = value - numerals.get(i[1])
            else:
                value = value + numerals.get(i[1])

        return value
