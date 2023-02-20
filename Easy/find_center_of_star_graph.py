###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(1)  #
# Space Complexity: O(1)  #
###########################

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in {edges[1][0], edges[1][1]}:
            return edges[0][0]
        else:
            return edges[0][1]
