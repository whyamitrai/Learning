# DSA Learning Context — Amit Rai

> **AI INSTRUCTIONS:** This is the SINGLE SOURCE OF TRUTH for session restore.
> 1. Read this file FIRST
> 2. Then read: progress.md, revision.md, pattern_notes.md
> 3. Resume from "LIVE SESSION STATE" section below
> 4. Follow ALL rules in this file strictly — no exceptions

---

## 📡 LIVE SESSION STATE
> **UPDATE THIS SECTION AFTER EVERY SESSION / PROBLEM**
> This is what makes cross-device sync work. Push after every session.

```
Last Updated    : 2025-04-10
Current Pattern : Trees (DFS)
Current Problem : Path Sum — DONE. Next: Lowest Common Ancestor
Problem Status  : ✅ Solved
Problems Solved : 44
Next Step       : Start Lowest Common Ancestor
Waiting For     : Session start — ready for LCA
Notes           : Path Sum solved. Key learning: remaining subtract PEHLE karo, phir leaf check, phir recurse. Argument mein pass karna cleaner than mutable state. return left or right — clean combine.
```

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
