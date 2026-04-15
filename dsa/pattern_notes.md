# DSA Pattern Recognition Guide

> Ye file pattern RECOGNITION ke liye hai — problem dekh ke turant pehchaan: konsa pattern lagega, kyun lagega.
> Revision mein tu apna reasoning likhega. Ye file tera reference hai.

---

## 1. Two Pointers

**Analogy:** Do log ek rope ke dono ends pe khade hain aur ek dusre ki taraf chal rahe hain. Ya dono ek hi side se chal rahe hain — ek slow, ek fast.

**MUST HAVE (ye nahi toh Two Pointers nahi):**
- Array SORTED hona chahiye (ya sort kar sakte ho). Unsorted pe two pointers kaam nahi karta kyunki movement ka logic sorted order pe depend karta hai.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- Do elements ka relationship check karna hai (sum, compare, match)
- In-place kuch karna hai bina extra space ke (remove, partition, deduplicate)
- "Pair dhundho" type problems

**Bilkul use NAHI kar sakte jab:**
- Subarray/substring ka sum ya count chahiye (→ sliding window ya prefix sum)
- Order matter nahi karta, sirf existence check hai (→ hashmap/set)
- Data unsorted hai aur sort karna allowed nahi ya sort karne se answer change hoga

**Signal words:** "sorted array", "pair", "in-place", "remove duplicates", "two sum (sorted)", "palindrome"

**Variants:**
- Opposite ends (shrink inward): Container With Most Water, Two Sum II, 3Sum
- Same direction (slow-fast): Move Zeroes, Remove Duplicates, Remove Element

**Template — Opposite Ends:**
```python
def two_pointer_opposite(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]  # ya koi aur calculation
        if current == target:
            return [left, right]
        elif current < target:
            left += 1      # chhota hai, left badha
        else:
            right -= 1     # bada hai, right ghatao
    return []
```

**Template — Same Direction (slow-fast / partition):**
```python
def two_pointer_same(arr):
    slow = 0  # slow = write position / boundary
    for fast in range(len(arr)):
        if condition(arr[fast]):  # ye element rakhna hai?
            arr[slow] = arr[fast]
            slow += 1
    return slow  # slow = new length / boundary
```

---

## 2. Hashmap / Set

**Analogy:** Ek register/diary jisme tu cheezein note karta hai taaki baad mein turant dhundh sake. "Ye pehle dekha tha kya?" — diary khol, check kar, O(1) mein answer.

**MUST HAVE (ye nahi toh Hashmap/Set nahi):**
- Tujhe kisi element ki EXISTENCE ya FREQUENCY instantly check karni hai (O(1) lookup chahiye). Agar lookup ki zaroorat nahi toh hashmap overkill hai.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- Complement dhundhna hai (target - current = kya chahiye?)
- Frequency/count chahiye (kitni baar aaya?)
- Order matter nahi karta, sirf presence/count matters

**Bilkul use NAHI kar sakte jab:**
- Contiguous subarray chahiye (→ sliding window, prefix sum)
- Sorted order mein kuch karna hai (→ two pointers, binary search)
- Space O(1) constraint hai (hashmap = O(n) space hamesha lega)

**Signal words:** "frequency", "count", "duplicate", "unique", "anagram", "complement", "two sum (unsorted)"

**Template — Complement Lookup (Two Sum style):**
```python
def complement_lookup(arr, target):
    seen = {}  # value → index
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Template — Frequency Count:**
```python
from collections import Counter
def frequency_check(s):
    freq = Counter(s)  # ya manually: freq = {}; freq[c] = freq.get(c, 0) + 1
    for char, count in freq.items():
        if count == 1:  # ya koi aur condition
            return char
    return None
