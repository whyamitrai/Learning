# DSA Revision System

## 🧠 Why This Exists
Solve karo, aage badho, 2 hafte baad — blank. Normal hai.
Fix: **Spaced Repetition** — increasing intervals pe revisit karo, short-term se permanent memory mein shift hoga.

## 📅 Revision Cycle

After solving any problem, it enters this cycle:

| Review | When | What to do |
|--------|------|------------|
| R1 | Next day | Invariant + approach explain kar bina dekhe. No code. |
| R2 | Day 3 | Skeleton from memory. Dry run in head. |
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
