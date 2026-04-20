# LangChain, RAG & Agents — Simple, Interview-Ready

> Har section standalone hai. 5-10 min mein padh sakte ho.
> 🟢 = Easy, 🟡 = Medium, 🔴 = Advanced

---

## 🟢 LangChain Kyun Exist Karta Hai

**Problem:** Bina LangChain ke GenAI app banana = har cheez manually karna.
- API call manually likho
- Prompt manually format karo
- Response manually parse karo
- Memory manually manage karo
- Model switch karna ho toh poora code rewrite

**Solution:** LangChain = pre-built components ka framework for GenAI apps.
- Model switch? Ek line change
- Memory chahiye? Plugin karo
- RAG banana hai? Components connect karo

**Analogy:** Bina LangChain = raw AWS CLI commands se infrastructure banana. LangChain = Terraform modules use karna. Dono se kaam hoga, but Terraform se faster aur cleaner.

**Interview mein:** "LangChain provides a unified framework for building GenAI applications with pre-built components for model integration, memory management, and orchestration — similar to how Terraform abstracts infrastructure management."

---

## 🟢 LangChain Ke 5 Core Components

### 1. Models (LLM Wrapper)

Different AI providers ko ek unified interface deta hai. Model switch karna = ek line change.

```python
# OpenAI use karna hai
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")

# Bedrock pe switch karna hai? Sirf ye line change
from langchain_aws import ChatBedrock
llm = ChatBedrock(model_id="anthropic.claude-3-5-sonnet")

# Local model chahiye? Sirf ye line change
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.1")
```

Baaki poora code SAME rehta hai. Ye flexibility production mein valuable hai — client bole "OpenAI se Bedrock pe shift karo" → 5 min ka kaam.

### 2. Prompts (Template System)

Reusable prompt formats with variables. Jaise Terraform templates with different parameters.

```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "Tu ek {role} hai. {format} mein answer de."),
    ("human", "{question}")
])

# Use with different values
prompt = template.invoke({
    "role": "senior DevOps engineer",
    "format": "step by step",
    "question": "Lambda deploy kaise kare?"
})
```

**Kyun important:** Consistency (same structure har baar), maintainability (ek jagah change karo), testability (different prompts A/B test karo).

### 3. Chains (Sequential Processing)

Multiple steps ko connect karna. Ek step ka output = next step ka input.

```
Simple:  Question → LLM → Answer
Complex: Question → Analyze → Search Docs → Generate → Validate → Format → Return
```

**Tera IaC Generator mein:**
```
Architecture Description → Requirements Analysis → Design → Terraform Generation → Validation → Output
```

### 4. Memory (Conversation History)

AI by default STATELESS hai. Har message ke baad sab bhool jaata hai. Memory systems conversation history store karte hain.

| Memory Type | Kya karta hai | Kab use kare | Cost |
|-------------|-------------|-------------|------|
| Buffer | Sab kuch yaad rakho | Chhoti conversations | High (tokens badhte jaate hain) |
| Window | Last N messages yaad rakho | Most chatbots | Medium (fixed cost) |
| Summary | Purani conversation ka summary bana ke rakho | Long conversations | Low (summary chhota hota hai) |

**Tera healthcare chatbot mein:** Window memory — patient ke last 5-10 messages enough hain. Poori conversation store karna expensive aur unnecessary.

### 5. Agents (AI Jo Decisions Le Sake)

**Chain vs Agent — KEY difference:**
- Chain: Fixed path. Step 1 → Step 2 → Step 3. HAMESHA same order.
- Agent: Dynamic path. AI DECIDE karta hai next kya karna hai based on situation.

**Agent ka flow (ReAct pattern):**
```
1. THINK: "User ne appointment book karna chahta hai. Mujhe appointment API call karni chahiye."
2. ACT: Appointment API call karta hai
3. OBSERVE: Result dekhta hai — "slot available hai"
4. THINK: "Ab mujhe confirm karna hai user se"
5. ACT: Confirmation message generate karta hai
6. RETURN: Final answer user ko
```

**Tools:** Agents ke paas "tools" hote hain — functions jo woh call kar sakte hain. Agent DECIDE karta hai KONSA tool use karna hai.

```python
tools = [
    search_tool,        # Web search
    calculator_tool,    # Math calculations
    database_tool,      # DB queries
    api_tool,           # External API calls
]
# Agent decides which tool to use based on user's question
```

