# Interval List Intersections

## 🧩 Problem Statement
Given two lists of intervals, compute their intersection.  
Each list contains **disjoint**, **sorted** intervals based on their start time.

---

## 📘 Example 1

**Input:**  
`arr1 = [[1, 3], [5, 6], [7, 9]]`  
`arr2 = [[2, 3], [5, 7]]`

**Output:**  
`[2, 3], [5, 6], [7, 7]`

**Explanation:**  
These are the overlapping portions between intervals in the two lists.

---

## 📙 Example 2

**Input:**  
`arr1 = [[1, 3], [5, 7], [9, 12]]`  
`arr2 = [[5, 10]]`

**Output:**  
`[5, 7], [9, 10]`

**Explanation:**  
The output contains the common overlapping intervals.

---

## 📏 Constraints

- `0 <= arr1.length, arr2.length <= 1000`
- `arr1.length + arr2.length >= 1`
- For each interval in `arr1`:
    - `0 <= start_i < end_i <= 10^9`
    - Intervals are non‑overlapping and sorted: `end_i < start_{i+1}`
- For each interval in `arr2`:
    - `0 <= start_j < end_j <= 10^9`
    - Intervals are non‑overlapping and sorted: `end_j < start_{j+1}`