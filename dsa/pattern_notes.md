# DSA Pattern Notes

> Pattern recognition guide + common mistakes + templates in my code style.
> AI updates this after every revision attempt if there's useful data.
> Templates reflect how I actually write code, not textbook style.

---

## 1. Two Pointers

**When to use:**
- Array sorted hai (ya sort kar sakte ho)
- Pair/triplet dhundhna hai
- In-place remove/partition/deduplicate

**When NOT to use:**
- Subarray sum/count chahiye (prefix sum / sliding window)
- Unsorted + sort nahi kar sakte (hashmap)

**Common mistakes:**
- (none yet from revision)

**Template — Opposite Ends:**
(pending — will update from my code when I solve this in revision)

**Template — Same Direction (slow-fast):**
(pending — will update from my code when I solve this in revision)

---

## 2. Hashmap / Set

**When to use:**
- O(1) lookup chahiye — existence ya frequency
- Complement dhundhna (target - current)
- Count/frequency track karna

**When NOT to use:**
- Contiguous subarray chahiye (sliding window / prefix sum)
- Sorted order chahiye (two pointers / binary search)

**Common mistakes:**
- (none yet from revision)

**Template — Complement Lookup:**
(pending — will update from my code when I solve this in revision)

**Template — Frequency Count:**
(pending — will update from my code when I solve this in revision)

---

## 3. Sliding Window

**When to use:**
- Contiguous subarray/substring chahiye
- Window shrink karne se condition monotonically change hoti hai
- All positive numbers + longest/shortest subarray

**When NOT to use:**
- Negative numbers + subarray sum (prefix sum)
- COUNT of subarrays with exact sum (prefix sum)
- Non-contiguous elements (DP)

**Common mistakes:**
- (none yet from revision — but see Prefix Sum traps below)

**Variants:**
- Fixed window: size pata hai (Max Average, Permutation in String)
- Variable violation-based: expand, jab condition BREAK ho toh shrink (Longest Substring)
- Variable goal-based: expand, jab condition MEET ho toh shrink (Min Size Subarray)

**Template — Fixed Window (Permutation in String style):**
(pending — will update from my code when I solve this in revision)

**Template — Variable (violation-based, Longest Substring style):**
(pending — will update from my code when I solve this in revision)

**Template — Variable (goal-based):**
(pending — will update from my code when I solve this in revision)

---

## 4. Prefix Sum

**When to use:**
- Subarray SUM involved hai
- Negative numbers hain (sliding window nahi chalega)
- COUNT of subarrays with sum = K
- Range sum queries

**When NOT to use:**
- Problem sum ke baare mein nahi hai (hashmap / sliding window)
- Single element dhundhna (binary search / hashmap)

**TRAP — Sliding Window vs Prefix Sum:**
- "Count of subarrays with exact sum" = ALWAYS Prefix Sum, never Sliding Window
- Negative numbers = Prefix Sum (sliding window shrink predictable nahi)
- I have guessed Sliding Window for Prefix Sum problems TWICE (Subarray Sum Equals K, Binary Subarrays With Sum). This is my weakest pattern recognition area.

**Common mistakes:**
- Guessing Sliding Window when "count of subarrays with sum = X" is asked
- Forgetting {0: 1} initialization in hashmap

**Template — Count subarrays with sum = K (my style):**
```python
count = 0
freq = {0: 1}
current_sum = 0
for right in range(len(nums)):
    current_sum += nums[right]
    if current_sum - goal in freq:
        count += freq[current_sum - goal]
    freq[current_sum] = freq.get(current_sum, 0) + 1
return count
# Enhancement: "for right in range(len(nums))" can be "for num in nums" since index not used.
# Enhancement: freq.get(current_sum - goal, 0) lets you skip the "if" check — always add, 0 if not found.
```

**Template — Modulo variant (divisible by K):**
(pending — will update from my code when I solve this in revision)

---

## 5. Kadane's Algorithm

**When to use:**
- MAXIMUM or MINIMUM contiguous subarray sum
- "Best contiguous segment" type
- Buy/sell stock (min so far variant)

**When NOT to use:**
- Count chahiye (prefix sum)
- Specific sum chahiye (prefix sum)
- Non-contiguous (DP)

