![License](https://img.shields.io/github/license/aardzark/LeetCode_Python_Solutions?color=%233D79A9)
![HitCount](https://img.shields.io/endpoint?color=%23F7D550&url=https%3A%2F%2Fhits.dwyl.com%2Faardzark%2FLeetCode_Python_Solutions.json)
![Top Language](https://img.shields.io/github/languages/top/aardzark/LeetCode_Python_Solutions?color=%233d79a9)
![Last Commit](https://img.shields.io/github/last-commit/aardzark/LeetCode_Python_Solutions?color=f7d550)

<div>
<h1>
<br>
  <div align="center">
    <a href="https://www.leetcode.com/zacharyromeperales"><img src="https://camo.githubusercontent.com/7c89b46de0f34cfcc4d8c7217c2359d1b1af78c72151f73f4e81b7aa127ca4c6/68747470733a2f2f692e696d6775722e636f6d2f49735335786b5a2e706e67" width="200"></a>
    <br>
    <a href="https://www.leetcode.com">LeetCode</a> Challenge Solutions in Python
  </div>
  <br>
  <div align="left">
    Index
  </div>
</h1>
</div>

- [Palindrome Number](#palindrome-number)
- [Two Sum](#two-sum)
- [Roman to Integer](#roman-to-integer)
- [Longest Common Prefix](#longest-common-prefix)
- [Valid Parentheses](#valid-parentheses)
- [Shuffle the Array](#shuffle-the-array)
- [Find Center of Star Graph](#find-center-of-star-graph)

# Palindrome Number

Given an integer `x`, return `true` if `x` is a *[palindrome](https://en.wikipedia.org/wiki/Palindrome)*, and `false` otherwise.

## Constraints

* `-2^31 <= x <= 2^31 - 1`

### [Solution](./Python/palindrome_number.py)

# Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly*** **one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

## Constraints
* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* **Only one valid answer exists.**


### [Solution](./Python/two_sum.py)

# Roman to Integer

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

## Constraints
* `1 <= s.length <= 15`
* `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
*  It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

### [Solution](./Python/roman_to_integer.py)

# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Constraints

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters.

### [Solution](./Python/longest_common_prefix.py)

# Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

## Constraints

* `1 <= s.length <= 10^4`
* `s` consists of parentheses only `'()[]{}'`.

### [Solution](./Python/valid_parentheses.py)

# Shuffle the Array

Given the array `nums` consisting of 2n elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.

*Return the array in the form* `[x1,y1,x2,y2,...,xn,yn]`.

## Constraints

* `1 <= n <= 500`
* `nums.length == 2n`
* `1 <= nums[i] <= 10^3`

### [Solution](./Python/shuffle_the_array.py)

# Find Center of Star Graph

There is an undirected **star** graph consisting of `n` nodes labeled from `1` to `n`
A star graph is a graph where there is one **center** node and **exactly** `n - 1` edges
that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [u subscript(i), v subscript(i)]` 
indicates that there is an edge between the nodes `u subscript(i)` and `v subscript(i)`. Return the center of the given star graph.

## Constraints

* `3 <= n <= 10^5`
* `edges.length == n - 1`
* `edges[i].length == 2`
* `1 <= u subscript(i), v subscript(i) <= n`
* `u subscript(i) != v subscript(i)`
* The given `edges` represent a valid star graph.

### [Solution: Python](./Python/find_center_of_star_graph.py)
