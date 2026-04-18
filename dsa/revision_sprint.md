ha# Revision Sprint — April 2026

> Random problems from all 48 solved. Pattern NOT given. Goal: identify pattern + solve independently.

## Scoring
| Score | Meaning | Next Action |
|-------|---------|-------------|
| ✅ Solo | Pattern + code sahi, no help | Locked — done |
| ⚠️ Hint | Needed hint on pattern/approach, code khud | Retry in 3 days |
| ❌ Guided | Major help needed | Retry next day |
| 🔴 Blank | Nothing recalled | Retry same day after review |

## Sprint Log

| # | Date | Problem | My Pattern Guess | Correct? | Attempts | Score | Notes | Retry Date |
|---|------|---------|-----------------|----------|----------|-------|-------|------------|
| 1 | Apr 14 | Subarray Sum Equals K (LC 560) | Sliding Window | ❌ Wrong (Prefix Sum) | 3 | ❌ Guided | Missed: negative nums = no sliding window. COUNT = prefix sum. Forgot prefix sum approach entirely. | Apr 15 |
| 2 | Apr 14 | Trapping Rain Water (LC 42) | Monotonic Stack | ✅ Correct | 4 | ⚠️ Hint | Pattern correct. Implementation issues: stack empty check, width calc, water formula. | Apr 17 |
| 3 | Apr 14 | Koko Eating Bananas (LC 875) | No guess | ❌ Wrong (Binary Search on Answer) | 5 | ❌ Guided | Didn't identify BS on Answer. Confused lo/hi (piles vs speed). for loop issues. | Apr 15 |
| 4 | Apr 15 | Subarray Sum Equals K (LC 560) — RETRY | Prefix Sum | ✅ Correct | 1 | ✅ Solo | Pattern sahi, code sahi, {0:1} reasoning clear. Big improvement from yesterday. | — |
| 5 | Apr 15 | Koko Eating Bananas (LC 875) — RETRY | Binary Search on Answer | ✅ Correct | 1 | ✅ Solo | Pattern identified, lo/hi correct, ceil logic correct. Only minor fix: return low not mid. | — |
| 6 | Apr 15 | Remove Duplicates from Sorted Array (LC 26) | Two Pointers (slow-fast) | ✅ Correct | 1 | ✅ Solo | Instant pattern recognition. Clean code. Redundant fast=0 init, minor. | — |
| 7 | Apr 15 | Maximum Sum Circular Subarray (LC 918) | Kadane's | ✅ Correct | 3 | ⚠️ Hint | Pattern sahi, but circular trick (total - min_kadane) yaad nahi tha. Kadane template bhi bhool gaya. Edge case (all negative) missed twice. | Apr 18 |
| 8 | Apr 16 | Longest Substring Without Repeating (LC 3) | Sliding Window | ✅ Correct | 2 | ⚠️ Hint | Pattern + approach sahi. Impl issues: i vs right/left, shrink logic order, del syntax. | Apr 19 |
| 9 | Apr 16 | Diameter of Binary Tree (LC 543) | Trees (DFS) | ✅ Correct | 4 | ⚠️ Hint | Pattern + global vs return sahi. Impl: node vs root, return height not diameter, result mutable list concept. | Apr 19 |
| 10 | Apr 16 | First Bad Version (LC 278) | Binary Search | ✅ Correct | 2 | ⚠️ Hint | Pattern sahi. Direction initially ulta (True pe right vs left). Input n vs array confusion. | Apr 19 |
| 11 | Apr 18 | Trapping Rain Water (LC 42) — RETRY | Monotonic Stack | ✅ Correct | 3 | ⚠️ Hint | Pattern sahi. Impl issues: variable overwrite (height), stack[-1] vs stack[i], empty check, append missing, += vs =. Improving from Apr 14. | Apr 21 |
| 12 | Apr 18 | Maximum Sum Circular Subarray (LC 918) — RETRY | Kadane's | ✅ Correct | 4 | ⚠️ Hint | Approach remembered (circular trick, edge case). Impl typos: duplicate var, wrong var name, total init, loop start. Still shaky on clean impl. | Apr 21 |
| 13 | Apr 18 | Container With Most Water (LC 11) | Two Pointers (opposite ends) | ✅ Correct | 1 | ✅ Solo | Instant pattern, clean code. Width confusion (right-left vs +1) clarified. | — |
| 14 | Apr 18 | Largest Rectangle in Histogram (LC 84) | Sliding Window | ❌ Wrong (Monotonic Stack) | 4 | ⚠️ Hint | Pattern miss — guessed sliding window. Remaining stack concept unclear initially, samjha after analogy. Variable name bug (height vs bar_height). | Apr 21 |
