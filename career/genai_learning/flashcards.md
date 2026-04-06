# GenAI Flashcards — Active Recall Practice

> Don't just read these. Cover the answer, try to answer from memory.
> If you can't → go back to the source file and re-read that section.
> Review 10 cards/day on commute. Shuffle the order every few days.

---

## 🟢 Core Concepts (File 01)

**Q1:** GenAI aur Traditional AI mein kya farak hai?
<details><summary>Answer</summary>
Traditional AI = classify/sort existing categories (cat ya dog?).
GenAI = create new content (cat ki photo banao sunglasses ke saath).
</details>

**Q2:** LLM actually kya karta hai internally? Ek line mein.
<details><summary>Answer</summary>
Next token prediction. Bas. Previous tokens dekh ke next most likely token predict karta hai.
</details>

**Q3:** Token kya hai aur kyun important hai?
<details><summary>Answer</summary>
Text ka ek piece (~0.75 words). Important kyunki: cost per token charge hota hai, context window token limit hoti hai, zyada tokens = slow response.
</details>

**Q4:** Context window kya hai? GPT-4 vs Claude 3 mein kitni hai?
<details><summary>Answer</summary>
Kitna text AI ek baar mein yaad rakh sakta hai. GPT-4: ~128K tokens. Claude 3: ~200K tokens.
</details>

**Q5:** Temperature 0.1 vs 0.8 — kab kya use karega?
<details><summary>Answer</summary>
0.1 = consistent, predictable (code generation, data extraction). 0.8 = creative, varied (brainstorming, casual chat). Tera IaC generator mein 0.1, voice bot mein thoda higher.
</details>

**Q6:** Embedding kya hai? Ek line mein.
<details><summary>Answer</summary>
Text ko numbers ki list mein convert karna jahan similar meanings = similar numbers. RAG ka foundation hai.
</details>

**Q7:** Hallucination kya hai aur kaise handle karte hain?
<details><summary>Answer</summary>
AI confident hoke galat info deta hai. Handle: RAG (grounding), low temperature, output validation, guardrails, source citation. Healthcare chatbot mein sab use kiye.
</details>

**Q8:** Transformer ka core innovation kya hai purane models (RNN) ke comparison mein?
<details><summary>Answer</summary>
Parallel processing + Attention mechanism. RNN sequential tha (slow, long text bhool jaata tha). Transformer saara text ek saath dekhta hai.
</details>

**Q9:** Attention mechanism ek line mein?
<details><summary>Answer</summary>
Har word decide karta hai baaki words mein se kisko kitna dhyan dena hai. "it was tired" mein "it" ka attention "cat" pe high hoga.
</details>

**Q10:** Encoder vs Decoder — kab kya?
<details><summary>Answer</summary>
Encoder = input samajhna (BERT, classification/search). Decoder = output generate karna (GPT/Claude, text generation). Tu mostly decoder use karta hai.
</details>

---

## 🔵 LangChain & RAG (File 02)

**Q11:** LangChain kyun use karte hain? Bina iske kya problem hai?
<details><summary>Answer</summary>
Bina LangChain: har cheez manual (API call, prompt format, memory, error handling, model switch = code rewrite). LangChain: pre-built components, model switch = 1 line change. Terraform analogy: raw CLI vs Terraform modules.
</details>

**Q12:** Chain vs Agent — kya farak hai?
<details><summary>Answer</summary>
Chain = fixed path (A→B→C hamesha). Agent = dynamic path (AI DECIDE karta hai next kya karna hai based on situation). Chain = bash script, Agent = K8s operator.
</details>

**Q13:** LangChain vs LangGraph?
<details><summary>Answer</summary>
LangChain = linear chains. LangGraph = graphs with loops, conditions, retries. LangGraph jab decision-making, validation failures, multi-agent coordination chahiye.
</details>

**Q14:** RAG ke 5 steps bata.
<details><summary>Answer</summary>
1. Document Loading 2. Chunking (500-1000 chars, 200 overlap) 3. Embedding (text → numbers) 4. Storage (Vector DB) 5. Retrieval + Generation (query embed → similar chunks search → inject as context → LLM generates)
</details>

**Q15:** Chunking mein overlap kyun rakhte hain?
<details><summary>Answer</summary>
Bina overlap ke boundary pe information lost ho sakti hai. 200 char overlap se boundary context preserve hota hai.
</details>

