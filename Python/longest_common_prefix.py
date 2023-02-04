###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(nm) #
# Space Complexity: O(m)  #
###########################

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for str in strs[1:]:
            for i in range(len(lcp)):
                if lcp[:(i + 1)] != str[:(i + 1)]:
                    lcp = lcp[:i]
                    break
        return lcp
