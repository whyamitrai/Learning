---
inclusion: always
---

# DSA Context Sync Rule

## CRITICAL — READ BEFORE EVERY ACTION

Before making ANY changes to files in the `dsa/` folder:

1. **ALWAYS read `dsa/CONTEXT.md` FIRST** — check the LIVE SESSION STATE section
2. **Compare the `Last Updated` date with today's date** — if different, this means changes were made on another device
3. **NEVER overwrite data from other sessions** — if CONTEXT.md has newer data than what you remember from this conversation, TRUST THE FILE, not your memory
4. **If you see unfamiliar entries in sprint log, session log, or revision files** — these are from another PC. Do NOT delete or overwrite them.
5. **Always read the latest state of ALL dsa files before updating them** — never assume you know the current content
6. **At the START of every new user message** — read `dsa/CONTEXT.md` and `dsa/revision_sprint.md` to confirm current state. Even if same session, always verify before proceeding.

## Why This Exists
User works on multiple PCs. Changes are synced via git. AI must respect changes made in other sessions on other devices. Previous sessions have lost data because AI overwrote newer changes with stale memory.
