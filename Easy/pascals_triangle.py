###############################
# Author: Zachary Perales     #
#                             #
# Time  Complexity: O(n^2)    #
# Space Complexity: O(n^2)    #
###############################

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []
        for i in range(1, numRows + 1):
            if i == 1:
                pascals_triangle.append([1])
            elif i == 2:
                pascals_triangle.append([1,1])
            else:
                pascals_row = [1]
                for j in range(0, i - 2):
                    pascals_row.append(pascals_triangle[i-2][j] + pascals_triangle[i-2][j + 1])
                pascals_row.append(1)
                pascals_triangle.append(pascals_row)
        return pascals_triangle