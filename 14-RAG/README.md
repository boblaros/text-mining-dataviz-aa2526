# Module 14: RAG & Modern LLMs

**Duration**: 5 hours
**Focus**: Real-world applications combining retrieval and generation

---

## Overview

This module covers production-ready NLP systems, including Retrieval-Augmented Generation (RAG) pipelines and modern LLM APIs. Students learn to build systems that combine the strengths of retrieval and generation while measuring performance comprehensively.

---

## Notebooks

### NLP14_1_RAG_Pipeline.ipynb (3 hours)

Complete implementation of a RAG system from scratch.

**Topics Covered:**

1. Introduction (10 min)
   - Why RAG? Solving hallucination and knowledge cutoff
   - RAG architecture: Retrieve → Augment → Generate

2. Knowledge base setup (10 min)
   - Document collection structure
   - Sample dataset preparation

3. Retrieval system (40 min)
   - Sentence-BERT embeddings
   - FAISS vector database
   - Semantic search implementation
   - Testing retrieval quality

4. Augmentation (15 min)
   - Prompt engineering for RAG
   - Context integration strategies

5. Generation (20 min)
   - GPT-2 integration
   - Answer synthesis

6. Complete pipeline (20 min)
   - End-to-end implementation
   - Multi-step processing
   - Error handling

7. Retrieval metrics (35 min)
   - Precision@K: Relevant docs in top-K
   - Recall@K: Coverage of relevant docs
   - MRR: Mean Reciprocal Rank
   - NDCG: Ranking quality

8. Generation quality metrics (25 min)
   - Faithfulness: Context grounding
   - Answer Relevance: Semantic similarity
   - Answer Correctness: Ground truth comparison

9. End-to-end evaluation (20 min)
   - Complete pipeline testing
   - Multi-dimensional metrics
   - Visualization of results

10. Performance analysis (20 min)
    - Latency breakdown (retrieval vs generation)
    - Cost analysis (tokens, API calls)
    - Optimization strategies

11. Practical insights (15 min)
    - When to use RAG
    - RAG vs fine-tuning comparison
    - Production considerations

**Key Metrics:**
- Precision@K, Recall@K, MRR, NDCG
- Faithfulness, Answer Relevance, Correctness
- Latency (ms), Cost per query

---

### NLP14_2_Modern_LLMs.ipynb (2 hours)

Working with production LLM APIs and evaluation frameworks.

**Topics Covered:**

1. Modern LLM landscape (15 min)
   - Model comparison (GPT-4, Claude, LLaMA, Mistral)
   - Capability evolution
   - When to use what?

2. API setup (10 min)
   - OpenAI/Anthropic configuration
   - Mock mode for education

3. API integration (15 min)
   - Basic chat completion
   - Token counting
   - Cost tracking

4. Prompt engineering (30 min)
   - Best practices (specific, context, examples, format)
   - Bad vs good prompts
   - Few-shot learning (zero-shot vs few-shot)
   - Chain-of-thought prompting

5. LLM evaluation framework (35 min)
   - Task-specific evaluation
   - Model comparison (GPT-3.5 vs GPT-4 vs BERT)
   - LLM-as-judge methodology
   - Visualization of tradeoffs

6. Cost-performance optimization (20 min)
   - Monthly cost projections
   - Optimization strategies
   - ROI analysis

7. Decision framework (10 min)
   - Fine-tune vs API decision tree
   - Special considerations

8. Production best practices (10 min)
   - Error handling & retries
   - Monitoring checklist
   - Safety & content filtering

9. Benchmark suites (5 min)
   - MMLU, HellaSwag, GSM8K, HumanEval
   - State-of-the-art scores

**Key Metrics:**
- Accuracy, Latency (ms), Cost ($)
- Monthly cost projections
- LLM-as-judge scores (1-5 scale)
- Benchmark performance

---

## Learning Outcomes

By completing this module, students will be able to:

**RAG Systems:**
1. Build complete RAG pipelines with vector databases
2. Implement semantic search with embeddings
3. Evaluate retrieval quality (Precision@K, MRR, NDCG)
4. Measure generation quality (faithfulness, relevance)
5. Optimize for latency and cost

