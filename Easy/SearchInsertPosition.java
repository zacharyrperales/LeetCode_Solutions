###############################
# Author: Zachary Perales     #
#                             #
# Time  Complexity: O(log(n)) #
# Space Complexity: O(1)      #
###############################

class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = Arrays.binarySearch(nums, target);
        return (i >= 0) ? i : -(i + 1);
    }
}
