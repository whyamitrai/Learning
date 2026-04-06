# System Design & Interview Prep - Final Boss Level

> Phone pe padh. Ye file tera interview ka cheat sheet hai. Concepts, patterns, aur answers.

---

## System Design Kyun Important Hai

12-15L roles mein system design optional hota hai. 20L+ mein MANDATORY hai.

System design = "Ye system banao jo X users handle kare, Y latency mein, Z budget mein."

Tera advantage: Tu cloud engineer hai. Tu already AWS services, scaling, load balancing samajhta hai. Most GenAI engineers ko ye nahi aata. Ye tera USP hai.

---

## GenAI System Design Template

Har GenAI system design question ke liye ye framework follow kar:

### Step 1: Requirements Clarify Karo (2-3 min)
- Kitne users? (100? 1M? 100M?)
- Latency requirement? (real-time? batch?)
- Accuracy requirement? (medical = high, casual chat = medium)
- Budget constraint?
- Data sensitivity? (healthcare = HIPAA, finance = PCI)

### Step 2: High-Level Architecture (5 min)
- Draw the boxes: Client → API Gateway → Service → Database
- Identify GenAI-specific components: LLM, Vector DB, Embedding Service

### Step 3: Deep Dive Components (15 min)
- Model selection and why
- Caching strategy
- Scaling approach
- Data pipeline
- Monitoring

### Step 4: Trade-offs Discuss Karo (5 min)
- Cost vs latency
- Accuracy vs speed
- Complexity vs maintainability

---

## Design 1: Scalable Chatbot (1M Users)

### Architecture

```
Users → CDN → Load Balancer → API Gateway → Chat Service
                                                  ↓
                                          Message Router
                                         ↓            ↓
                                   Simple Query    Complex Query
                                      ↓                ↓
                                   Cache Hit?      RAG Pipeline
                                   ↓      ↓            ↓
                                  Yes     No       Vector DB Search
                                   ↓      ↓            ↓
                                Return  LLM Call    LLM + Context
                                          ↓            ↓
                                       Cache It     Return
```

### Key Decisions

**Model Selection**:
- Simple queries: Claude Instant / GPT-3.5 (fast, cheap)
- Complex queries: Claude 3 / GPT-4 (smart, expensive)
- Router decides which model based on query complexity

**Caching** (CRITICAL for cost):
- Layer 1: Exact match cache (Redis) - same question = same answer
- Layer 2: Semantic cache - similar question = cached answer
- Target: 60-80% cache hit rate = 60-80% cost reduction

**Session Management**:
- Redis cluster for session storage
- Window memory: last 10 messages per session
- Session TTL: 1 hour (auto-cleanup)

**Scaling**:
- Horizontal scaling: Multiple chat service instances behind load balancer
- Auto-scaling based on CPU/request count
- Rate limiting per user tier (free: 100/hr, premium: 1000/hr)

**Cost Estimation** (interviewers love this):
- 1M users, 10 messages/day average = 10M messages/day
- 80% cache hit = 2M LLM calls/day
- Average 500 tokens per call
- GPT-3.5: 2M × 500 × $0.002/1K = $2,000/day = $60K/month
- With caching: $12K/month (80% savings)

---

## Design 2: RAG System at Scale (10M Documents)

### Architecture

```
Document Ingestion Pipeline:
Documents → Chunker → Embedding Service → Vector DB
                                              ↓
                                        Index Manager
                                        (hot/warm/cold)

Query Pipeline:
User Query → Embedding → Vector Search → Re-ranker → LLM → Response
                              ↓
                        Multi-tier search
                        (hot → warm → cold)
```

### Key Decisions

**Chunking Strategy**:
- Recursive text splitter: 1000 chars, 200 overlap
- Metadata preservation: source, page, section
- Chunk-level embeddings + document-level summaries

**Vector DB Architecture**:
- Hot tier (in-memory): Top 100K most accessed chunks
- Warm tier (SSD): Next 1M chunks
- Cold tier (disk): Remaining 9M chunks
- Promotion/demotion based on access patterns

**Search Optimization**:
- Approximate Nearest Neighbor (ANN) instead of exact search
- Pre-filtering by metadata before vector search
- Re-ranking: Vector search gives top 20, re-ranker picks top 5

