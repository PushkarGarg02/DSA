# 🗓️ Can Attend All Appointments — Problem Statement

## 📘 Problem
Given an array of intervals representing **N appointments**, determine whether a person can attend **all** of them without any overlaps.

---

## 📌 Examples

### Example 1
**Input:**  
`[[1,4], [2,5], [7,9]]`

**Output:**  
`false`

**Explanation:**  
Appointments **[1,4]** and **[2,5]** overlap, so a person cannot attend both.

---

### Example 2
**Input:**  
`[[6,7], [2,4], [13,14], [8,12], [45,47]]`

**Output:**  
`true`

**Explanation:**  
None of the appointments overlap, so a person can attend all of them.

---

### Example 3
**Input:**  
`[[4,5], [2,3], [3,6]]`

**Output:**  
`false`

**Explanation:**  
Appointments **[4,5]** and **[3,6]** overlap, so a person cannot attend both.

---

## 🔒 Constraints
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`