**Interview mein:** "Chains are for fixed workflows, agents are for dynamic decision-making. In my healthcare chatbot, the agent decides whether to call the appointment API, search the medical knowledge base, or escalate to emergency — based on the patient's query."

---

## 🟡 LangGraph — LangChain Ka Advanced Version

**Simple:** LangChain chains = linear flow (A → B → C). LangGraph = graph flow with loops, conditions, retries.

**Analogy:** LangChain = highway (ek direction). LangGraph = city roads (multiple routes, traffic signals, U-turns).

**Key concepts:**

| Concept | Kya hai | Example |
|---------|---------|---------|
| State | Data jo nodes ke beech travel karta hai | `{"query": "...", "docs": [...], "answer": "..."}` |
| Nodes | Processing steps (functions) | analyze_node, search_node, generate_node |
| Edges | Connections between nodes | analyze → search → generate |
| Conditional Edges | "Agar X toh A pe jao, warna B pe" | validation pass → output, fail → retry |

**Tera IaC Generator ka graph:**
```
Start → Analyze Requirements → Design Architecture → Generate Terraform
                                                          ↓
                                                    Validate Code
                                                     ↓        ↓
                                              (valid)       (invalid)
                                                ↓              ↓
                                            Output      Fix & Re-generate
                                                          (loop back ↑)
```

Ye LangChain chain se nahi ho sakta — validation fail hone pe WAPAS jaana padta hai. Ye graph behavior hai.

**LangGraph 2026 mein:**
- v1.1+ with deep agent templates
- Distributed runtime support
- Production mein: Uber, LinkedIn, Replit, GitLab use karte hain
- LangGraph Platform for deployment
- LangSmith for observability (tracing, debugging)
- LangGraph Studio for visual debugging

**Interview mein:** "LangGraph enables complex agent workflows with state graphs, conditional routing, and retry loops. My IaC generator uses a supervisor pattern with 5 specialized agents connected via LangGraph, including validation gates that loop back on failure."

---

## 🟡 Multi-Agent Systems

**Simple:** Ek agent sab kuch kare vs multiple specialized agents collaborate karein.

**Analogy:** Single agent = ek banda jo coding + testing + deployment sab kare. Multi-agent = team jisme developer, tester, DevOps alag alag hain.

### 3 Patterns

**1. Supervisor Pattern** (tera IaC generator)
```
Supervisor (Boss)
  ├── Requirements Analyzer (Worker 1)
  ├── Architecture Designer (Worker 2)
  ├── Terraform Generator (Worker 3)
  ├── Security Validator (Worker 4)
  └── Cost Optimizer (Worker 5)
```
Boss kaam distribute karta hai, workers apna kaam karte hain, boss review karta hai.

**2. Peer Pattern**
```
Agent A → Agent B → Agent C → Agent A (loop)
```
Sab equal. Ek ka output dusre ka input. No central coordinator.

**3. Hierarchical Pattern**
```
Top Supervisor
  ├── Team Lead 1
  │     ├── Worker A
  │     └── Worker B
  └── Team Lead 2
        ├── Worker C
        └── Worker D
```
Multiple levels. Complex workflows ke liye.

**Interview mein:** "I use the supervisor pattern in my IaC generator — a coordinator agent delegates to 5 specialized agents for requirements analysis, architecture design, Terraform generation, security validation, and cost optimization. LangGraph's state graph manages the data flow and conditional routing between them."

---

## 🟡 RAG — Retrieval Augmented Generation

**Simple:** AI ko "open book exam" dena. Pehle relevant documents SEARCH karo, phir un documents ke basis pe answer GENERATE karo.

**Without RAG:** AI sirf apni training data se answer deta hai. Knowledge cutoff hai. Company-specific info nahi pata. Hallucinate kar sakta hai.

**With RAG:** AI pehle relevant docs search karta hai → phir un docs ke basis pe answer deta hai. Updated info. Company docs accessible. Hallucination kam.

### RAG Pipeline — 5 Steps

```
Step 1: LOAD documents (PDFs, text files, web pages)
    ↓
Step 2: CHUNK them (bade docs ko chhote pieces mein todo)
    ↓
Step 3: EMBED chunks (text → numbers via embedding model)
    ↓
Step 4: STORE in Vector DB (ChromaDB, Pinecone)
    ↓
Step 5: RETRIEVE + GENERATE
    User question → embed → search similar chunks → top 3-5 chunks + question → LLM → answer
```

