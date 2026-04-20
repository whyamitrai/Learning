# Interview Prep — Projects, Behavioral, System Design

> Ye file tera interview ka cheat sheet hai. Har section standalone.
> Projects ke 30-second pitches, STAR answers, system design framework, negotiation scripts.

---

## 🟢 Tera 3 Projects — 30-Second Pitches

### Project 1: IaC Generator

**Pitch:**
"I built a multi-agent GenAI system using LangGraph and AWS Bedrock that converts architecture diagram descriptions into production-ready Terraform code. It uses a supervisor pattern with 5 specialized agents — requirements analyzer, architecture designer, Terraform generator, security validator, and cost optimizer. Reduced infrastructure setup from 6 hours to 20 minutes."

**Technical deep dive points (agar interviewer puche):**
- LangGraph state graph with conditional edges (validation fail → retry loop)
- Supervisor pattern for agent coordination
- Low temperature (0.1) for consistent Terraform output
- Multi-layer validation: syntax check → security scan → cost analysis
- Bedrock Claude for code generation (best reasoning)

**Numbers:**
- 85% time reduction (6 hours → 20 minutes)
- 90% fewer configuration errors
- 30% AWS cost savings through optimized configs

### Project 2: Healthcare Chatbot

**Pitch:**
"I built a serverless conversational AI for a healthcare client using AWS Bedrock, Lambda, and API Gateway. It integrates with 4 hospital management APIs for appointment scheduling and patient queries. Uses RAG with medical knowledge base and has safety filters for medical accuracy."

**Technical deep dive points:**
- Serverless: Lambda + API Gateway + DynamoDB
- RAG pipeline: Medical docs → ChromaDB → context injection
- Safety filters: Emergency detection, dangerous query blocking, medical disclaimers
- 4 API integrations: Appointments, patient info, medication, doctor availability
- Audit logging for compliance

**Numbers:**
- 4 healthcare APIs integrated
- Sub-second response time
- 150-200 queries daily
- Safety filter catches 100% of emergency queries

### Project 3: Voice Bot (Nova Sonic)

**Pitch:**
"I engineered a real-time voice bot for a retail client using AWS Nova Sonic with bidirectional WebSocket streaming. Achieved sub-200ms first-response latency through parallel processing of speech-to-text, LLM inference, and text-to-speech."

**Technical deep dive points:**
- Bidirectional WebSocket (not HTTP request-response)
- Parallel processing pipeline (STT + LLM + TTS simultaneously)
- Nova Sonic for speech processing
- Bedrock for LLM inference
- Docker + ECS for containerized deployment

**Numbers:**
- Sub-200ms first response latency
- Bidirectional streaming
- Containerized on ECS with auto-scaling

---

## 🟢 STAR Method — Behavioral Answers

**S**ituation → **T**ask → **A**ction → **R**esult

Har behavioral answer mein ye 4 parts hone chahiye. Action mein TECHNICAL DETAIL, Result mein NUMBERS.

### "Tell me about a time you took initiative"

**S:** At Rapyder, I noticed our team was spending 75+ hours/month writing repetitive Terraform templates for client projects.
**T:** Nobody asked me to solve this. I decided to build an automated solution.
**A:** Built a multi-agent GenAI system using LangGraph and Bedrock. Supervisor pattern with 5 specialized agents. Validated output through syntax checking and security scanning.
**R:** Reduced infrastructure setup from 6 hours to 20 minutes. 85% time savings. Saved approximately ₹18L annually in engineering hours.

### "Tell me about a technical challenge you solved"

**S:** Building the voice bot, the initial architecture used sequential processing — speech-to-text, then LLM, then text-to-speech. Latency was 800ms.
**T:** Client needed sub-500ms response for natural conversation feel.
**A:** I proposed parallel processing — start TTS as soon as first sentence is ready, while LLM is still generating. Built prototypes of both approaches, measured latency.
**R:** Parallel approach achieved 180ms first-response latency. Showed data to team, convinced them. Shipped with sub-200ms latency.

### "How do you handle disagreements?"

**S:** Voice bot project — manager wanted sequential processing (simpler to build).
**T:** I believed parallel processing was necessary for the latency requirement.
**A:** Instead of arguing opinions, I built both prototypes. Measured: sequential = 800ms, parallel = 180ms. Presented data to the team.
**R:** Data spoke for itself. Team agreed on parallel approach. Shipped successfully.

### "Tell me about a failure"

**S:** First version of IaC Generator had 40% error rate in generated Terraform.
**T:** Needed to bring error rate to acceptable levels for production use.
**A:** Root cause: single-shot generation without validation. Solution: Added multi-agent validation pipeline — syntax check, security scan, cost analysis. Each failure loops back for regeneration.
**R:** Error rate dropped from 40% to under 5%. Learned that GenAI outputs ALWAYS need validation layers.

### "Why are you leaving your current company?"

"I've learned a lot at Rapyder and built production GenAI systems from scratch. I'm looking for deeper technical challenges and a role where I can work on larger-scale AI systems. I want to grow into a senior GenAI engineer, and I believe [company name] offers that path with [specific thing about the company]."

**NEVER mention:** Bond, salary, anything negative about Rapyder.

---

## 🟡 GenAI System Design — Framework

### 4-Step Framework (Use for EVERY system design question)

**Step 1: Requirements (2-3 min)**
- Kitne users? (100? 1M?)
- Latency? (real-time? batch?)
- Accuracy? (medical = high, casual = medium)
- Budget?
- Data sensitivity? (HIPAA? PCI?)

