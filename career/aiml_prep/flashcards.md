# Flashcards — Active Recall Practice

> Cover the answer, try to recall from memory. If blank → re-read that section.
> 10 cards/day. Shuffle order every few days.
> Cards marked with ⭐ = you've blanked on these before, prioritize them.

---

## GenAI Core (File 01)

**Q1:** GenAI aur Traditional AI mein farak?
<details><summary>Answer</summary>
Traditional AI = classify/sort (cat ya dog?). GenAI = create new content (cat ki photo banao sunglasses ke saath).
</details>

**Q2:** LLM internally kya karta hai? Ek line.
<details><summary>Answer</summary>
Next token prediction. Previous tokens dekh ke next most likely token predict karta hai. Pattern matching at massive scale.
</details>

**Q3:** Token kya hai? 3 reasons kyun important?
<details><summary>Answer</summary>
Text ka chhota piece (~0.75 words). Important: 1) Cost per token charge hota hai 2) Context window token limit hai 3) Zyada tokens = slow response.
</details>

**Q4:** Context window kya hai? GPT-4o vs Claude 3.5?
<details><summary>Answer</summary>
Kitna text AI ek baar mein process kar sakta hai. GPT-4o: 128K tokens. Claude 3.5: 200K tokens.
</details>

**Q5:** Temperature 0.1 vs 0.8 — kab kya?
<details><summary>Answer</summary>
0.1 = consistent (code gen, medical info, data extraction). 0.8 = creative (brainstorming, casual chat). IaC generator mein 0.1, voice bot mein 0.4-0.6.
</details>

**Q6:** Embedding kya hai? Ek line.
<details><summary>Answer</summary>
Text ko numbers ki list mein convert karna jahan similar meanings = similar numbers. RAG ka foundation.
</details>

**Q7:** Hallucination kya hai? 5 fixes?
<details><summary>Answer</summary>
AI confident hoke galat info deta hai. Fix: 1) RAG (grounding) 2) Low temperature 3) Output validation 4) Guardrails 5) Source citation. Healthcare chatbot mein sab use kiye.
</details>

**Q8:** Transformer ka core innovation?
<details><summary>Answer</summary>
Parallel processing + Attention mechanism. RNN sequential tha (slow, bhool jaata tha). Transformer saare tokens ek saath process karta hai.
</details>

**Q9:** Attention mechanism ek line mein?
<details><summary>Answer</summary>
Har token decide karta hai baaki tokens mein se kisko kitna dhyan dena hai. "it was tired" mein "it" ka attention "cat" pe high.
</details>

**Q10:** Encoder vs Decoder?
<details><summary>Answer</summary>
Encoder = input samajhna (BERT, search/classification). Decoder = output generate karna (GPT/Claude, text gen). Tu mostly decoder use karta hai.
</details>

---

## LangChain & RAG (File 02)

**Q11:** LangChain kyun use karte hain?
<details><summary>Answer</summary>
Pre-built components for GenAI apps. Model switch = 1 line. Memory, prompts, chains built-in. Bina iske sab manual. Terraform analogy: raw CLI vs modules.
</details>

**Q12:** Chain vs Agent?
<details><summary>Answer</summary>
Chain = fixed path (A→B→C hamesha). Agent = dynamic (AI DECIDE karta hai next kya). Chain = bash script, Agent = K8s operator.
</details>

**Q13:** LangChain vs LangGraph?
<details><summary>Answer</summary>
LangChain = linear chains. LangGraph = graphs with loops, conditions, retries. LangGraph for decision-making, validation failures, multi-agent.
</details>

**Q14:** RAG ke 5 steps?
<details><summary>Answer</summary>
1) Load documents 2) Chunk (500-1000 chars, 200 overlap) 3) Embed (text → numbers) 4) Store in Vector DB 5) Retrieve similar chunks + Generate answer with LLM.
</details>

**Q15:** Chunking mein overlap kyun?
<details><summary>Answer</summary>
Boundary pe information lost ho sakti hai bina overlap ke. 200 char overlap context preserve karta hai.
</details>

**Q16:** RAG vs Fine-tuning?
<details><summary>Answer</summary>
RAG = external knowledge at query time (easy update, cheaper, most cases). Fine-tuning = retrain model (specific behavior, expensive, forgetting risk). RAG first.
</details>

**Q17:** Supervisor pattern kya hai?
<details><summary>Answer</summary>
Boss agent kaam distribute karta hai, workers apna kaam karte hain, boss review karta hai. IaC generator: supervisor + 5 workers (requirements, design, terraform, security, cost).
</details>

**Q18:** Memory ke 3 types?
<details><summary>Answer</summary>
Buffer = sab yaad (expensive). Window = last N messages (practical). Summary = purani conversation ka summary (smart). Healthcare chatbot mein window.
</details>

---

## Interview Answers (File 03)

**Q19:** IaC Generator — 30 seconds.
<details><summary>Answer</summary>
Multi-agent GenAI, LangGraph + Bedrock. Architecture description → production Terraform. Supervisor pattern, 5 agents. 85% time reduction (6hr→20min), 90% fewer errors, 30% cost savings.
</details>

**Q20:** Healthcare Chatbot — 30 seconds.
<details><summary>Answer</summary>
Serverless, Bedrock + Lambda + API Gateway. 4 hospital APIs. RAG with medical knowledge base. Safety filters. Sub-second response, 150-200 queries daily.
</details>

