# Key Insights — Har Problem Ki Ek Line

> Ye file code nahi hai. Har problem ke liye WO EK LINE jo yaad ho toh poora approach derive ho jaye.
> Revision mein pehle bina dekhe try kar. Agar nahi aaya toh yahan se sirf apni problem ki line padh — phir khud derive kar.

---

## Two Pointers
| Problem | Key Insight |
|---------|------------|
| Container With Most Water | Chhoti height wali side move karo — kyunki wo bottleneck hai |
| Move Zeroes | Slow pointer = next non-zero position, fast pointer scan karta hai |
| Valid Palindrome | Dono ends se compare karo, inward move karo |
| Two Sum II (Sorted) | Sum chhota hai toh left badha, bada hai toh right ghatao |
| Remove Duplicates | Slow = last unique position, fast se next unique dhundho |
| Remove Element | Slow = write position, fast se valid elements dhundho |
| 3Sum | Fix one, two pointer on rest. Sort pehle. Skip duplicates. |

## Hashmap / Set
| Problem | Key Insight |
|---------|------------|
| Valid Anagram | Dono strings ki frequency count same honi chahiye |
| Two Sum (Unsorted) | Har element pe check: target - current pehle dekha hai kya? |
| Intersection of Two Arrays | Ek ko set mein daal, dusre mein check kar |
| Contains Duplicate | Set mein daalo, agar pehle se hai toh duplicate |
| First Unique Character | Frequency count karo, pehla character jiska count 1 hai |
| Happy Number | Cycle detect karo set se — agar number repeat hua toh not happy |

## Sliding Window
| Problem | Key Insight |
|---------|------------|
| Max Average Subarray I | Fixed window slide karo — add new, remove old |
| Permutation in String | Fixed window, frequency match check karo |
| Longest Substring Without Repeating | Expand right, jab repeat aaye toh left shrink karo jab tak valid |
| Minimum Size Subarray Sum | Expand right, jab sum >= target toh left shrink karo (shortest dhundho) |
| Longest Repeating Character Replacement | Window mein max frequency track karo, window_size - max_freq <= k |
| Max Consecutive Ones III | Window mein zeros count karo, jab zeros > k toh shrink |

## Prefix Sum
| Problem | Key Insight |
|---------|------------|
| Subarray Sum Equals K | Pehle kabhi aisa prefix sum aaya tha kya jo current_sum - k ke equal ho? |
| Continuous Subarray Sum | Prefix sum ka modulo k store karo — same modulo dobara aaya toh valid subarray |
| Subarray Sums Divisible by K | Same as above — modulo repeat = divisible subarray |
| Binary Subarrays With Sum | Prefix sum count karo, current - target pehle kitni baar aaya? |
| Max Size Subarray Sum Equals K | Prefix sum store karo with EARLIEST index — current - k ka earliest index dhundho for max length |

## Kadane's
| Problem | Key Insight |
|---------|------------|
| Maximum Subarray | Har element pe: continue ya fresh start? Agar pichla sum negative toh fresh start |
| Best Time to Buy/Sell Stock | Min price track karo, har din pe profit = current - min_so_far |
| Max Sum Circular Subarray | Answer = max(normal kadane, total_sum - min_subarray_sum) |

## Binary Search
| Problem | Key Insight |
|---------|------------|
| Binary Search | Sorted mein mid check karo, half eliminate karo |
| Guess Number | Hidden space pe binary search — feedback se half eliminate |
| First Bad Version | First True dhundho — condition true toh left jao, false toh right |
| Koko Eating Bananas | Answer pe binary search — kya is speed se time mein kha payegi? |
| Capacity To Ship Packages | Answer pe binary search — kya is capacity se D din mein ship hoga? |
| Split Array Largest Sum | Answer pe binary search — kya is max sum se k parts mein split hoga? |

## Monotonic Stack
| Problem | Key Insight |
|---------|------------|
| Next Greater Element I | Stack mein chhote rakho, bada aaya toh pop karo — popped ka answer mil gaya |
| Daily Temperatures | Same as above but index difference store karo |
| Next Greater Element II | Circular = array ko 2x loop karo (i % n) |
| Largest Rectangle in Histogram | Har bar ke liye left aur right boundary dhundho using stack |
| Trapping Rain Water | Har position pe min(max_left, max_right) - height = trapped water |

## Trees (DFS)
| Problem | Key Insight |
|---------|------------|
| Max Depth | Return 1 + max(left, right). None = 0. |
| Same Tree | Dono None = True. Ek None = False. Values equal + both subtrees same. |
| Invert Binary Tree | Har node pe left aur right swap karo. Recursion baaki handle karega. |
| Diameter | Global = left + right (path through node). Return = 1 + max (height upar bhejo). |
| Balanced Binary Tree | Height return karo, -1 = invalid signal. Agar left-right diff > 1 toh -1. |
| Path Sum | Target se subtract karte jao. Leaf pe remaining == 0? |
| LCA | None/match = return self. Left aur right dono found = main LCA. Ek found = upar bhej. |
| Level Order (BFS) | Queue mein level ke nodes. len(q) = level size. Popleft + children add. |
| Validate BST | Range (lower, upper) pass karo. Left jao = upper tight. Right jao = lower tight. |
| Right Side View | Level Order ka last element = right side se dikhta hai. |