**Common mistakes:**
- Circular variant: forgot total - min_kadane trick
- Kadane template: forgot to start loop from index 1
- Edge case: all negative array in circular variant

**Template — Classic Kadane:**
(pending — will update from my code when I solve this in revision)

---

## 6. Binary Search

**When to use:**
- Monotonic condition (ek side True, dusri False)
- Sorted array mein search
- "Minimum/maximum value jisse condition satisfy ho"

**When NOT to use:**
- Condition monotonic nahi hai
- Subarray/substring problems (sliding window / prefix sum)

**Common mistakes:**
- Direction confusion: True pe left jaana hai ya right (First Bad Version)
- lo/hi confusion: search space kya hai — array indices vs answer range (Koko)
- Return value: return lo, not mid (boundary search)

**Template — Boundary (First True):**
(pending — will update from my code when I solve this in revision)

**Template — Binary Search on Answer:**
(pending — will update from my code when I solve this in revision)

---

## 7. Monotonic Stack

**When to use:**
- NEAREST greater/smaller element dhundhna (left ya right)
- Span/range based on nearest boundary
- Histogram area, trapping water

**When NOT to use:**
- Subarray sum (prefix sum / sliding window)
- "Nearest" concept nahi hai

**Common mistakes:**
- Histogram: guessed Sliding Window instead of Monotonic Stack
- Trapping Rain: variable overwrite (height), stack[-1] vs stack[i], empty check, append missing, += vs =
- Remaining stack processing: after loop ends, stack mein jo bacha uska bhi answer nikalna hai

**Template — Next Greater (left to right):**
(pending — will update from my code when I solve this in revision)

**Template — Histogram (left + right boundaries):**
(pending — will update from my code when I solve this in revision)

---

## 8. Trees (DFS)

**When to use:**
- Tree structure hai
- Problem ko subtree problems mein tod sakte ho
- Har node ka answer children ke answers se banta hai

**When NOT to use:**
- Level-by-level traverse (BFS with queue)
- Shortest path (BFS)
- Graph with cycles (graph BFS/DFS with visited)

**Common mistakes:**
- Balanced Binary Tree: -1 propagation miss — pehle children se -1 check karo, THEN abs(left - right) check
- Validate BST: base case return True (not False) — empty tree is valid BST
- Validate BST: strict inequality (lower < val < upper), not <=
- Diameter: global vs return confusion — diameter is global (left + right), height is return (1 + max)
- result = [0] trick for mutable global in nested function

**Key thinking:**
- "Har node ek mini problem hai"
- "Return value ka meaning fix karo pehle"
- "Global vs return — kya node ka answer hai vs kya upar bhejne ke liye hai"

**Template — Simple return (height):**
(pending — will update from my code when I solve this in revision)

**Template — Global + return (diameter):**
(pending — will update from my code when I solve this in revision)

**Template — Boolean check with -1 signal (balanced tree):**
(pending — will update from my code when I solve this in revision)

**Template — Range validation (Validate BST, my style):**
```python
def solve(root, lower, upper):
    if not root:
        return True
    if lower < root.val < upper:
        left = solve(root.left, lower, root.val)
        right = solve(root.right, root.val, upper)
    else:
        return False
    return left and right
# Enhancement: "return left and right" can short-circuit — if left is False, right won't even be called.
# Enhancement: can combine into one return: "return solve(root.left, lower, root.val) and solve(root.right, root.val, upper)"
# This skips the left/right variables entirely. Cleaner but same logic.
```

---

## Pattern Selection Flowchart

```
Problem aaya:

1. Tree/Graph structure?
   Tree: DFS (recursion, bottom-up)
   Graph: BFS/DFS (with visited set)

2. Array/String?
   Sorted?
     Element dhundhna: Binary Search
     Pair/triplet: Two Pointers

   Subarray/Substring?
     COUNT of subarrays with exact sum: Prefix Sum (NEVER sliding window)
     Sum + negative numbers: Prefix Sum
     Sum + all positive + longest/shortest: Sliding Window
     Maximum/Minimum sum: Kadane's
     Next greater/smaller: Monotonic Stack

   Existence/Count/Frequency?
     Hashmap / Set

3. "Minimum X that satisfies condition"?
   Binary Search on Answer
```