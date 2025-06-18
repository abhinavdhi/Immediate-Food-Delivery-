# Immediate Food Delivery II

This project solves a grouping problem using Python.

## 🧩 Problem Statement

You are given an integer array `nums` of size `n` where `n` is a multiple of 3 and a positive integer `k`.

**Goal:** Divide `nums` into `n / 3` arrays of size 3 such that in each array, the difference between any two elements is less than or equal to `k`.

If it is impossible to do so, return an empty list. If there are multiple valid answers, any one is acceptable.

## 💡 Approach

1. Sort the input array.
2. Try to form groups of 3 from consecutive elements.
3. Ensure the maximum difference within each group is `≤ k`.

## ✅ Example

```python
Input:
nums = [1, 3, 4, 6, 8, 9]
k = 2

Output:
[[1, 3, 4], [6, 8, 9]]   # If max difference ≤ 2
