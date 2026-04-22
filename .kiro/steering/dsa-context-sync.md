---
inclusion: always
---

# DSA Context Sync Rule

## Before ANY action on dsa/ files:
1. Read `dsa/CONTEXT.md` FIRST — check LIVE SESSION STATE
2. ALWAYS get today's date from SYSTEM CONTEXT (the date provided in system prompt) — NEVER from training data, NEVER from conversation history, NEVER guess
3. Compare `Last Updated` in CONTEXT.md with today's system date
4. TRUST THE FILE over your memory — files sync via git across devices

## Problem Presentation Rules (STRICT — NO EXCEPTIONS):
- **New problem:** Say ONLY the problem name + LeetCode number + problem statement. NEVER mention pattern, variant, category, or hint. User must identify the pattern themselves.
- **Retry problem:** Say ONLY the problem name + LeetCode number + "bata kya yaad hai". NEVER mention past grade, past mistakes, pattern, variant, or any hint.
- **NEVER copy pattern/variant info from progress.md into chat.** That file is for tracking, not for showing to the user.
- These rules apply even when picking a random problem — strip all metadata before presenting.

## Do NOT:
- Overwrite data from other sessions/devices
- Delete unfamiliar entries (they're from another PC)
- Assume you know file contents — always read before modifying
- Use any date other than the one from system context
