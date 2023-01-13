# Leetcode Solutions
Original solutions
## Index
- [Palindrome Number](#palindrome-number)
- [Two Sum](#two-sum)
## Palindrome Number
### Python
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        unreversed = str(x)
        reversed = ""
        i = 0
        for digit in unreversed:
            reversed = reversed + unreversed[len(unreversed)- 1 - i]
            i = i + 1
        if unreversed.__eq__(reversed):
            return True
        return False
```

## Two Sum
### Python
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        reverse = list(reversed(nums))
        for x in nums:
            for y in reverse:
                if x + y == target and nums.index(x) != len(nums) - 1 - reverse.index(y) and not result:
                    result = [nums.index(x), len(nums) - 1 - reverse.index(y)]
        return result
```