**Q16:** RAG vs Fine-tuning — kab kya?
<details><summary>Answer</summary>
RAG = external knowledge at query time (easy to update, transparent, cheaper). Fine-tuning = retrain model on your data (better performance, expensive, hard to update). Most cases mein RAG enough hai.
</details>

**Q17:** Multi-agent mein Supervisor pattern kya hai?
<details><summary>Answer</summary>
Ek boss agent kaam distribute karta hai, worker agents apna specific kaam karte hain, boss results review karta hai. Tera IaC generator isi pattern pe hai — supervisor + 5 workers.
</details>

**Q18:** Memory ke 3 types bata aur kab kya use hota hai.
<details><summary>Answer</summary>
Buffer = sab yaad rakho (simple, expensive). Window = last N messages (practical, fixed cost). Summary = purani conversation ka summary (smart, context preserve + cost control). Healthcare chatbot mein window memory.
</details>

---

## 🟡 Interview Answers (File 04)

**Q19:** Apna IaC Generator 30 seconds mein explain kar.
<details><summary>Answer</summary>
Multi-agent GenAI system, LangGraph + Bedrock. Architecture description → production-ready Terraform. Supervisor pattern, 5 agents. 85% time reduction (6hr → 20min), 90% fewer config errors, 30% cost savings.
</details>

**Q20:** Healthcare Chatbot 30 seconds mein explain kar.
<details><summary>Answer</summary>
Serverless conversational AI, Bedrock + Lambda + API Gateway. 4 hospital API integrations. RAG with medical knowledge base. Safety filters for medical accuracy. Sub-second response, ~150-200 queries daily.
</details>

**Q21:** Voice Bot 30 seconds mein explain kar.
<details><summary>Answer</summary>
Real-time voice bot, Nova Sonic + Bedrock. Bidirectional WebSocket streaming. Parallel processing pipeline (not sequential). Sub-200ms first response latency. Docker + ECS deployment.
</details>

**Q22:** "How do you handle hallucination?" ka answer?
<details><summary>Answer</summary>
RAG for grounding, low temperature, output validation, source citation, guardrails. Healthcare chatbot mein sab use kiye + medical safety filters.
</details>

**Q23:** "How do you optimize GenAI costs?" ka answer?
<details><summary>Answer</summary>
Multi-layer caching (exact + semantic), model selection by task complexity, prompt optimization, token tracking with alerts, batch processing. 60-80% cost reduction possible.
</details>

**Q24:** Expected CTC puche toh kya bolna hai?
<details><summary>Answer</summary>
"Based on my production GenAI experience, AWS certification, and market rate for GenAI engineers in Bangalore, I'm targeting 14-16 LPA. Flexible based on overall package and growth." (Ask 14-16, settle at 12-13)
</details>

**Q25:** "Why leaving current company?" ka answer?
<details><summary>Answer</summary>
"Learned a lot, built production GenAI systems. Looking for deeper technical challenges and larger-scale AI systems. Want to grow into senior GenAI engineer." NEVER mention bond, salary, or anything negative.
</details>

---

## 🔴 System Design (File 04)

**Q26:** GenAI system design ka 4-step framework?
<details><summary>Answer</summary>
1. Requirements clarify (users, latency, accuracy, budget) 2. High-level architecture (boxes + GenAI components) 3. Deep dive (model selection, caching, scaling, monitoring) 4. Trade-offs (cost vs latency, accuracy vs speed)
</details>

**Q27:** Chatbot mein caching kaise kaam karta hai?
<details><summary>Answer</summary>
Layer 1: Exact match cache (Redis) — same question = same answer. Layer 2: Semantic cache — similar question = cached answer. Target 60-80% hit rate = 60-80% cost reduction.
</details>

**Q28:** RAG system mein vector DB ka hot/warm/cold tiering kya hai?
<details><summary>Answer</summary>
Hot (in-memory): most accessed chunks. Warm (SSD): next tier. Cold (disk): rarely accessed. Promotion/demotion based on access patterns. Like S3 storage classes.
</details>

---

## How to Use This File

1. **Daily (commute, 10 min):** Pick 10 random cards. Cover answer. Try to recall.
2. **Mark cards:** If you nail it → skip next time. If you blank → star it, revisit tomorrow.
3. **Weekly:** Go through all starred cards. If still blanking → re-read the source file section.
4. **Before interview:** Run through ALL cards. Anything you can't answer = study that topic.


