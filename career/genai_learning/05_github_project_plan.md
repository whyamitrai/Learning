# GitHub Projects - Exactly Kya Banana Hai

> Ye 3 projects tujhe weekend mein banana hai. Bedrock free tier use kar. Har project ka goal: recruiter dekhke samjhe ki tu ye cheez production mein kar chuka hai.

---

## Project 1: `rag-chatbot-bedrock`

### Kya hai
A simple document Q&A chatbot using RAG with AWS Bedrock + ChromaDB.

### Kyun banana hai
RAG har GenAI JD mein hai. Ye project proves tu RAG samajhta hai end-to-end.

### Tech Stack
- AWS Bedrock (Titan Embeddings + Claude for generation)
- ChromaDB (vector store)
- LangChain (orchestration)
- FastAPI (API layer)
- Python

### Kya banana hai (scope tight rakh)
1. PDF/text documents load karo (3-4 sample docs — AWS docs, Terraform docs, whatever)
2. Chunk karo, embeddings banao via Bedrock Titan Embeddings
3. ChromaDB mein store karo
4. User question aaye → relevant chunks retrieve karo → Bedrock Claude se answer generate karo
5. FastAPI endpoint: POST /ask with question, returns answer + sources
6. Simple Streamlit UI (optional but impressive)

### README mein kya likho
```
# RAG Chatbot with AWS Bedrock

Document Q&A system using Retrieval-Augmented Generation.

## Architecture
User Question → Bedrock Titan Embeddings → ChromaDB Similarity Search 
→ Top 3 Chunks → Bedrock Claude → Grounded Answer + Sources

## Features
- PDF/text document ingestion with recursive chunking
- Bedrock Titan Embeddings for semantic search
- ChromaDB vector store with metadata filtering
- Bedrock Claude for context-grounded answer generation
- Source citation in every response
- FastAPI REST API

## Tech Stack
AWS Bedrock, ChromaDB, LangChain, FastAPI, Python

## Setup
[pip install instructions]
[AWS credentials setup]
[How to run]

## Architecture Diagram
[Simple text/mermaid diagram]
```

### Time estimate: 4-6 hours

---

## Project 2: `langgraph-multi-agent-demo`

### Kya hai
A multi-agent workflow using LangGraph where agents collaborate to analyze a topic and produce a report.

### Kyun banana hai
Tera IaC generator multi-agent hai. Ye project proves tu LangGraph aur multi-agent patterns jaanta hai. But company ka code nahi daal sakta, toh similar concept different domain mein.

### Tech Stack
- LangGraph (state graphs)
- AWS Bedrock (Claude)
- Python

### Kya banana hai
Theme: "Tech Research Assistant" — user ek topic de, agents research + analysis + report generate karein.

Agents:
1. **Research Agent**: Topic pe key points gather kare (Bedrock Claude)
2. **Analysis Agent**: Research output analyze kare, pros/cons nikale
3. **Writer Agent**: Final structured report likhe

LangGraph flow:
```
Start → Research Agent → Analysis Agent → Quality Check
                                              ↓
                                    (pass) → Writer Agent → Output
                                    (fail) → Research Agent (retry, max 2)
```

Ye conditional edge (quality check → retry) dikhata hai ki tu LangGraph ka real power samajhta hai — loops, conditions, not just linear chains.

### README mein kya likho
```
# Multi-Agent Research Assistant (LangGraph)

Collaborative AI agents that research, analyze, and write reports.

## Architecture
Supervisor pattern with 3 specialized agents connected via LangGraph state graph.
Includes conditional routing and retry logic for quality control.

## Agents
- Research Agent: Gathers key information on any topic
- Analysis Agent: Evaluates findings, identifies pros/cons/risks
- Writer Agent: Produces structured final report

## Key LangGraph Features Used
- State graphs with typed state
- Conditional edges (quality gate)
- Retry loops (max 2 retries on quality failure)
- Supervisor coordination pattern

## Tech Stack
LangGraph, AWS Bedrock (Claude), Python
```

### Time estimate: 4-5 hours

---

## Project 3: `bedrock-genai-toolkit`

### Kya hai
Collection of practical Bedrock utilities — model comparison, cost calculator, embedding benchmarks.

### Kyun banana hai
Shows depth of Bedrock knowledge. Not just "I called an API" but "I understand model selection, cost optimization, embedding quality."

### Tech Stack
- AWS Bedrock (multiple models)
- Python
- Boto3

### Kya banana hai
3-4 scripts/notebooks:

1. **model_comparison.py**: Same prompt ko Claude, Titan, Llama se run karo. Response quality, latency, cost compare karo. Output: comparison table.

2. **cost_calculator.py**: Input text de, ye bataye kitne tokens lagenge, har model pe kitna cost aayega. Practical utility.

3. **embedding_benchmark.py**: Titan Embeddings vs Cohere Embeddings — same documents pe similarity search quality compare karo.

4. **guardrails_demo.py**: Simple content filtering — block harmful queries, validate output quality.

### README mein kya likho
```
# AWS Bedrock GenAI Toolkit

Practical utilities for working with AWS Bedrock in production.

## Tools
1. Model Comparison — Compare Claude, Titan, Llama on quality/speed/cost
2. Cost Calculator — Estimate token usage and API costs before deployment
3. Embedding Benchmark — Compare embedding models for RAG quality
4. Guardrails Demo — Input/output safety filtering

## Why This Exists
In production GenAI, model selection and cost optimization matter as much as 
the AI logic itself. These tools help make data-driven decisions.

## Tech Stack
AWS Bedrock, Boto3, Python
```

### Time estimate: 3-4 hours

---

## Total Time: 1.5 to 2 weekends

Weekend 1: Project 1 (RAG chatbot) — ye sabse important hai
Weekend 2: Project 2 (LangGraph) + Project 3 (toolkit)

## GitHub Profile README

Apne GitHub profile pe ek README.md bana:

```
# Hi, I'm Amit Rai 👋

GenAI Developer | AWS Certified | Building AI-powered systems on AWS Bedrock

## What I Build
- Multi-agent AI systems with LangGraph
- RAG pipelines for enterprise document Q&A
- Real-time voice bots with AWS Nova Sonic
- Cloud infrastructure automation with Terraform

## Tech Stack
Python | LangChain | LangGraph | AWS Bedrock | RAG | ChromaDB | 
Terraform | Docker | FastAPI

## Currently
- Building GenAI solutions at Rapyder Cloud Solutions
- Exploring ML fundamentals and fine-tuning
```

---

## Important Rules

1. **Company ka code KABHI mat daalo.** Ye termination + legal issue hai.
2. Simplified/demo versions bana jo SAME CONCEPTS demonstrate karein.
3. Har repo mein README MUST hai. Recruiter code nahi padhta, README padhta hai.
4. Clean code with comments. No jupyter notebook dumps.
5. .env.example file rakh (credentials template without actual keys).
6. Architecture diagram har repo mein (even text-based is fine).