```

---

## 3. Sliding Window

**Analogy:** Train ki window se bahar dekh raha hai. Window fixed size ki hai ya adjust hoti hai. Jab tak view accha hai window rakh, jab view kharab ho (condition break) toh window shrink kar ya aage badha.

**MUST HAVE (ye nahi toh Sliding Window nahi):**
- CONTIGUOUS subarray/substring chahiye AND window shrink karne se condition monotonically change hoti hai (matlab shrink karne se cheezein "better" ya "worse" hoti hain predictably). Negative numbers mein ye guarantee nahi hoti — shrink kiya toh sum badh bhi sakta hai, isliye window kaam nahi karta.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- Koi condition maintain karni hai window ke andar (sum, unique count, frequency)
- "Longest/shortest subarray with condition X"
- Array mein sab positive numbers hain (strongest signal)

**Bilkul use NAHI kar sakte jab:**
- Negative numbers hain aur subarray sum chahiye (→ prefix sum — shrink karne se sum predictably decrease nahi hoga)
- Non-contiguous elements chahiye (→ DP, hashmap)
- Exact count of subarrays chahiye (→ prefix sum)

**Signal words:** "contiguous", "substring", "subarray", "window", "longest", "shortest", "at most K", "maximum/minimum length"

**Variants:**
- Fixed window: size pata hai (Maximum Average Subarray, Permutation in String)
- Variable — violation-based: expand karo, jab condition BREAK ho toh shrink
- Variable — goal-based: expand karo, jab condition MEET ho toh shrink for optimization

**Template — Fixed Window:**
```python
def fixed_window(arr, k):
    # Build first window
    window_sum = sum(arr[:k])
    best = window_sum
    # Slide
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # add new, remove old
        best = max(best, window_sum)
    return best
```

**Template — Variable Window (violation-based — longest valid):**
```python
def variable_window_violation(s):
    left = 0
    window = {}  # ya set — track window state
    best = 0
    for right in range(len(s)):
        # Expand: add s[right] to window
        window[s[right]] = window.get(s[right], 0) + 1
        # Shrink: jab tak condition VIOLATED hai
        while condition_violated(window):
            # Remove s[left] from window
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        # Window valid hai — update answer
        best = max(best, right - left + 1)
    return best
```

**Template — Variable Window (goal-based — shortest valid):**
```python
def variable_window_goal(arr, target):
    left = 0
    current_sum = 0
    best = float('inf')
    for right in range(len(arr)):
        current_sum += arr[right]  # expand
        # Shrink: jab tak goal MET hai
        while current_sum >= target:
            best = min(best, right - left + 1)
            current_sum -= arr[left]
            left += 1
    return best if best != float('inf') else 0
```

---

## 4. Prefix Sum

**Analogy:** Tu har din ka kharcha note karta hai. Prefix sum = running total. "Day 3 se Day 7 tak kitna kharcha hua?" — Day 7 ka total minus Day 2 ka total. Seedha answer, koi loop nahi.

**MUST HAVE (ye nahi toh Prefix Sum nahi):**
- Subarray SUM involved hai. Agar problem sum ke baare mein nahi hai (unique elements, longest without repeating, etc.) toh prefix sum kaam nahi aayega.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- Negative numbers hain (sliding window nahi chalega, prefix sum chahiye)
- "Kitne subarrays hain jinki sum = K?" type counting
- Range sum queries (L to R ka sum baar baar)

**Bilkul use NAHI kar sakte jab:**
- Problem sum ke baare mein nahi hai — unique elements, longest substring, frequency (→ sliding window, hashmap)
- Single element dhundhna hai (→ binary search, hashmap)
- Contiguous subarray nahi chahiye (→ DP)

**Signal words:** "subarray sum", "sum equals K", "divisible by K", "number of subarrays", "range sum"

**Sliding Window vs Prefix Sum — THE KEY DISTINCTION:**
- Sab positive + contiguous + longest/shortest → Sliding Window
- Negative numbers + subarray sum + count → Prefix Sum
- Dono contiguous subarrays ke liye hain, but negative numbers sliding window tod dete hain

**Template — Count subarrays with sum = K:**
```python
def subarray_sum_count(arr, k):
    prefix = 0
    count = 0
    seen = {0: 1}  # prefix_sum → kitni baar dekha
    for num in arr:
        prefix += num
        complement = prefix - k
        if complement in seen:
            count += seen[complement]
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

