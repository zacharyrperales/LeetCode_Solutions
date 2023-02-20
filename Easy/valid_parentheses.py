###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(n)  #
###########################

class Solution:
    def isValid(self, s: str) -> bool:
        p = {')':'(','}':'{',']':'['}
        if len(s)%2 != 0:
            return False
        stack = []
        for c in s:
            if c not in p:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif p.get(c) == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
