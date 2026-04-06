# Code Practice - Hands-On Exercises

> Ye folder actual coding practice ke liye hai. Concepts pehle padh (01-04 files), phir yahan aake code kar.

## Structure

```
code_practice/
├── 01_basic_llm_calls/       → OpenAI/Bedrock API calls, temperature experiments
├── 02_langchain_chains/      → Chains, prompts, memory
├── 03_rag_from_scratch/      → Document loading, chunking, embeddings, search
├── 04_agents_and_tools/      → ReAct agents, custom tools
├── 05_langgraph_workflows/   → State graphs, multi-agent systems
├── 06_production_patterns/   → FastAPI wrapper, Docker, caching
├── 07_ml_basics/             → Scikit-learn, pandas, basic models
```

## How To Use

1. Pehle concept file padh (01_genai_foundations.md, etc.)
2. Phir corresponding practice folder mein jaa
3. Har folder mein `exercises.py` hoga with TODO comments
4. Code likh, run kar, experiment kar
5. Solutions folder mein reference answers honge

## Setup

```bash
pip install langchain langchain-openai chromadb fastapi uvicorn boto3 scikit-learn pandas numpy
```

## Rules
- Copy-paste mat kar. Khud likh.
- Agar stuck ho, 15 min try kar pehle. Phir solution dekh.
- Har exercise ke baad apne words mein explain kar kya hua.
- Variations try kar (different prompts, different models, different data).