**Template — Modulo variant (divisible by K):**
```python
def subarray_divisible(arr, k):
    prefix = 0
    count = 0
    seen = {0: 1}
    for num in arr:
        prefix = (prefix + num) % k
        if prefix < 0:
            prefix += k  # handle negative modulo
        if prefix in seen:
            count += seen[prefix]
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

---

## 5. Kadane's Algorithm

**Analogy:** Tu road pe chal raha hai, har step pe paisa milta ya khota hai. Kadane = "kya mujhe pichle path ke saath continue karna chahiye ya fresh start karna chahiye?" Har step pe ye decision. Agar pichla path negative hai toh fresh start better.

**MUST HAVE (ye nahi toh Kadane nahi):**
- MAXIMUM ya MINIMUM contiguous subarray sum chahiye. Agar max/min nahi chahiye (count chahiye, specific sum chahiye) toh Kadane kaam nahi aayega.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- "Best contiguous segment" type problem
- Buy/sell stock (min so far track karo, max profit update karo — Kadane variant)

**Bilkul use NAHI kar sakte jab:**
- Count chahiye (kitne subarrays?) → prefix sum
- Specific sum chahiye (sum = K) → prefix sum
- Non-contiguous elements → DP

**Signal words:** "maximum subarray", "best time to buy/sell", "maximum sum", "contiguous"

**Kadane vs Prefix Sum:**
- Sirf MAX/MIN subarray sum → Kadane (O(1) space)
- Count of subarrays with sum = K → Prefix Sum + Hashmap
- Kadane is basically a special case optimization

**Template — Classic Kadane:**
```python
def max_subarray(arr):
    current = arr[0]
    best = arr[0]
    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])  # fresh start ya continue?
        best = max(best, current)
    return best
```

**Template — Kadane Variant (Best Time to Buy/Sell):**
```python
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit
```

---

## 6. Binary Search

**Analogy:** Dictionary mein word dhundhna. Beech mein kholo — word pehle hai ya baad mein? Half eliminate karo. Repeat. But ye sirf sorted dictionary pe kaam karta hai.

**MUST HAVE (ye nahi toh Binary Search nahi):**
- MONOTONIC condition honi chahiye — matlab ek side sab True hai, dusri side sab False. Agar aisa clear boundary nahi hai toh half eliminate nahi kar sakte, binary search lagega nahi.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- Array sorted hai
- "Minimum/maximum value jisse condition satisfy ho"
- Search space bahut bada hai, O(n) slow hoga, O(log n) chahiye

**Bilkul use NAHI kar sakte jab:**
- Condition monotonic nahi hai (kabhi True kabhi False randomly — half eliminate nahi ho sakta)
- Subarray/substring problems (→ sliding window, prefix sum)
- Unsorted data + sort karna allowed nahi (→ hashmap)

**Signal words:** "sorted", "search", "minimum/maximum that satisfies", "koko eating bananas type", "capacity", "split array"

**Variants:**
- Exact match: element dhundho (classic binary search)
- Boundary: pehla/aakhri position dhundho (First Bad Version)
- Binary Search on Answer: answer space pe search karo, feasibility check karo

**Template — Exact Match:**
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Template — Boundary (First True / Leftmost):**
```python
def first_true(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):  # feasible hai?
            hi = mid         # answer ho sakta hai, left mein aur dekho
        else:
            lo = mid + 1     # nahi hai, right jao
    return lo  # smallest value where condition is True
```

**Template — Binary Search on Answer:**
```python
def search_on_answer(arr, constraint):
    lo, hi = min_possible, max_possible
    while lo < hi:
        mid = (lo + hi) // 2
        if is_feasible(arr, mid, constraint):
            hi = mid         # feasible hai, kya aur chhota chalega?
        else:
            lo = mid + 1     # nahi chala, bada try karo
    return lo

def is_feasible(arr, candidate, constraint):
    # Check: kya 'candidate' answer se kaam chal jayega?
    # Return True/False
    pass
