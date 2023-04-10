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
  - [26. Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array)
  - [27. Remove Element](#27-remove-element)
  - [35. Search Insert Position](#31-search-insert-position)
  - [58. Length of Last Word](#58-length-of-last-word)
  - [66. Plus One](#66-plus-one)
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

* `2 <= nums.length <=` ${10^{4}}$
* ${-10^{9}}$ `<= nums[i] <=` ${10^{9}}$
* ${-10^{9}}$ `<= target <=` ${10^{9}}$
* **Only one valid answer exists.**

## Solution

| Language  | Type                           |  
| :-------: | :----------------------------: |
| Python 3  | [brute force: iterative](./Easy/two_sum.py) |

# 9. Palindrome Number

Given an integer `x`, return `true` *if* `x` *is a [palindrome](https://en.wikipedia.org/wiki/Palindrome), and* `false` *otherwise*.

## Constraints

* ${-2^{31}}$ `<= x <=` ${2^{31}}$ `- 1`

## Solution

| Language  | Type                                     |  
| :-------: | :--------------------------------------: |
| Python 3  | [optimized: iterative](./Easy/palindrome_number.py) |

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

| Language  | Type                                    |  
| :-------: | :-------------------------------------: |
| Python 3  | [optimal: iterative, hashmap](./Easy/roman_to_integer.py) |

# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Constraints

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters.

## Solution

| Language  | Type                                         |  
| :-------: | :------------------------------------------: |
| Python 3  | [optimized: iterative](./Easy/longest_common_prefix.py) |

# 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

## Constraints

* `1 <= s.length <=` ${10^4}$
* `s` consists of parentheses only `'()[]{}'`.

## Solution

| Language  | Type                                                  |  
| :-------: | :---------------------------------------------------: |
| Python 3  | [optimized: iterative, hashmap](./Easy/valid_parentheses.py) |

# 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list.*

## Constraints

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list` and `list2` are sorted in **non-decreasing** order.

## Solution

| Language  | Type                                          |  
| :-------: | :-------------------------------------------: |
| Python 3  | [optimized: recursive](./Easy/merge_two_sorted_lists.py) |

# 26. Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates in-place such that each unique element appears only **once**. 
The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, 
then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array** [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.

# 27. Remove Element

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [in-place](https://en.wikipedia.org/wiki/In-place_algorithm). 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. 
More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input** array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.

## Constraints

* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`
* `0 <= val <= 100`

## Solution

| Language  | Type                                          |  
| :-------: | :-------------------------------------------: |
| Python 3  | [optimal](./Easy/remove_element.py)           |

## Constraints

* `1 <= nums.length <= 3 *` ${10^4}$
* `-100 <= nums[i] <= 100`
* `nums` is sorted in **non-decreasing** order.

## Solution

| Language  | Type                                          |  
| :-------: | :-------------------------------------------: |
| Python 3  | [optimal: iterative](./Easy/remove_duplicates_from_sorted_array.py) |

# 35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints
* `1 <= nums.length <=` $10^4$
* $-10^4$ `<= nums[i] <=` $10^4$
* `nums` contains **distinct** values sorted in **ascending** order.
* $-10^4$ `<= target <=` $10^4$

## Solution

| Language | Type                                          |  
| :------: | :-------------------------------------------: |
| Java     | [optimized: binary search, class methods](./Easy/SearchInsertPosition.java) |

# 58. Length of Last Word

Given a string `s` consisting of words and spaces, return the *length of the ***last*** *word in the string.*

A **word** is a maximal [substring](https://en.wikipedia.org/wiki/Substring) consisting of non-space characters only.
 
## Constraints

* `1 <= s.length <=` $10^4$
* `s` consists of only English letters and spaces `' '`.
* There will be at least one word in `s`.

## Solution

| Language | Type                                          |  
| :------: | :-------------------------------------------: |
| Python   | [optimal](./Easy/length_of_last_word.py)      |

# 66. Plus One

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the $i^{th}$ digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

## Constraints

* `1 <= digits.length <= 100`
* `0 <= digits[i] <= 9`
* `digits` does not contain any leading `0`'s.

## Solution

| Solution                       |
| :----------------------------: |
| [Python](./Easy/plus_one.py)   |

# 108. Convert Sorted Array to Binary Search Tree

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a
[height-balanced](https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/) binary search tree.*

## Constraints

* `1 <= nums.length <=` ${10^4}$
* ${-10^4}$ `<= nums[i] <=` ${10^4}$
* `nums` is sorted in a **strictly increasing** order.

## Solution

| Language  | Type                                                                         |  
| :-------: | :--------------------------------------------------------------------------: |
| Python 3  | [optimal: recursive](./Easy/convert_sorted_array_to_binary_search_tree.py) |

# 179. Largest Number

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

## Constraints

* `1 <= nums.length <= 100`
* `0 <= nums[i] <=` ${10^9}$

## Solution

| Language  | Type                                                                                   |  
| :-------: | :-----------------------------------------------------:                                |
| Python 3  | [optimal: custom sort](./Medium/largest_number_1.py)                       |
|           | [optimal: timsort, custom comparator, concise](./Medium/largest_number_2.py) |

# 1470. Shuffle the Array

Given the array `nums` consisting of `2n` elements in the form `[` ${x_1}$ `,` ${x_2}$ `, ...,` ${x_n}$ `,` ${y_1}$ `,` ${y_2}$ `, ...,` ${y_n}$ `]`.

*Return the array in the form* `[` ${x_1}$ `,` ${y_1}$ `,` ${x_2}$ `,` ${y_2}$ `, ...,` ${x_n}$ `,` ${y_n}$ `]`.

## Constraints

* `1 <= n <= 500`
* `nums.length == 2n`
* `1 <= nums[i] <=` ${10^3}$

## Solution

| Language  | Type                                                |  
| :-------: | :-------------------------------------------------: |
| Python 3  | [optimal: iterative](./Easy/shuffle_the_array.py) |

# 1791. Find Center of Star Graph

There is an undirected **star** graph consisting of `n` nodes labeled from `1` to `n`
A star graph is a graph where there is one **center** node and **exactly** `n - 1` edges
that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [` ${u_i}$ `,` ${v_i}$ `]` 
indicates that there is an edge between the nodes ${u_i}$ and ${v_i}$. Return the center of the given star graph.

## Constraints

* `3 <= n <=` ${10^5}$
* `edges.length == n - 1`
* `edges[i].length == 2`
* `1 <=` ${u_i}$ `,` ${v_i}$ `<= n`
* ${u_i}$ `!=` ${v_i}$
* The given `edges` represent a valid star graph.

## Solution

| Language  | Type                                                        |  
| :-------: | :---------------------------------------------------------: |
| Python 3  | [optimal](./Easy/find_center_of_star_graph.py) |