**Step 2: High-Level Architecture (5 min)**
- Draw boxes: Client → API Gateway → Service → Database
- Add GenAI components: LLM, Vector DB, Embedding Service
- Show data flow with arrows

**Step 3: Deep Dive (15 min)**
- Model selection and WHY
- Caching strategy
- Scaling approach
- Data pipeline
- Monitoring

**Step 4: Trade-offs (5 min)**
- Cost vs latency
- Accuracy vs speed
- Complexity vs maintainability

### Design: Scalable Chatbot (1M Users)

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

**Key decisions to discuss:**
- Model routing: Simple → cheap model, Complex → expensive model
- Caching: Exact (Redis) + Semantic. Target 60-80% hit rate.
- Session: Redis cluster, window memory (last 10 messages), 1hr TTL
- Scaling: Horizontal, auto-scale on CPU/request count
- Rate limiting: Free tier 100/hr, premium 1000/hr

**Cost estimation (interviewers love this):**
- 1M users × 10 msgs/day = 10M messages/day
- 80% cache hit = 2M LLM calls/day
- 500 tokens avg per call
- Claude 3.5 Sonnet: 2M × 500 × $3/1M = $3,000/day
- With caching: ~$600/day (80% savings)

### Design: RAG System (10M Documents)

```
Ingestion: Documents → Chunker → Embedding Service → Vector DB
Query:     User Query → Embed → Vector Search → Re-ranker → LLM → Response
```

**Key decisions:**
- Chunking: Recursive, 1000 chars, 200 overlap
- Vector DB tiering: Hot (in-memory) → Warm (SSD) → Cold (disk)
- Search: ANN (Approximate Nearest Neighbor) for speed
- Re-ranking: Vector search gives top 20, re-ranker picks top 5
- Updates: Hash-based change detection, incremental indexing

### Design: Real-Time Voice Bot

```
User Voice → WebSocket → STT → LLM (streaming) → TTS → WebSocket → User
```

**Latency budget (total < 500ms):**
- STT: 100ms (streaming)
- LLM: 200ms (first token, then stream)
- TTS: 100ms (streaming)
- Network: 100ms buffer

**Key:** Parallel processing. TTS starts as soon as first sentence is ready. User hears response while LLM is still generating.

---

## 🟡 Technical Interview Questions — Quick Answers

**"LangChain vs LangGraph?"**
→ LangChain = linear chains. LangGraph = graphs with loops, conditions, retries. Use LangGraph for decision-making, validation failures, multi-agent coordination.

**"RAG vs Fine-tuning?"**
→ RAG = external knowledge at query time (easy to update, cheaper). Fine-tuning = retrain model (better for specific behavior, expensive). RAG first, fine-tuning as last resort.

**"How do you handle hallucination?"**
→ RAG for grounding, low temperature, output validation, source citation, guardrails. Healthcare chatbot mein sab use kiye + medical safety filters.

**"Explain your multi-agent architecture"**
→ Supervisor pattern with LangGraph. Supervisor coordinates 5 specialized agents. State graph manages data flow. Conditional edges handle validation failures with retry loops.

**"How do you optimize GenAI costs?"**
→ Multi-layer caching (exact + semantic), model routing by complexity, prompt optimization, token tracking with alerts, batch processing.

**"What's MCP?"**
→ Model Context Protocol by Anthropic. Standard protocol for connecting AI models to external tools and data sources. Like a USB standard for AI — any tool can plug in. 97M+ monthly SDK downloads in 2026.

**"What's A2A?"**
→ Agent-to-Agent protocol by Google. Enables different AI agents (even from different vendors) to discover each other and collaborate. 50+ enterprise partners. MCP handles vertical (model ↔ tools), A2A handles horizontal (agent ↔ agent).

**"Explain Transformer architecture"**
→ Parallel text processing + self-attention mechanism. Each token attends to all other tokens simultaneously. Solved RNN's sequential bottleneck. All modern LLMs (GPT, Claude, BERT) are based on Transformers.

**"Supervised vs Unsupervised learning?"**
→ Supervised = labeled data (input + answer), model learns to predict. Unsupervised = no labels, model finds patterns/groups on its own.

**"Overfitting kya hai?"**
→ Model memorizes training data instead of learning patterns. High accuracy on training, low on test. Fix: more data, regularization, simpler model.

**"Precision vs Recall?"**
→ Precision = when model said "yes", how often was it right? Recall = of all actual "yes" cases, how many did model catch? F1 = balance of both.

---

## 🟢 Salary Negotiation Scripts

### When asked "What's your expected CTC?"

**Say:** "Based on my production GenAI experience, AWS certification, and the market rate for GenAI engineers in Bangalore, I'm targeting 14-16 LPA. I'm flexible based on the overall package and growth opportunities."

**Why 14-16?** They'll counter at 11-12. You negotiate to 12-13. If you say 12, they'll offer 8-9.

**If they push for current CTC:**
"I'd prefer to discuss based on market rate and role expectations rather than my current compensation."

### When you get an offer

1. NEVER accept immediately. "Thank you, I'm excited. Can I have 2-3 days to review?"
2. If below target: "I appreciate the offer. Based on my experience, I was expecting closer to [X]. Is there flexibility?"
3. Mention competition: "I'm in discussions with a couple of other companies as well."

### Bond discussion

"I have a transition obligation. Would the company be able to support with a signing bonus to cover the transition costs?"

₹2L is small for most companies. Many have signing bonus budgets.
