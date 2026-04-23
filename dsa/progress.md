# DSA Progress Tracker

> Single source of truth for all problems — pattern, revision status, and next retry date.  
> AI must update Status, Step, and Next Retry after every revision attempt.

## Two Pointers (7 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Container With Most Water | Shrink from both ends | Retry | Easy-final pending | May 2 |
| 2 | Move Zeroes | Partition (slow-fast) | New | — | — |
| 3 | Valid Palindrome | Compare inward | Retry | Easy-final pending | May 6 |
| 4 | Two Sum II (Sorted) | Shrink from both ends | Retry | Easy-final pending | May 6 |
| 5 | Remove Duplicates (Sorted Array) | Slow-fast write | Retry | Easy-final pending | Apr 29 |
| 6 | Remove Element | Partition | New | — | — |
| 7 | 3Sum | Two Pointers + Dedup | New | — | — |

## Hashmap / Set (6 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Valid Anagram | Frequency count | Retry | Easy-final pending | May 6 |
| 2 | Two Sum (Unsorted) | Complement lookup | New | — | — |
| 3 | Intersection of Two Arrays | Set intersection | New | — | — |
| 4 | Contains Duplicate | Set membership | Retry | Easy-final pending | May 6 |
| 5 | First Unique Character | Frequency count | New | — | — |
| 6 | Happy Number | Cycle detection via set | Retry | Easy-final pending | May 6 |

## Sliding Window (6 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Find Maximum Average Subarray I | Fixed window | New | — | — |
| 2 | Permutation in String | Fixed window + freq match | Retry | Easy-final pending | May 4 |
| 3 | Longest Substring Without Repeating | Violation-based shrink | Retry | Good-2 pending | Apr 27 |
| 4 | Minimum Size Subarray Sum | Goal-based shrink | New | — | — |
| 5 | Longest Repeating Character Replacement | Goal-based | New | — | — |
| 6 | Max Consecutive Ones III | Goal-based | New | — | — |

## Prefix Sum (5 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Subarray Sum Equals K | Prefix + Hashmap (Count) | Retry | Hard-3 pending | Apr 28 |
| 2 | Continuous Subarray Sum | Prefix + Hashmap (Modulo, Boolean) | New | — | — |
| 3 | Subarray Sums Divisible by K | Prefix + Hashmap (Modulo, Count) | New | — | — |
| 4 | Binary Subarrays With Sum | Prefix + Hashmap (Exact Sum, Count) | Retry | Good-2 pending | Apr 30 |
| 5 | Maximum Size Subarray Sum Equals K | Prefix + Hashmap (Max Length) | New | — | — |

## Kadane's Algorithm (3 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Maximum Subarray | Classic Kadane | New | — | — |
| 2 | Best Time to Buy and Sell Stock | Kadane variant (min so far) | New | — | — |
| 3 | Maximum Sum Circular Subarray | Kadane + circular trick | Retry | Good-2 pending | Apr 25 |

## Binary Search (6 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Binary Search (LC 704) | Exact match | New | — | — |
| 2 | Guess Number Higher or Lower | Hidden space | New | — | — |
| 3 | First Bad Version | Boundary / First True | Retry | Good-2 pending | Apr 27 |
| 4 | Koko Eating Bananas | Binary Search on Answer (Min Feasible) | Retry | Hard-3 pending | Apr 28 |
| 5 | Capacity To Ship Packages | Binary Search on Answer | New | — | — |
| 6 | Split Array Largest Sum | Binary Search on Answer | New | — | — |

## Monotonic Stack (5 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Next Greater Element I | Next greater (right) | New | — | — |
| 2 | Daily Temperatures | Next greater (right, index diff) | New | — | — |
| 3 | Next Greater Element II | Circular next greater | New | — | — |
| 4 | Largest Rectangle in Histogram | Span-based (left+right boundary) | Retry | Hard-3 pending | Apr 29 |
| 5 | Trapping Rain Water | Min(maxLeft, maxRight) - height | Retry | Good-2 pending | Apr 25 |

## Trees — DFS + BFS (10 problems)

| # | Problem | Variant | Status | Step | Next Retry |
| --- | --- | --- | --- | --- | --- |
| 1 | Maximum Depth of Binary Tree | Return height | New | — | — |
| 2 | Same Tree | Compare two trees | New | — | — |
| 3 | Invert Binary Tree | Swap children | New | — | — |
| 4 | Diameter of Binary Tree | Global + return height | Retry | Good-2 pending | Apr 27 |
| 5 | Balanced Binary Tree | Boolean check (-1 signal) | Retry | Good-2 pending | Apr 30 |
| 6 | Path Sum | Root-to-leaf sum check | New | — | — |
| 7 | Lowest Common Ancestor | Find LCA using left/right signals | New | — | — |
| 8 | Binary Tree Level Order Traversal | BFS with queue, level-wise grouping | New | — | — |
| 9 | Validate BST | Range check (lower, upper) pass in recursion | Retry | Easy-final pending | May 4 |
| 10 | Binary Tree Right Side View | BFS — last element of each level | New | — | — |

---

## Summary

| Pattern | Total | New | Retry | Locked |
| --- | --- | --- | --- | --- |
| Two Pointers | 7 | 3 | 4 | 0 |
| Hashmap / Set | 6 | 3 | 3 | 0 |
| Sliding Window | 6 | 4 | 2 | 0 |
| Prefix Sum | 5 | 3 | 2 | 0 |
| Kadane's | 3 | 2 | 1 | 0 |
| Binary Search | 6 | 4 | 2 | 0 |
| Monotonic Stack | 5 | 3 | 2 | 0 |
| Trees | 10 | 7 | 3 | 0 |
| **Total** | **48** | **29** | **19** | **0** |