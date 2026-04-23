# DSA Revision Rules and History

> Revision rules (scoring, retry ladder, session approach) and attempt history.  
> Current problem status (Status, Step, Next Retry) is tracked in progress.md.  
> This file contains HOW to revise and WHAT happened in past attempts.

## Scoring System

Inspired by Anki's spaced repetition grading:

| Grade | Meaning |
| --- | --- |
| Easy | Pattern + code correct, no help needed |
| Good | Approach correct, minor help on implementation |
| Hard | Major help needed on pattern or approach |
| Again | Nothing recalled, blank |

## Retry Ladder (STRICT — AI MUST FOLLOW)

Each grade has a fixed retry ladder. Steps are retry counts with increasing  
intervals. Problem is Locked ONLY when the LAST step is graded Easy.

Grade at each retry is decided FRESH — it does NOT auto-promote.  
Example: Hard problem, retry 1 gets Easy, retry 2 could still get Hard.  
Each retry is an independent test.

**Hard (5 retries before lock):**

1.  Retry next day
2.  Retry in 3 days
3.  Retry in 7 days
4.  Retry in 14 days
5.  Final — Easy = Locked

**Good (3 retries before lock):**

1.  Retry in 3 days
2.  Retry in 7 days
3.  Final at 14 days — Easy = Locked

**Easy (1 final check):**

1.  Final check after 14 days — Easy = Locked

**Again (same as Hard but starts same day):**

1.  Retry same day after review
2.  Then follows Hard ladder from step 1

**What happens if retry grade is NOT Easy at any step:**

*   Grade is Easy → move to next step in current ladder
*   Grade is Good at final step → add 1 more retry in 7 days
*   Grade is Hard at any step → reset to Hard ladder step 1
*   Grade is Again at any step → reset to Again flow (same day retry)

**Lock condition:** ONLY the LAST step graded Easy = Locked. No exceptions.

**AI RULES:**

*   ALWAYS check system date before setting retry dates
*   ALWAYS calculate retry date from today's date (system context)
*   NEVER write "Overdue" — always write actual dates
*   If calculated retry date is in the past, set retry to next session date (tomorrow or next available)
*   NEVER lock a problem unless last retry is Easy
*   ALWAYS update progress.md (Status, Step, Next Retry columns) after every problem
*   Retry date = date of current session + interval days for next step

## Session Approach

**Each session priority order:**

1.  Overdue retries first (always highest priority)
2.  Due-today retries
3.  New random problems from untested pool (48 total, test all once)
4.  Once all 48 tested at least once — start next pattern (Linked List)
5.  New pattern problems also enter revision cycle after solving

**Missed days policy:**

*   Overdue retries accumulate — this is normal, no penalty
*   Next session: do all overdue retries first
*   If 5+ overdue: only do overdue that session, skip new random
*   If 10+ overdue (long gap): max 5 overdue per session, clear backlog over multiple sessions
*   Retry dates stay as original — AI checks which dates are before today to find overdue
*   New random problems resume only after overdue backlog is cleared

## Revision Log

Full history of every attempt. Append-only — never delete rows.