**Modern LLMs:**
6. Integrate GPT-4/Claude APIs into applications
7. Apply prompt engineering techniques effectively
8. Perform cost-benefit analysis for model selection
9. Evaluate LLMs systematically
10. Make data-driven decisions (fine-tune vs API)

---

## Prerequisites

- Module 12: BERT (encoder models)
- Module 13: GPT (decoder models)
- Understanding of embeddings (Module 04)
- Basic knowledge of vector databases
- Python programming proficiency

---

## Required Packages

```python
# For NLP14_1_RAG_Pipeline.ipynb
pip install transformers sentence-transformers faiss-cpu torch numpy pandas matplotlib

# For NLP14_2_Modern_LLMs.ipynb
pip install openai anthropic tiktoken pandas numpy matplotlib
```

**Note:** For NLP14_2, you can run in mock mode without API keys for educational purposes.

---

## Connection to Other Modules

**From Module 12 (BERT):**
- Use BERT embeddings for retrieval
- Compare BERT Q&A vs RAG

**From Module 13 (GPT):**
- Use GPT for generation component
- Apply sampling strategies learned

**To Student Projects:**
- RAG pipeline for document Q&A
- Cost analysis for project planning
- Evaluation frameworks for project metrics

---

## Instructor Notes

### NLP14_1_RAG_Pipeline

**Preparation:**
- Test FAISS installation
- Prepare sample documents
- Review metric implementations
- Have backup data if needed

**Teaching Tips:**
- Emphasize each component separately first
- Show how pieces fit together
- Discuss real-world applications (customer support, research assistants)
- Compare to pure generation (show hallucination examples)

**Common Student Questions:**
- "Why not just use GPT-4?" → Cost, hallucination, no citations
- "How many documents to retrieve?" → Discuss K selection
- "Can I use my own documents?" → Yes, show how to adapt

### NLP14_2_Modern_LLMs

**Preparation:**
- Get API keys OR use mock mode
- Prepare cost comparison tables
- Review current pricing (changes frequently)
- Have recent benchmark scores

**Teaching Tips:**
- Start with mock mode to avoid API issues
- Emphasize cost at scale
- Show real pricing examples
- Discuss when fine-tuning makes sense

**Common Student Questions:**
- "Should I use GPT-4 for my project?" → Discuss budget and requirements
- "Can I run these models locally?" → Discuss LLaMA, Mistral options
- "How do I get API keys?" → Provide links, warn about costs

---

## Cost Considerations

**Important:** This module involves API costs. Options:

1. **Mock Mode** (Recommended for teaching)
   - No API keys needed
   - Simulated responses
   - Learn concepts without costs

2. **Shared API Keys** (Small classes)
   - Set spending limits
   - Monitor usage
   - Estimated cost: $5-10 per class session

3. **Student Keys** (Advanced courses)
   - Students get their own keys
   - Educational credits available
   - Good for project work

---

## Real-World Applications

Students will see how RAG is used in:
- Customer support chatbots
- Document Q&A systems
- Research assistants
- Legal/medical information retrieval
- Knowledge base querying

---

## Additional Resources

### Papers
- [RAG: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020)
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) (Wei et al., 2022)

### Documentation
- [LangChain RAG Guide](https://python.langchain.com/docs/use_cases/question_answering/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss/wiki)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Anthropic Claude Docs](https://docs.anthropic.com/)

### Tools
- [Pinecone Learning Center](https://www.pinecone.io/learn/)
- [Hugging Face Hub](https://huggingface.co/)

---

## Assessment Ideas

**For RAG Pipeline:**
- Build a Q&A system for a specific domain
- Evaluate with metrics (EM, F1, Precision@K)
- Compare to baseline (no retrieval)

**For Modern LLMs:**
- Compare GPT-3.5 vs GPT-4 on a task
- Calculate costs for 1000 queries
- Design an evaluation framework

---

**Module 14** | Data Visualization and Text Mining
Università Cattolica del Sacro Cuore | Academic Year 2025-2026
