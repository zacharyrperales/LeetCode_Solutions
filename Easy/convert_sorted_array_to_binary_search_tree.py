###########################
# Author: Zachary Perales #
#                         #
# Time  Complexity: O(n)  #
# Space Complexity: O(n)  #
###########################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        midpoint = int(len(nums) / 2)
        root = nums[midpoint]
        left = nums[:midpoint]
        right = nums[(midpoint + 1):]
        return TreeNode(root, self.sortedArrayToBST(left) if left else None, self.sortedArrayToBST(right) if right else None)
