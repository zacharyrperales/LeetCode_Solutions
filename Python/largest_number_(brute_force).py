############################
# Author: Zachary Perales  #
#                          #
# Time  Complexity: O(n^2) #
# Space Complexity: O(n)   #
############################

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = []
        str_nums.append(str(nums[0]))
        for num in nums[1:]:
            str_num = str(num)
            for i in range(len(str_nums)):
                if str_nums[i] + str_num <= str_num + str_nums[i]:
                    str_nums.insert(i, str_num)
                    break
                elif i == len(str_nums) - 1:
                    str_nums.insert(i + 1, str_num)
        largest_number = ''
        for str_num in str_nums:
            if len(largest_number) > 0:
                if largest_number[0] != '0':
                    largest_number += str_num
            else:
                largest_number += str_num
        return largest_number
