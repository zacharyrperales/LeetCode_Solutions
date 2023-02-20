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
    <a href="https://www.leetcode.com">LeetCode</a> Challenge Solutions
  </div>
  <br>
  <div align="left">
    Index
  </div>
</h1>
</div>

- Easy
  - [1. Two Sum](#1-two-sum)
  - [9. Palindrome Number](#9-palindrome-number)
  - [13. Roman to Integer](#13-roman-to-integer)
  - [14. Longest Common Prefix](#14-longest-common-prefix)
  - [20. Valid Parentheses](#20-valid-parentheses)
  - [21. Merge Two Sorted Lists](#21-merge-two-sorted-lists)
  - [108. Convert Sorted Array to Binary Search Tree](#108-convert-sorted-array-to-binary-search-tree)
  - [1470. Shuffle the Array](#1470-shuffle-the-array)
  - [1791. Find Center of Star Graph](#1791-find-center-of-star-graph)
- Medium
  - [179. Largest Number](#179-largest-number)

# 1. Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly*** **one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

## Constraints

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* **Only one valid answer exists.**

## Solution

| Language | Type                           |  
| :------: | :----------------------------: |
| python3  | [brute force: iterative](./Python/two_sum.py) |

# 9. Palindrome Number

Given an integer `x`, return `true` if `x` is a *[palindrome](https://en.wikipedia.org/wiki/Palindrome)*, and `false` otherwise.

## Constraints

* `-2^31 <= x <= 2^31 - 1`

## Solution

| Language | Type                                     |  
| :------: | :--------------------------------------: |
| python3  | [optimized: iterative](./Python/palindrome_number.py) |

# 13. Roman to Integer

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

## Solution

| Language | Type                                    |  
| :------: | :-------------------------------------: |
| python3  | [optimal: iterative, hashmap](./Python/roman_to_integer.py) |

# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

## Constraints

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters.

## Solution

| Language | Type                                         |  
| :------: | :------------------------------------------: |
| python3  | [optimized: iterative](./Python/longest_common_prefix.py) |

# 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

## Constraints

* `1 <= s.length <= 10^4`
* `s` consists of parentheses only `'()[]{}'`.

## Solution

| Language | Type                                                  |  
| :------: | :---------------------------------------------------: |
| python3  | [optimized: iterative, hashmap](./Python/valid_parentheses.py) |

# 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the *head of the merged linked list.*

## Constraints

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list` and `list2` are sorted in **non-decreasing** order.

## Solution

| Language | Type                                          |  
| :------: | :-------------------------------------------: |
| python3  | [optimized: recursive](./Python/merge_two_sorted_lists.py) |

# 108. Convert Sorted Array to Binary Search Tree

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a
[height-balanced](https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/) binary search tree.*

## Constraints

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` is sorted in a **strictly increasing** order.

## Solution

| Language | Type                                                                         |  
| :------: | :--------------------------------------------------------------------------: |
| python3  | [optimal: recursive](./Python/convert_sorted_array_to_binary_search_tree.py) |

# 179. Largest Number

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

## Constraints

* `1 <= nums.length <= 1001 <= nums.length <= 100`
* `0 <= nums[i] <= 10^9`

## Solution

| Language | Type                                                                                   |  
| :------: | :-----------------------------------------------------:                                |
| python3  | [optimal: custom sort](./Python/largest_number_1.py)                       |
|          | [optimal: timsort, custom comparator, concise](./Python/largest_number_2.py) |

# 1470. Shuffle the Array

Given the array `nums` consisting of 2n elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`.

*Return the array in the form* `[x1,y1,x2,y2,...,xn,yn]`.

## Constraints

* `1 <= n <= 500`
* `nums.length == 2n`
* `1 <= nums[i] <= 10^3`

## Solution

| Language | Type                                                |  
| :------: | :-------------------------------------------------: |
| python3  | [optimal: iterative](./Python/shuffle_the_array.py) |

# 1791. Find Center of Star Graph

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

## Solution

| Language | Type                                                        |  
| :------: | :---------------------------------------------------------: |
| python3  | [optimal](./Python/find_center_of_star_graph.py) |