### Step 2 Deep Dive: Chunking

**Kyun chunk karte hain:** Poora document context window mein fit nahi hoga. Plus, chhote focused chunks se better matching hota hai.

**Chunk size:** Typically 500-1000 characters per chunk.

**Overlap:** Chunks ke beech 100-200 characters overlap rakhte hain. Kyun? Agar ek paragraph do chunks mein split hua, bina overlap ke boundary pe information lost ho sakti hai.

**Chunking strategies:**

| Strategy | Kya karta hai | Quality | Speed |
|----------|-------------|---------|-------|
| Fixed Size | Har chunk exactly 500 chars | Low (context tod sakta hai) | Fast |
| Recursive | Pehle paragraphs pe split, phir sentences, phir words | Good (context preserve) | Fast |
| Semantic | AI se meaning-based chunks banwao | Best | Slow, expensive |

**Production mein:** Recursive chunking most common hai. Good balance of quality and speed.

### Step 4 Deep Dive: Vector Databases

**Vector DB = database jo embeddings (numbers ki lists) store karta hai aur similarity search karta hai.**

| Vector DB | Type | Best for | Cost |
|-----------|------|----------|------|
| ChromaDB | Open source, local | Development, prototyping | Free |
| Pinecone | Managed cloud service | Production, scaling | Pay per use |
| pgvector | PostgreSQL extension | If you already use PostgreSQL | Free (self-hosted) |
| Weaviate | Open source, cloud option | Multi-modal search | Free / paid |
| Amazon OpenSearch | AWS managed | AWS ecosystem | Pay per use |

**Analogy:** ChromaDB = SQLite (local, simple, dev). Pinecone = RDS (managed, scalable, production).

### Step 5 Deep Dive: Retrieval + Generation

```
User: "Lambda function ka timeout kitna hai?"
    ↓
1. Question ka embedding banta hai
    ↓
2. Vector DB mein similar chunks search hote hain
    ↓
3. Top 3 matching chunks milte hain:
   - Chunk 1: "AWS Lambda supports timeout up to 15 minutes..."
   - Chunk 2: "Lambda configuration includes memory and timeout settings..."
   - Chunk 3: "For long-running tasks, consider Step Functions..."
    ↓
4. Prompt banta hai:
   "Given these documents: [chunk 1, 2, 3]
    Answer this question: Lambda function ka timeout kitna hai?
    Only answer from the given documents. If not found, say 'I don't know'."
    ↓
5. LLM generates: "Lambda ka maximum timeout 15 minutes hai. 
   Long-running tasks ke liye Step Functions consider karein."
```

**"Only answer from given documents"** — ye line hallucination reduce karti hai. AI ko bolo sirf context se answer de.

**Interview mein:** "RAG is a two-phase process: first retrieve relevant documents using embedding similarity search, then generate answers grounded in those documents. In my healthcare chatbot, I use recursive chunking with 200-char overlap, Titan Embeddings for search, and Claude for generation with strict grounding instructions."

---

## 🟡 RAG vs Fine-Tuning vs Prompt Engineering

**Decision tree:**
```
Pehle try: Prompt Engineering (free, quick, no infra needed)
    ↓ not enough?
Phir try: RAG (medium cost, handles most use cases)
    ↓ still not enough?
Last resort: Fine-Tuning (expensive, complex, risk of forgetting)
```

| | Prompt Engineering | RAG | Fine-Tuning |
|---|-------------------|-----|-------------|
| What | Better instructions to AI | Give AI relevant docs at query time | Retrain model on your data |
| Cost | Free | Medium (Vector DB + embeddings) | High (GPU compute) |
| Update data | Change prompt | Update documents | Retrain model |
| Best for | Simple tasks, formatting | Company knowledge, changing data | Specific behavior/style |
| Risk | Limited by model's knowledge | Retrieval quality matters | Catastrophic forgetting |

**Catastrophic forgetting** = fine-tuning mein model purana seekha bhool sakta hai. Jaise tune ek subject padha aur dusra bhool gaya.

**Interview mein:** "I follow a progressive approach: start with prompt engineering, add RAG if domain knowledge is needed, and consider fine-tuning only as a last resort. In practice, RAG handles 90% of use cases — it's easier to update, more transparent, and cheaper than fine-tuning."