```

---

## 7. Monotonic Stack

**Analogy:** Tu ek line mein khada hai. Tujhe dekhna hai ki tere aage pehla lamba aadmi kaun hai. Chhote log skip ho jaate hain — sirf lamba milne pe ruk. Stack mein sirf "useful" log rehte hain, baaki pop ho jaate hain.

**MUST HAVE (ye nahi toh Monotonic Stack nahi):**
- Har element ke liye NEAREST greater/smaller element dhundhna hai (left ya right mein). Agar "nearest" nahi chahiye, sirf "any" ya "all" chahiye, toh monotonic stack overkill hai.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- "Next greater element", "next smaller element"
- Span/range based on nearest boundary
- Histogram area, trapping water

**Bilkul use NAHI kar sakte jab:**
- Subarray sum chahiye (→ prefix sum, sliding window)
- Sorted order mein search chahiye (→ binary search)
- "Nearest" concept nahi hai — sirf general comparison (→ brute force, sorting)

**Signal words:** "next greater", "next smaller", "span", "histogram", "trapping water", "temperatures", "stock span"

**Core invariant:** Stack hamesha monotonic rehta hai (increasing ya decreasing). Jab naya element aaye jo invariant tode, tab pop karo aur popped elements ka answer mil gaya.

**Template — Next Greater Element (right to left, decreasing stack):**
```python
def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # indices store karo
    for i in range(n - 1, -1, -1):
        # Pop: stack top chhota hai current se → useless
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        # Stack top = next greater element
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result
```

**Template — Next Greater (left to right, popping = answer found):**
```python
def next_greater_v2(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        # Jab tak current > stack top → stack top ka answer mil gaya
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
```

**Template — Histogram / Span (left + right boundaries):**
```python
def largest_rectangle(heights):
    n = len(heights)
    stack = []
    max_area = 0
    for i in range(n + 1):
        curr_h = heights[i] if i < n else 0
        while stack and curr_h < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
```

---

## 8. Trees (DFS)

**Analogy:** Family tree. Har person (node) ke children hain. Koi bhi question pucho — "family mein sabse zyada generations kitni hain?" — tu neeche se upar answer build karega. Pehle leaves se pucho, phir unke parents se, phir upar. Ye bottom-up recursion hai.

**MUST HAVE (ye nahi toh Tree DFS nahi):**
- Tree structure hai AND problem ko subtree problems mein tod sakte ho (har node ka answer uske children ke answers se ban sakta hai). Agar node ka answer children se independently nahi ban sakta, toh simple DFS kaam nahi karega.

**Bonus signals (MUST HAVE ke baad ye confirm karte hain):**
- "Height", "depth", "path", "subtree", "balanced", "diameter"
- Bottom-up build karna hai (leaves se root tak)

**Bilkul use NAHI kar sakte jab:**
- Level-by-level traverse karna hai (→ BFS with queue)
- Shortest path chahiye tree/graph mein (→ BFS)
- Graph hai tree nahi — cycles hain (→ graph BFS/DFS with visited set)

**Signal words:** "binary tree", "depth", "height", "path", "subtree", "root to leaf", "balanced", "diameter"

**Key thinking:**
- "Har node ek mini problem hai"
- "Return value ka meaning fix karo pehle"
- "Global vs return — kya node ka answer hai vs kya upar bhejne ke liye hai"
- Height = return value (upar bhejo). Diameter = global (node ka answer, upar nahi jaata).

**Template — Simple return (height, depth, same tree):**
```python
def dfs(node):
    if not node:
        return 0  # base case — empty node
    left = dfs(node.left)
    right = dfs(node.right)
    return 1 + max(left, right)  # combine — meaning fix hai: height
```

**Template — Global + return (diameter, longest path):**
```python
def solve(root):
    result = [0]  # global variable — node ka answer store karo
    
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        # Update global — ye node ka answer hai (upar nahi jaata)
        result[0] = max(result[0], left + right)
        # Return — ye upar bhejne ke liye hai (height)
        return 1 + max(left, right)
    
    dfs(root)
    return result[0]
```

**Template — Boolean check (same tree, symmetric, balanced):**
```python
def dfs(node):
    if not node:
        return 0  # ya True/valid base
    left = dfs(node.left)
    right = dfs(node.right)
    # Check: kya ye node VALID hai?
    if not valid(left, right):  # condition break
        return -1  # signal: invalid
    return 1 + max(left, right)  # valid: return height
```

---

## 🔀 Pattern Selection Flowchart

```
Problem aaya →

1. Tree/Graph structure hai?
   → Tree: DFS (recursion, bottom-up)
   → Graph: BFS/DFS (with visited set)

2. Array/String hai?
   → Sorted hai?
      → Element dhundhna: Binary Search
      → Pair/triplet: Two Pointers
   
   → Subarray/Substring chahiye?
      → Sum related + negative numbers: Prefix Sum
      → Sum related + all positive + longest/shortest: Sliding Window
      → Maximum/Minimum sum: Kadane's
      → Next greater/smaller: Monotonic Stack
   
   → Existence/Count/Frequency?
      → Hashmap / Set

3. "Minimum X that satisfies condition"?
   → Binary Search on Answer
```

---

## ✍️ Revision Template

When revising a problem, write this:

```
Problem: [name]
My pattern guess: [pattern]
Why this pattern: [1-2 lines reasoning]
Edge case / trap: [kya galat ho sakta hai ya kahan phasa tha pehle]
Invariant: [what must always be true]
Approach in 3 lines: [skeleton]
```

This is what builds REAL pattern recognition — not solving, but REASONING about why.
"Edge case / trap" forces you to think about WHERE things break — that's where real learning happens.
