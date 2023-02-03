# Leetcode Solutions
Solutions for problems on the LeetCode platform

## Index
- [Palindrome Number](#palindrome-number)
- [Two Sum](#two-sum)
- [Roman to Integer](#roman-to-integer)

## Palindrome Number
### Python
#### Time Complexity
$$
\begin{flalign}
& O(n) &
\end{flalign}
$$
#### Space Complexity
$$
\begin{flalign}
& O(n) &
\end{flalign}
$$
#### Solution
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
#### Time Complexity
$$
\begin{flalign}
& O(n^2) &
\end{flalign}
$$
#### Space Complexity
$$
\begin{flalign}
& O(n) &
\end{flalign}
$$
#### Solution
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

## Roman to Integer

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value  |  
| ------ | ------ |
| I      | 1      |
| V      | 5      |
| X      | 10     |
| L      | 50     |
| C      | 100    |
| D      | 500    |
| M      | 1000   |

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. 
The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. 
Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Constraints:
* `1 <= s.length <= 15`
* `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
*  It is **guaranteed** that s is a valid roman numeral in the range [1, 3999].

#### [Solution: Python](./Python/roman_to_integer.py)