**Q21:** Voice Bot — 30 seconds.
<details><summary>Answer</summary>
Real-time, Nova Sonic + Bedrock. Bidirectional WebSocket. Parallel pipeline (not sequential). Sub-200ms latency. Docker + ECS.
</details>

**Q22:** "How handle hallucination?"
<details><summary>Answer</summary>
RAG grounding, low temperature, output validation, source citation, guardrails. Healthcare chatbot: all of these + medical safety filters.
</details>

**Q23:** "How optimize GenAI costs?"
<details><summary>Answer</summary>
Multi-layer caching (exact + semantic = 60-80% savings), model routing by complexity, prompt optimization, token tracking with alerts, batch processing.
</details>

**Q24:** Expected CTC?
<details><summary>Answer</summary>
"Based on production GenAI experience, AWS cert, and market rate for GenAI engineers in Bangalore, targeting 14-16 LPA. Flexible based on overall package." (Ask 14-16, settle 12-13)
</details>

**Q25:** "Why leaving?"
<details><summary>Answer</summary>
"Learned a lot, built production GenAI systems. Looking for deeper technical challenges and larger-scale AI systems. Want to grow into senior GenAI engineer." NEVER mention bond/salary/negative.
</details>

---

## System Design (File 03)

**Q26:** GenAI system design — 4 steps?
<details><summary>Answer</summary>
1) Requirements (users, latency, accuracy, budget) 2) High-level architecture (boxes + GenAI components) 3) Deep dive (model selection, caching, scaling) 4) Trade-offs (cost vs latency, accuracy vs speed).
</details>

**Q27:** Chatbot caching?
<details><summary>Answer</summary>
Layer 1: Exact match (Redis). Layer 2: Semantic cache (embedding similarity). Target 60-80% hit rate = 60-80% cost reduction.
</details>

**Q28:** Vector DB tiering?
<details><summary>Answer</summary>
Hot (in-memory): most accessed. Warm (SSD): next tier. Cold (disk): rarely accessed. Like S3 storage classes.
</details>

---

## ML Fundamentals (Concept Level)

**Q29:** ML kya hai ek line mein?
<details><summary>Answer</summary>
Computer ko data dikha ke patterns seekhna sikhana — bina rules likhne ke.
</details>

**Q30:** Supervised vs Unsupervised vs Reinforcement?
<details><summary>Answer</summary>
Supervised = labeled data (input+answer, predict). Unsupervised = no labels (find patterns). Reinforcement = actions + rewards (learn strategy). ChatGPT uses RLHF.
</details>

**Q31:** Classification vs Regression?
<details><summary>Answer</summary>
Classification = categories (spam/not spam). Regression = numbers (house price). Classification = dabba, Regression = scale.
</details>

**Q32:** Overfitting? Fix?
<details><summary>Answer</summary>
Training pe 99%, test pe 60%. Ratta maara. Fix: more data, regularization, dropout, simpler model.
</details>

**Q33:** Precision vs Recall?
<details><summary>Answer</summary>
Precision = jab alarm bajaya, sahi tha kya? (false alarm check). Recall = kitne chor pakde? (miss check). F1 = balance.
</details>

**Q34:** Gradient descent?
<details><summary>Answer</summary>
Andheri raat mein pahaad se utarna. Slope feel karo (gradient), step lo (weight update), repeat until minimum loss.
</details>

**Q35:** Fine-tuning kab, RAG kab?
<details><summary>Answer</summary>
RAG = most cases (easy update, cheaper). Fine-tuning = specific behavior/style jo RAG se nahi aa raha. Fine-tuning expensive, forgetting risk.
</details>

---

## 2026 Trends

**Q36:** MCP kya hai?
<details><summary>Answer</summary>
Model Context Protocol (Anthropic). Standard for connecting AI models to tools/data. Like USB standard. 97M+ monthly SDK downloads. Vertical integration: model ↔ tools.
</details>

**Q37:** A2A kya hai?
<details><summary>Answer</summary>
Agent-to-Agent protocol (Google). Different AI agents communicate/collaborate. 50+ enterprise partners. Horizontal integration: agent ↔ agent.
</details>

**Q38:** MCP + A2A together?
<details><summary>Answer</summary>
MCP = model ko tools se connect (vertical). A2A = agents ko ek dusre se connect (horizontal). Together = complete agentic ecosystem.
</details>

**Q39:** LangGraph 2026 mein kya naya?
<details><summary>Answer</summary>
v1.1+ with deep agent templates, distributed runtime. Production: Uber, LinkedIn, Replit, GitLab. LangGraph Platform for deployment, LangSmith for observability.
</details>

**Q40:** Agentic AI kya hai?
<details><summary>Answer</summary>
AI agents jo khud decisions le sakein, tools use karein, complex workflows handle karein. 2026 ka biggest trend. Tera IaC generator ek agentic system hai.
</details>

---

## How to Use

1. Daily: 10 random cards. Cover answer. Recall.
2. Blank on a card? → ⭐ mark it. Revisit tomorrow.
3. Weekly: All ⭐ cards. Still blank? → Re-read source file.
4. Before interview: ALL cards. Can't answer = study that topic.