| # | Date | Problem | Pattern Guess | Correct? | Attempts | Grade | Notes | Retry |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Apr 14 | Subarray Sum Equals K (LC 560) | Sliding Window | Wrong (Prefix Sum) | 3 | Hard | Missed: negative nums = no sliding window. COUNT = prefix sum. Forgot prefix sum approach entirely. | Apr 15 |
| 2 | Apr 14 | Trapping Rain Water (LC 42) | Monotonic Stack | Correct | 4 | Good | Pattern correct. Implementation issues: stack empty check, width calc, water formula. | Apr 17 |
| 3 | Apr 14 | Koko Eating Bananas (LC 875) | No guess | Wrong (Binary Search on Answer) | 5 | Hard | Didn't identify BS on Answer. Confused lo/hi (piles vs speed). for loop issues. | Apr 15 |
| 4 | Apr 15 | Subarray Sum Equals K (LC 560) — RETRY | Prefix Sum | Correct | 1 | Easy | Pattern sahi, code sahi, {0:1} reasoning clear. Big improvement from yesterday. | Apr 21 |
| 5 | Apr 15 | Koko Eating Bananas (LC 875) — RETRY | Binary Search on Answer | Correct | 1 | Easy | Pattern identified, lo/hi correct, ceil logic correct. Only minor fix: return low not mid. | Apr 21 |
| 6 | Apr 15 | Remove Duplicates from Sorted Array (LC 26) | Two Pointers (slow-fast) | Correct | 1 | Easy | Instant pattern recognition. Clean code. | Apr 29 |
| 7 | Apr 15 | Maximum Sum Circular Subarray (LC 918) | Kadane's | Correct | 3 | Good | Pattern sahi, but circular trick (total - min\_kadane) yaad nahi tha. Kadane template bhi bhool gaya. Edge case (all negative) missed twice. | Apr 18 |
| 8 | Apr 16 | Longest Substring Without Repeating (LC 3) | Sliding Window | Correct | 2 | Good | Pattern + approach sahi. Impl issues: i vs right/left, shrink logic order, del syntax. | Apr 19 |
| 9 | Apr 16 | Diameter of Binary Tree (LC 543) | Trees (DFS) | Correct | 4 | Good | Pattern + global vs return sahi. Impl: node vs root, return height not diameter, result mutable list concept. | Apr 19 |
| 10 | Apr 16 | First Bad Version (LC 278) | Binary Search | Correct | 2 | Good | Pattern sahi. Direction initially ulta (True pe right vs left). Input n vs array confusion. | Apr 19 |
| 11 | Apr 18 | Trapping Rain Water (LC 42) — RETRY | Monotonic Stack | Correct | 3 | Good | Pattern sahi. Impl issues: variable overwrite (height), stack\[-1\] vs stack\[i\], empty check, append missing, += vs =. Improving from Apr 14. | Apr 25 |
| 12 | Apr 18 | Maximum Sum Circular Subarray (LC 918) — RETRY | Kadane's | Correct | 4 | Good | Approach remembered (circular trick, edge case). Impl typos: duplicate var, wrong var name, total init, loop start. Still shaky on clean impl. | Apr 25 |
| 13 | Apr 18 | Container With Most Water (LC 11) | Two Pointers (opposite ends) | Correct | 1 | Easy | Instant pattern, clean code. Width confusion (right-left vs +1) clarified. | May 2 |
| 14 | Apr 18 | Largest Rectangle in Histogram (LC 84) | Sliding Window | Wrong (Monotonic Stack) | 4 | Good | Pattern miss — guessed sliding window. Remaining stack concept unclear initially, samjha after analogy. Variable name bug (height vs bar\_height). | Apr 21 |
| 15 | Apr 20 | Longest Substring Without Repeating (LC 3) — RETRY | Sliding Window | Correct | 1 | Easy | Pattern + code both clean. Set-based approach. | Apr 27 |
| 16 | Apr 20 | Diameter of Binary Tree (LC 543) — RETRY | Trees (DFS) | Correct | 1 | Easy | Global vs return perfect. dia=\[0\] trick remembered. | Apr 27 |
| 17 | Apr 20 | First Bad Version (LC 278) — RETRY | Binary Search | Correct | 1 | Easy | Direction correct this time. while left \< right, hi=mid. | Apr 27 |
| 18 | Apr 20 | Permutation in String (LC 567) | Sliding Window (fixed) + Hashmap | Correct | 1 | Easy | Fixed window + freq match. Clean code. | May 4 |
| 19 | Apr 20 | Balanced Binary Tree (LC 110) | Trees (DFS) | Correct | 2 | Good | \-1 signal approach sahi. Missed: propagate -1 from children before abs check. | Apr 23 |
| 20 | Apr 20 | Validate BST (LC 98) | Trees (DFS) | Correct | 3 | Easy | Range-based approach sahi. Base case (True not False), return missing, strict inequality — all structural, logic was correct. | May 4 |
| 21 | Apr 20 | Binary Subarrays With Sum (LC 930) | Sliding Window | Wrong (Prefix Sum) | 1 | Good | Pattern miss — guessed sliding window (same trap as Subarray Sum). After hint, prefix sum + hashmap approach recalled correctly. Code clean. | Apr 23 |
| 22 | Apr 21 | Subarray Sum Equals K (LC 560) — RETRY 2 | Prefix Sum | Correct | 1 | Easy | Pattern, reasoning, code all clean. {0:1} reasoning solid. Order correct (check then update). No help needed. | Apr 28 |
| 23 | Apr 21 | Koko Eating Bananas (LC 875) — RETRY 2 | Binary Search on Answer | Correct | 1 | Easy | Pattern, lo/hi, feasibility check, ceil logic, return lo — all correct. No help needed. | Apr 28 |
| 24 | Apr 21 | Largest Rectangle in Histogram (LC 84) — RETRY | Monotonic Stack | Correct | 5 | Hard | Pattern correct (stack). Width formula struggle — empty stack case, right boundary in second loop, if/else structure. Multiple fixes needed. Last time's approach (left=-1 sentinel) was cleaner but didn't recall it. | Apr 22 |
| 25 | Apr 22 | Largest Rectangle in Histogram (LC 84) — RETRY 2 | Monotonic Stack | Correct | 1 | Easy | Pattern, width formula, remaining stack handling — all clean. No help needed. Big improvement from yesterday's Hard. | Apr 29 |
| 26 | Apr 22 | Two Sum II (LC 167) | Two Pointers (opposite ends) | Correct | 1 | Easy | Pattern instant. Shrink logic correct. Only fix: tuple to list return. 1-indexed concept learned. | May 6 |
| 27 | Apr 22 | Contains Duplicate (LC 217) | Hashmap/Set (membership) | Correct | 1 | Easy | Set membership instant. Clean code. | May 6 |
| 28 | Apr 22 | Valid Palindrome (LC 125) | Two Pointers (opposite ends) | Correct | 1 | Easy | Pattern correct. Approach + invariant solid. Minor: .isalnum() recall miss, len(s)-1 off-by-one. | May 6 |
| 29 | Apr 22 | Happy Number (LC 202) | Hashmap/Set (cycle detection) | Correct | 1 | Easy | Pattern correct (set cycle detect). Minor: forgot square, forgot n=total update. Self-fixed. | May 6 |
| 30 | Apr 22 | Valid Anagram (LC 242) | Hashmap/Set (frequency count) | Correct | 1 | Easy | Two dicts, frequency compare. Clean code. | May 6 |
