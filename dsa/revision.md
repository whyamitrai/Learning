# DSA Revision System

## 🧠 Why This Exists
Solve karo, aage badho, 2 hafte baad — blank. Normal hai.
Fix: **Spaced Repetition** — increasing intervals pe revisit karo, short-term se permanent memory mein shift hoga.

## 📅 Revision Cycle

After solving any problem, it enters this cycle:

| Review | When | What to do |
|--------|------|------------|
| R1 | Next day | Invariant + approach explain kar bina dekhe. Skeleton + code from memory. |
| R2 | Day 3 | Full code from scratch. Dry run in head. |
| R3 | Day 7 | Solve from scratch. Time yourself. |
| R4 | Day 14 | Solve again. Clean → Locked ✅. Struggle → Reset to R1. |
| R5 | Day 30 | Final dry run. Clean → Permanently Locked 🔒 |

## 🏷️ Status Tags
- 🔴 **Weak** — couldn't recall approach, needs immediate re-solve
- 🟡 **Shaky** — remembered idea but messed up implementation
- 🟢 **Solid** — solved cleanly on revision
- 🔒 **Locked** — passed R4/R5, permanently done

## 📋 Revision Queue

| # | Problem | Pattern | Solved On | R1 | R2 | R3 | R4 | R5 | Status |
|---|---------|---------|-----------|----|----|----|----|----|----|
| 1 | Balanced Binary Tree | Trees (DFS) — Boolean check (-1 signal) | 2025-04-07 | Apr 8 | Apr 10 | Apr 14 | Apr 21 | May 7 | 🔴 |
| 2 | Path Sum | Trees (DFS) — Root-to-leaf sum check | 2025-04-10 | Apr 11 | Apr 13 | Apr 17 | Apr 24 | May 10 | 🔴 |
| 3 | Lowest Common Ancestor | Trees (DFS) — LCA via left/right signals | 2025-04-10 | Apr 11 | Apr 13 | Apr 17 | Apr 24 | May 10 | 🔴 |
| 4 | Binary Tree Level Order Traversal | Trees (BFS) — Queue, level grouping | 2025-04-11 | Apr 12 | Apr 14 | Apr 18 | Apr 25 | May 11 | 🔴 |
| 5 | Validate BST | Trees (DFS) — Range (lower, upper) pass | 2026-04-13 | Apr 14 | Apr 16 | Apr 20 | Apr 27 | May 13 | 🔴 |

*(New problems get added here as we solve them)*

## 🔄 Daily Routine

**Before starting a new problem:**
1. Check this table — do any reviews due today
2. For each: explain invariant → write skeleton → code if needed
3. Update the table with ✅ or ❌ for that review column
4. If ❌ on any review → reset back to R1

**Weekend (30 min):**
- Scan 5 older problems — just invariant + skeleton in head
- Anything fuzzy → add back to queue

## 💡 Rules
- Don't re-read code. Explain the WHY.
- If you can teach it, you know it.
- Goal isn't "I remember the code" — it's "I can derive the solution from the pattern."