**Update Strategy**:
- Hash-based change detection (don't re-embed unchanged docs)
- Incremental indexing (add new chunks without rebuilding entire index)
- Background reindexing for major updates

---

## Design 3: Real-Time Voice Bot

### Architecture

```
User Voice → WebSocket → Speech-to-Text → Text Processing
                                                ↓
                                          LLM (streaming)
                                                ↓
                                          Text-to-Speech
                                                ↓
                                          WebSocket → User
```

### Key Decisions

**Latency Budget** (total < 500ms):
- Speech-to-Text: 100ms (streaming, not batch)
- LLM Processing: 200ms (first token, then stream)
- Text-to-Speech: 100ms (streaming)
- Network: 100ms buffer

**Streaming**: 
- Bidirectional WebSocket (not HTTP request-response)
- LLM streams tokens as they're generated
- TTS starts as soon as first sentence is complete
- User hears response while LLM is still generating

**Tera Nova Sonic project**: Exactly this architecture. Interview mein ye explain kar with specific latency numbers.

---

## Tera 3 Projects - Interview Explanations

### STAR Method Reminder
- **S**ituation: Context kya tha
- **T**ask: Tujhe kya karna tha
- **A**ction: Tune kya kiya (TECHNICAL DETAIL yahan)
- **R**esult: Kya outcome aaya (NUMBERS yahan)

### Project 1: IaC Generator

**30-second pitch**:
"I built a multi-agent GenAI system using LangGraph and AWS Bedrock that converts architecture diagram descriptions into production-ready Terraform code. It uses a supervisor pattern with 5 specialized agents - requirements analyzer, architecture designer, Terraform generator, security validator, and cost optimizer. Reduced infrastructure setup time from 6 hours to 20 minutes."

**Technical deep dive points**:
- LangGraph state graph with conditional edges (validation failure → retry loop)
- Supervisor pattern for agent coordination
- Low temperature (0.1) for consistent Terraform output
- Multi-layer validation: syntax check → security scan → cost analysis
- Bedrock Claude for code generation (best reasoning capability)

**Numbers to mention**:
- 85% time reduction (6 hours → 20 minutes)
- 90% fewer configuration errors
- 30% AWS cost savings through optimized configs
- 15 projects/month × 5 hours saved = 75 hours/month saved

### Project 2: Healthcare Chatbot

**30-second pitch**:
"I built a serverless conversational AI system for a healthcare client using AWS Bedrock, Lambda, and API Gateway. It integrates with 4 hospital management APIs for appointment scheduling and patient queries. Uses RAG with medical knowledge base and has safety filters for medical accuracy."

**Technical deep dive points**:
- Serverless architecture: Lambda + API Gateway + DynamoDB
- RAG pipeline: Medical docs → ChromaDB → context injection
- Safety filters: Emergency detection, dangerous query blocking, medical disclaimers
- 4 API integrations: Appointments, patient info, medication info, doctor availability
- HIPAA-aware: Audit logging, data encryption, minimal data exposure

**Numbers to mention**:
- 4 healthcare APIs integrated
- Sub-second response time
- Safety filter catches 100% of emergency queries
- Handles ~150-200 queries daily

### Project 3: Voice Bot (Nova Sonic)

**30-second pitch**:
"I engineered a real-time voice bot for a retail client using AWS Nova Sonic APIs with bidirectional WebSocket streaming. Achieved sub-second voice response latency through parallel processing of speech-to-text, LLM inference, and text-to-speech."

**Technical deep dive points**:
- Bidirectional WebSocket for real-time audio streaming
- Parallel processing pipeline (not sequential)
- Nova Sonic for speech processing
- Bedrock for LLM inference
- Docker + ECS for containerized deployment

**Numbers to mention**:
- Sub-200ms first response latency
- Bidirectional streaming (simultaneous input/output)
- Containerized on ECS with auto-scaling

---

## Behavioral Questions - Top 5

### "Tell me about a time you took initiative"
→ IaC Generator. Nobody asked me to build it. I saw 75 hours/month wasted on repetitive Terraform writing. Built prototype on my own time. Presented to manager. Got approval. Shipped it. Saved ₹18L annually.

### "Tell me about a technical challenge you solved"
→ Voice Bot latency. Manager wanted sequential processing. I proved with prototypes that parallel processing was necessary (800ms vs 180ms). Built both versions, showed data, convinced team. Shipped with 180ms latency.

### "How do you handle disagreements?"
→ Data-driven approach. Voice Bot example - didn't argue opinions, built prototypes, showed numbers. Let data speak.

### "Tell me about a failure"
→ First version of IaC Generator had 40% error rate in generated Terraform. Root cause: single-shot generation without validation. Solution: Added multi-agent validation pipeline. Error rate dropped to <5%.

### "Why are you leaving your current company?"
→ "I've learned a lot at Rapyder and built production GenAI systems. But I'm looking for deeper technical challenges and a role where I can work on larger-scale AI systems. I want to grow into a senior GenAI engineer, and I believe [company name] offers that path."
(NEVER mention bond, salary, or negative things about current company)

---

## Salary Negotiation Script

### When They Ask "What's Your Expected CTC?"

**DON'T say**: "4.27L hai abhi, 12L chahiye" (they'll offer 8-9L)