---

## 🟡 Production Patterns

### Caching (Cost Reduction)

| Cache Type | Kya karta hai | Savings |
|-----------|-------------|---------|
| Exact Match | Same question → cached answer (Redis) | High for repeated queries |
| Semantic | Similar question → cached answer (embedding similarity) | High for paraphrased queries |

**Combined:** 60-80% cost reduction in production. Tera chatbot mein ye implement karna chahiye.

### Guardrails (Safety)

**Input guardrails** (user → AI se pehle):
- Dangerous queries block karo ("bomb kaise banaye?")
- Healthcare mein emergency detect karo ("chest pain" → escalate)
- Prompt injection attempts block karo

**Output guardrails** (AI → user se pehle):
- Hallucinated info validate karo
- Medical dosage check karo
- PII (personal info) filter karo
- Offensive content block karo

**AWS Bedrock Guardrails (2026):** Console mein define kar sakta hai — denied topics, content filters, word filters, PII masking. Code mein custom guardrails bhi likh sakta hai.

### Monitoring

| What to track | Why |
|--------------|-----|
| Token usage | Cost control |
| Response latency | User experience |
| Error rates | Reliability |
| Cache hit rates | Efficiency |
| Retrieval quality | RAG accuracy |

### Cost Optimization

1. **Model routing:** Simple queries → cheap model (Titan), complex → expensive model (Claude)
2. **Caching:** Don't call API for repeated/similar questions
3. **Prompt optimization:** Shorter prompts = fewer tokens = less cost
4. **Batch processing:** Group requests where possible

**Interview mein:** "In production, I implement multi-layer caching (exact + semantic) for 60-80% cost reduction, model routing based on query complexity, and Bedrock guardrails for safety. I track token usage and set budget alerts to keep costs within client budgets."

---

## 🔴 AWS Bedrock — Deeper Understanding

**Simple:** Bedrock = AWS ka AI model marketplace + runtime. Serverless. Multiple models ek API se.

**Analogy:** EC2 pe different instance types choose karta hai (t3.micro, c5.large). Bedrock pe different AI models choose karta hai (Claude, Titan, Llama).

**Models on Bedrock (2026):**

| Model | Best for | Cost tier |
|-------|----------|-----------|
| Claude 3.5 Sonnet / Claude 4 | Reasoning, code, long context | Medium-High |
| Amazon Titan Text | General tasks | Low (cheapest) |
| Amazon Titan Embeddings v2 | Embeddings for RAG | Low |
| Meta Llama 3.1 / 4 | Open source, customizable | Medium |
| Cohere Command R+ | RAG-optimized generation | Medium |
| Mistral Large 2 | Fast, efficient | Medium |

**Bedrock advantages:**
- No infrastructure management (serverless)
- Multiple models, one API
- AWS security + compliance built-in
- Pay per token (no upfront cost)
- VPC integration (data stays in your network)
- Built-in guardrails
- Knowledge Bases (managed RAG)
- Agents (managed agent framework)

**Bedrock Knowledge Bases (2026):**
Managed RAG service. Tu documents upload kar, Bedrock automatically chunk kare, embed kare, store kare, aur query time pe retrieve + generate kare. Manual RAG pipeline banana optional ho gaya hai for simple use cases.

**Interview mein:** "I use Bedrock as my primary AI platform because it provides serverless access to multiple models with built-in security, guardrails, and cost controls. For my projects, I use Claude for generation, Titan for embeddings, and Bedrock's built-in guardrails for safety filtering."

---

## Quick Revision — All Concepts

| Concept | One-liner |
|---------|-----------|
| LangChain | Framework for GenAI apps (like Terraform for AI) |
| Chain | Fixed sequential processing (A → B → C) |
| Agent | Dynamic decision-making (AI decides next step) |
| LangGraph | Advanced orchestration with graphs, loops, conditions |
| Multi-agent | Specialized agents collaborating (like microservices) |
| RAG | Search docs → inject as context → generate grounded answer |
| Chunking | Big docs → small pieces for better retrieval |
| Vector DB | Store embeddings for similarity search |
| Caching | Exact + semantic cache = 60-80% cost reduction |
| Guardrails | Input/output safety filters |
| Bedrock | AWS serverless AI platform, multiple models |