---

## 🟠 ML Fundamentals (File 03) — Concept Level for 12L Roles

**Q29:** ML kya hai ek line mein? Traditional programming se kya farak?
<details><summary>Answer</summary>
Traditional: tu rules likhta hai, computer follow karta hai. ML: tu data deta hai, computer KHUD rules seekhta hai patterns se.
</details>

**Q30:** Supervised vs Unsupervised vs Reinforcement Learning?
<details><summary>Answer</summary>
Supervised = labeled data (input-output pairs, model seekhta hai predict karna). Unsupervised = no labels (model khud patterns/groups dhundhta hai). Reinforcement = agent actions leta hai, rewards/penalties milte hain, optimal strategy seekhta hai.
</details>

**Q31:** Supervised learning ke 2 types?
<details><summary>Answer</summary>
Classification = categories predict karna (spam/not spam). Regression = continuous value predict karna (house price).
</details>

**Q32:** Overfitting kya hai aur kaise fix karte hain?
<details><summary>Answer</summary>
Training data pe bahut accha but new data pe kharab. Fix: more data, regularization (L1/L2), dropout, simpler model. Analogy: ek opponent ke against perfect strategy but dusron pe fail.
</details>

**Q33:** Underfitting kya hai?
<details><summary>Answer</summary>
Training data pe bhi kharab. Model too simple hai. Fix: more complex model, more features, more training. Analogy: "always fold" strategy — simple but useless.
</details>

**Q34:** Bias-Variance tradeoff?
<details><summary>Answer</summary>
High bias = underfitting (too simple). High variance = overfitting (too complex). Goal = balance. Sweet spot where model generalizes well to new data.
</details>

**Q35:** Accuracy kyun misleading ho sakti hai?
<details><summary>Answer</summary>
Imbalanced data mein. 99% emails non-spam hain, model sab ko "not spam" bole = 99% accuracy but useless. Isliye Precision, Recall, F1 use karte hain.
</details>

**Q36:** Precision vs Recall?
<details><summary>Answer</summary>
Precision = jitne spam bole usme se kitne actually spam the ("jab bola spam, kitni baar sahi tha?"). Recall = total spam mein se kitne detect kiye ("kitne actual spam catch kiye?"). F1 = dono ka balance.
</details>

**Q37:** Fine-tuning kab use karoge RAG ke bajaye?
<details><summary>Answer</summary>
RAG = external knowledge at query time (easy update, cheaper, most cases). Fine-tuning = jab specific behavior/style chahiye jo RAG se nahi aa raha, jab domain bahut specialized hai. Fine-tuning expensive hai, good data chahiye, catastrophic forgetting ka risk.
</details>

**Q38:** Neural network kya hai simple mein?
<details><summary>Answer</summary>
Layers of mathematical functions. Input aata hai → multiple layers process karte hain (har layer kuch transform karta hai) → output nikalta hai. Factory assembly line analogy. Weights training mein adjust hote hain.
</details>

**Q39:** Gradient descent kya hai?
<details><summary>Answer</summary>
Optimization algorithm. Loss (error) calculate karo, gradient (steepest direction) nikalo, weights ko opposite direction mein adjust karo to reduce loss. Pahaad se neeche utarna — har step mein sabse steep direction mein.
</details>

**Q40:** Train-test split kyun karte hain?
<details><summary>Answer</summary>
80% data pe train, 20% pe test. Test data pe kabhi train mat karo (data leakage). Ye check karta hai ki model new unseen data pe kaise perform karta hai, not just memorized data pe.
</details>

**Q41:** RLHF kya hai aur LLMs se kaise related hai?
<details><summary>Answer</summary>
Reinforcement Learning from Human Feedback. LLMs pehle pre-train hote hain (next token prediction), phir RLHF se human preferences ke according fine-tune hote hain — helpful, harmless, honest banne ke liye. ChatGPT isi se polished hua.
</details>

**Q42:** GenAI system evaluate kaise karte ho?
<details><summary>Answer</summary>
Automated: BLEU, ROUGE (text quality), perplexity (model confidence). RAG-specific: retrieval precision, answer relevance, faithfulness. But end mein human evaluation sabse important. No single metric enough.
</details>
