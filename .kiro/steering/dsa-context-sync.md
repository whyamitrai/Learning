---
inclusion: always
---

# DSA Context Sync Rule

## Before ANY action on dsa/ files:
1. Read `dsa/CONTEXT.md` FIRST — check LIVE SESSION STATE
2. ALWAYS get today's date from SYSTEM CONTEXT (the date provided in system prompt) — NEVER from training data, NEVER from conversation history, NEVER guess
3. Compare `Last Updated` in CONTEXT.md with today's system date
4. TRUST THE FILE over your memory — files sync via git across devices

## Do NOT:
- Overwrite data from other sessions/devices
- Delete unfamiliar entries (they're from another PC)
- Assume you know file contents — always read before modifying
- Use any date other than the one from system context
