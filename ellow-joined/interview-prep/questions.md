# Python Interview Practice Set

## Question 1: Contains Duplicate

### Problem Statement

Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

### Example 1

Input:

```python
nums = [1,2,3,1]
```

Output:

```python
True
```

### Example 2

Input:

```python
nums = [1,2,3,4]
```

Output:

```python
False
```

### Constraints

* Solve with optimal time complexity if possible.

---

## Question 2: Valid Anagram

### Problem Statement

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, otherwise return `False`.

An anagram is formed by rearranging the letters of another word using all original letters exactly once.

### Example 1

Input:

```python
s = "anagram"
t = "nagaram"
```

Output:

```python
True
```

### Example 2

Input:

```python
s = "rat"
t = "car"
```

Output:

```python
False
```

---

## Question 3: Two Sum

### Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

Assume exactly one solution exists.

You may not use the same element twice.

### Example

Input:

```python
nums = [2,7,11,15]
target = 9
```

Output:

```python
[0,1]
```

Explanation:

```python
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Question 4: Binary Search

### Problem Statement

Given a sorted array of integers `nums` and an integer `target`, return the index of `target`.

If the target does not exist, return `-1`.

### Example 1

Input:

```python
nums = [-1,0,3,5,9,12]
target = 9
```

Output:

```python
4
```

### Example 2

Input:

```python
nums = [-1,0,3,5,9,12]
target = 2
```

Output:

```python
-1
```

Requirement:

* Time Complexity must be O(log n)

---

## Question 5: Longest Substring Without Repeating Characters

### Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1

Input:

```python
s = "abcabcbb"
```

Output:

```python
3
```

Explanation:

```python
"abc"
```

### Example 2

Input:

```python
s = "bbbbb"
```

Output:

```python
1
```

### Example 3

Input:

```python
s = "pwwkew"
```

Output:

```python
3
```

Explanation:

```python
"wke"
```

---

## Question 6: Reverse String

### Problem Statement

Given a string `s`, return the reversed string.

### Example

Input:

```python
s = "hello"
```

Output:

```python
"olleh"
```

---

## Question 7: Merge Two Sorted Arrays

### Problem Statement

Given two sorted arrays, merge them into a single sorted array.

### Example

Input:

```python
arr1 = [1,3,5]
arr2 = [2,4,6]
```

Output:

```python
[1,2,3,4,5,6]
```

---

## Question 8: Maximum Subarray

### Problem Statement

Given an integer array `nums`, find the contiguous subarray that has the largest sum and return the sum.

### Example

Input:

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Output:

```python
6
```

Explanation:

```python
[4,-1,2,1]
```

has the largest sum.

---

## Question 9: Best Time to Buy and Sell Stock

### Problem Statement

You are given an array where each element represents a stock price on a given day.

Find the maximum profit possible by buying once and selling once.

### Example

Input:

```python
prices = [7,1,5,3,6,4]
```

Output:

```python
5
```

Explanation:

```python
Buy at 1
Sell at 6
Profit = 5
```

---

## Question 10: Group Anagrams

### Problem Statement

Given an array of strings, group all anagrams together.

### Example

Input:

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

Output:

```python
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]
```

---

For Every Question

Be ready to explain:

1. Brute Force Solution
2. Optimized Solution
3. Time Complexity
4. Space Complexity
5. Why your optimized solution is better