**DO say**: "Based on my production GenAI experience, AWS certification, and the market rate for GenAI engineers in Bangalore, I'm targeting 14-16 LPA. I'm flexible based on the overall compensation package including learning opportunities and growth path."

**Why 14-16 when you want 12?**: Negotiation 101. Ask higher, settle at your target. They'll counter at 11-12, you'll negotiate to 12-13.

### When They Give an Offer

- NEVER accept immediately. "Thank you, I'm excited about this opportunity. Can I have 2-3 days to review the complete offer?"
- If offer is below target: "I appreciate the offer. Based on my experience with production GenAI systems and the market rate, I was expecting closer to [X]. Is there flexibility?"
- Mention competing offers (even if you don't have them): "I'm in discussions with a couple of other companies as well, and I want to make sure I make the right decision."

### Bond Discussion

If they ask about notice period/bond: "I have a 2-month notice period with a bond obligation. Would the company be able to support with a signing bonus to cover the transition costs?"

Many companies have relocation/signing bonus budgets. 2L is a small amount for them if they want you.

---

## DSA Strategy (Since You're Already Doing It)

Tera current approach is solid: pattern-based, 5-6 questions per pattern.

**Current progress**: 47 questions, up to trees. Good pace.

**What to cover for 12-15L roles**:
- ✅ Arrays, Two Pointers, Sliding Window (done)
- ✅ Hashmaps, Prefix Sum (done)
- ✅ Binary Search (done)
- 🔄 Trees (in progress)
- ⬜ Graphs (BFS, DFS, basic shortest path)
- ⬜ Basic DP (fibonacci, climbing stairs, coin change, LCS)
- ⬜ Heap/Priority Queue
- ⬜ Stack/Queue patterns

**Target**: 80-100 questions total covering all patterns above. Ye 12-15L roles ke liye enough hai.

**For 20L+ roles** (later):
- DP medium-hard
- Graph advanced (Dijkstra, topological sort)
- Trie
- Segment trees (rare but shows up)

---

## Weekly Schedule Suggestion

**Weekdays (2 hours/day)**:
- 30 min: Read GenAI/ML concepts (these files, on commute)
- 1 hour: DSA practice (1-2 problems)
- 30 min: Apply to 2-3 jobs OR practice interview answers

**Weekends (4 hours/day)**:
- Saturday: Code practice (GenAI hands-on from practice folder)
- Sunday: System design study + mock interview prep

**Non-negotiable daily habits**:
1. Solve at least 1 DSA problem
2. Apply to at least 1 job
3. Read at least 1 concept page

---

## Key Takeaways

1. System design = requirements → architecture → deep dive → trade-offs
2. GenAI system design: always discuss caching, model selection, cost
3. STAR method for every behavioral answer (Situation, Task, Action, Result)
4. Always have NUMBERS ready for your projects
5. Negotiate salary UP from your target, not down
6. Never badmouth current company
7. DSA: pattern-based approach is correct, keep going
8. Apply NOW, don't wait to be "ready"

> Next: Create a `code_practice/` folder for hands-on coding exercises
