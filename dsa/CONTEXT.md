# DSA Learning Context — Amit Rai

> **AI INSTRUCTIONS:** This is the SINGLE SOURCE OF TRUTH for session restore.
> 1. Read this file FIRST
> 2. Then read: progress.md, revision.md, pattern_notes.md
> 3. Compare current date with "Last Updated" in LIVE SESSION STATE — is this same day or new day?
> 4. Resume from "LIVE SESSION STATE" section below
> 5. Follow ALL rules in this file strictly — no exceptions
> 6. **CRITICAL: EVERY TIME you update this file — check current date from system context FIRST. Never assume date. Always verify.**

---

## 📡 LIVE SESSION STATE
> **UPDATE THIS SECTION AFTER EVERY SESSION / PROBLEM**
> This is what makes cross-device sync work. Push after every session.

```
Last Updated    : 2026-04-15
Current Pattern : REVISION SPRINT
Current Problem : Sprint Day 2. Retries done — both ✅ Solo.
Problem Status  : Sprint in progress
Problems Solved : 48
Next Step       : More random problems from sprint. Continue revision sprint.
Waiting For     : Next problem
Notes           : Subarray Sum retry ✅ Solo (pattern + code correct, {0:1} reasoning clear). Koko retry ✅ Solo (BS on Answer identified, minor return fix). Both weak areas from yesterday now solid.
```

## 📅 Session Log
> Track what happened each day. Helps AI know if same day or next day, and if we're on track.

| Date | What Happened | New Problems | Revision Done | Notes |
|------|--------------|-------------|---------------|-------|
| Apr 10 | Path Sum + LCA solved | 2 (Path Sum, LCA) | — | First time solving LCA, 4 combine cases learned |
| Apr 11 | Level Order Traversal solved | 1 (Level Order) | — | First BFS problem, learned queue/deque |
| Apr 12 | Revision + Validate BST | 1 (Validate BST) | Path Sum ✅, LCA ❌→✅, Level Order ✅ | LCA base case weak, fixed. BST — new concept |
| Apr 13 | Revision + BST + Right Side View | 2 (BST, Right Side View) | LCA revised ❌→✅ | Trees pattern COMPLETE (10 problems). |
| Apr 14 | Revision Sprint Day 1 | 0 new | 3 revised: Subarray Sum ❌, Trapping Rain ⚠️, Koko ❌ | Prefix Sum + BS on Answer weak. Reading files rest of day. |
| Apr 15 | Revision Sprint Day 2 — Retries | 0 new | 2 retries: Subarray Sum ✅ Solo, Koko ✅ Solo | Both weak areas from yesterday now solid. Pattern recognition improving. |

---

## 🎯 Goal
- Master DSA patterns, NOT memorize problems
- Build strong intuition — solve unseen problems by recognizing patterns
- Think in terms of subproblems and invariants
- Target: 80-100 problems covering all major patterns

## 👨‍💻 Background
- Comfortable in Python
- Beginner in DSA (started Jan 2025)
- Weak in recursion (improving — currently doing Trees)
- Working professional, limited time — quality over quantity

## 🧠 Learning Style (STRICT)
- Explain in Hinglish
- Focus on intuition + invariant + reasoning
- Avoid bookish definitions
- Use simple examples
- Break concepts into small steps
- DO NOT jump directly to code

## 🔥 Core Rule (STRICT FLOW)
Every problem MUST follow this order:
1. **Intuition** — what is the problem really asking? why this pattern?
2. **Invariant** — what must always be true?
3. **What breaks** — when does the invariant fail?
4. **Skeleton** — pseudocode / structure (no full code yet)
5. **My explanation** — I explain my approach back
6. **My code** — I write the code
7. **Your review** — you review, point out issues

NO skipping steps. Ever.

## 🛠 Debug Rules
If my code is wrong:
1. Identify which invariant broke
2. Explain WHY it broke
3. Give a small failing example
4. Let me fix it
5. **DO NOT rewrite code directly. NEVER give me the full solution.**
6. **When my logic is correct but has typos/style issues — point them out, let ME fix and write the final clean code. DO NOT write the clean version for me. EVER.**

