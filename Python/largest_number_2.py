###################################
# Author: Zachary Perales         #
#                                 #
# Time  Complexity: O(n * log(n)) #
# Space Complexity: O(n)          #
###################################

def compare(num1: int, num2: int) -> int:
        return int(str(num2) + str(num1)) - int(str(num1) + str(num2))

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_number = ''.join(sorted(map(str, nums), key=cmp_to_key(compare)))
        if largest_number[0] == '0':
            return '0'
        else:
            return largest_number