## ⚠️ Behavior Rules
- Never give full solution directly
- Always guide step-by-step
- Focus on thinking, not coding
- Push me if I'm vague
- Correct me bluntly if wrong — say "This is wrong because..."
- After every problem: update progress.md, revision.md, and LIVE SESSION STATE above

## 🧠 Key Insights I've Built So Far
- "Har node ek mini problem hai"
- "Return value ka meaning fix hona chahiye"
- "Height = best downward path"
- "Diameter = path through node"
- "Recursion = bottom-up build"
- Tree = recursive structure, every node = subtree root
- Difference between: height vs diameter, return vs global, node vs node's answer

## 🗺️ Upcoming Plan
Trees progression after Balanced Binary Tree:
- Path Sum
- Lowest Common Ancestor
- Binary Tree Level Order Traversal (BFS intro)
- Advanced DFS patterns

After Trees:
- Linked List
- Stack/Queue (beyond monotonic)
- Heap / Priority Queue
- Graphs (BFS/DFS)
- Dynamic Programming
- Backtracking

## 📂 File Structure
```
dsa/
├── CONTEXT.md       ← THIS FILE. Session state + all rules. Read FIRST.
├── progress.md      ← All solved problems by pattern with dates
├── revision.md      ← Spaced repetition tracker (R1-R5 cycle)
└── pattern_notes.md ← Pattern recognition: analogy + MUST HAVE + templates

career/genai_learning/
├── 00_career_strategy.md       ← Where to apply, messages, daily routine
├── 01_genai_foundations.md      ← LLM, tokens, embeddings, prompting
├── 02_langchain_and_orchestration.md ← LangChain, RAG, agents, vector DBs
├── 03_ml_fundamentals.md       ← ML basics — zero se, beginner-friendly
├── 04_system_design_and_interviews.md ← System design, STAR answers, negotiation
├── 05_github_project_plan.md   ← Projects to build for GitHub
├── 06_docker.md                ← Docker — zero se samajh
├── 07_terraform.md             ← Terraform — zero se samajh
├── 08_cicd.md                  ← CI/CD — zero se (Docker + Terraform pehle padh)
├── flashcards.md               ← Active recall cards (GenAI + ML + interviews)
└── my_understanding.md         ← Personal doubts & answers

Reading order for DevOps: 06 (Docker) → 07 (Terraform) → 08 (CI/CD)
```

## 🎯 Two-Phase Plan
**Phase 1 (Next 2 months): Get 10-12L offer**
- DSA: Finish trees → graphs → basic DP → heap → target 80-100 problems
- GenAI + ML: Flashcard review daily (10 cards/day) — covers Files 01, 02, 03, 04
- ML concepts at CONCEPT level (explain transformers, overfitting, evaluation — not hands-on)
- Interview: STAR stories ready (File 04), salary negotiation script ready
- GitHub: Build at least Project 1 (RAG chatbot) from File 05
- Apply: 2-3 targeted applications/day using process in File 00

**Phase 2 (1 year): FAANG-ready**
- DSA: 150+ problems, medium-hard comfort, DP + graphs advanced
- ML: Hands-on with PyTorch/scikit-learn, fine-tuning practice
- System design: Practice designing at scale
- Projects: All 3 GitHub projects done

## 📊 Tracking Rules
- After every problem: update progress.md with date
- After every problem: update revision.md with R1-R5 schedule
- After every session: update LIVE SESSION STATE at top of this file
- At end of a pattern: show full updated summary
- **CROSS-DEVICE WORKFLOW:** Update files → git push → other laptop → git pull → tell AI "read dsa/CONTEXT.md" → continue

## 🔄 How To Resume On Any Device
1. `git pull`
2. Open chat with AI
3. Say: "read dsa/CONTEXT.md and continue from where we left off"
4. AI reads LIVE SESSION STATE → knows exactly where you are
5. Continue solving
6. When done: AI updates files → you `git push`
