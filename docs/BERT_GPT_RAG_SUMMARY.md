# BERT, GPT, and RAG: 10-Hour Module Summary

## Overview

This module covers modern transformer-based NLP across three folders (12-BERT, 13-GPT, 14-RAG) for a comprehensive 10-hour learning experience focused on understanding encoders, decoders, and real-world applications with strong emphasis on **quantitative metrics**.

---

## Folder Structure

```
12-BERT/ (Encoder Models - 2 hours)
├── NLP12_1_Classification.ipynb (1.5h)  Existing, perfect
└── NLP12_2_Q&A.ipynb (0.5h)  Enhanced with EM & F1 metrics

13-GPT/ (Decoder Models - 2 hours)
└── NLP13_1_Text_Generation.ipynb (2h)  NEW

14-RAG/ (Real-World Applications - 5 hours)
├── NLP14_1_RAG_Pipeline.ipynb (3h)  NEW
└── NLP14_2_Modern_LLMs.ipynb (2h)  NEW

Plus: BERT Theory slides (1 hour)
Total: 10 hours
```

---

## Detailed Notebook Breakdown

### **12-BERT: Encoder Models** (2 hours)

#### NLP12_1_Classification.ipynb  (1.5h)
- **Status**: Existing notebook, already perfect
- **Content**: Fine-tuning BERT for sentiment analysis
- **Metrics**:  Complete (Accuracy, Precision, Recall, F1, Confusion Matrix, ROC)

#### NLP12_2_Q&A.ipynb  (0.5h)
- **Status**: Enhanced with metrics section
- **Original**: Basic Q&A inference demo
- **Added**:
  -  Exact Match (EM) metric implementation
  -  F1 Score calculation (token-level overlap)
  -  Confidence score analysis
  -  Multi-example evaluation
  -  Average performance tracking

---

### **13-GPT: Decoder Models** (2 hours)

#### NLP13_1_Text_Generation.ipynb  (2h)
**Structure:**
1. **Introduction** (15 min)
   - BERT vs GPT architecture comparison
   - Autoregressive generation explained

2. **Setup & Basic Generation** (25 min)
   - Load GPT-2 model
   - Greedy decoding demonstration
   - Limitations of greedy approach

3. **Sampling Strategies** (30 min)
   - Temperature sampling (0.3 → 2.0)
   - Top-k sampling (k=10, 50, 100)
   - Top-p (nucleus) sampling (p=0.9, 0.95)
   - Combined strategies

4. **Generation Metrics**  (35 min)
   - **Perplexity**: Model confidence measurement
   - **Distinct-n**: Diversity metrics (unique n-grams)
   - **Self-BLEU**: Inter-sample similarity
   - **BLEU Score**: For paraphrasing/translation tasks
   - **ROUGE Score**: For summarization tasks
   - **Human Evaluation Framework**: Fluency, coherence, relevance

5. **Quantitative Analysis** (20 min)
   - Strategy comparison table
   - Temperature vs diversity visualization
   - Performance benchmarking

6. **BERT vs GPT Comparison** (15 min)
   - Side-by-side architecture
   - Task suitability matrix
   - Decision tree for model selection

7. **Practical Insights** (10 min)
   - Use cases and limitations
   - Cost-performance tradeoffs
   - Bridge to RAG

**Key Metrics Covered:**
-  Perplexity (lower = better)
-  Distinct-1/2/3 (diversity)
-  Self-BLEU (lower = more diverse)
-  BLEU/ROUGE (task-specific)
-  Inference time

---

### **14-RAG: Real-World Applications** (5 hours)

#### NLP14_1_RAG_Pipeline.ipynb  (3h)
**Structure:**
1. **Introduction** (10 min)
   - Why RAG? (hallucination, no external knowledge)
   - RAG architecture: Retrieve → Augment → Generate

2. **Knowledge Base Setup** (10 min)
   - Sample document collection
   - Data structure

3. **Retrieval System** (40 min)
   - Sentence-BERT embeddings
   - FAISS vector database
   - Semantic search implementation
   - Retrieval testing

4. **Augmentation** (15 min)
   - Prompt engineering
   - Context integration

5. **Generation** (20 min)
   - GPT-2 integration
   - Answer generation

6. **Complete RAG Pipeline** (20 min)
   - End-to-end implementation
   - Multi-step processing

7. **Retrieval Metrics**  (35 min)
   - **Precision@K**: Relevant docs in top-K
   - **Recall@K**: Coverage of relevant docs
   - **MRR (Mean Reciprocal Rank)**: First relevant doc position
   - **NDCG**: Ranking quality with discounting

8. **Generation Quality Metrics**  (25 min)
   - **Faithfulness**: Answer grounded in context
   - **Answer Relevance**: Semantic similarity to question
   - **Answer Correctness**: Comparison to ground truth

9. **End-to-End Evaluation** (20 min)
   - Complete pipeline testing
   - Multi-dimensional metric tracking
   - Visualization of results

10. **Performance Analysis** (20 min)
    - **Latency breakdown**: Retrieval vs generation
    - **Cost analysis**: Token usage, API costs
    - Optimization strategies

11. **Practical Insights** (15 min)
    - When to use RAG
    - RAG vs fine-tuning comparison
    - Production considerations

**Key Metrics Covered:**
-  Precision@K, Recall@K
-  MRR (Mean Reciprocal Rank)
-  NDCG (Normalized Discounted Cumulative Gain)
-  Faithfulness score
-  Answer relevance
-  Semantic similarity
-  Latency (ms)
-  Cost per query

---

#### NLP14_2_Modern_LLMs.ipynb  (2h)
**Structure:**
1. **Modern LLM Landscape** (15 min)
   - Model comparison table (GPT-4, Claude, LLaMA, Mistral)
   - Capability evolution
   - When to use what?

2. **API Setup** (10 min)
   - OpenAI/Anthropic configuration
   - Mock mode for education

3. **Working with APIs** (15 min)
   - Basic chat completion
   - Token counting
   - Cost tracking

4. **Prompt Engineering** (30 min)
   - Basic principles (specific, context, examples, format)
   - Bad vs good prompts comparison
   - Few-shot learning (zero-shot vs few-shot)
   - Chain-of-thought prompting

5. **LLM Evaluation Framework**  (35 min)
   - **Task-specific evaluation**: Accuracy on test sets
   - **Model comparison**: GPT-3.5 vs GPT-4 vs BERT
     - Accuracy
     - Latency (ms)
     - Cost per 1K queries
   - **LLM-as-judge**: Using LLM to evaluate outputs
   - Visualization of tradeoffs

6. **Cost-Performance Optimization** (20 min)
   - Monthly cost projections at scale
   - Optimization strategies table
   - ROI analysis

7. **Decision Framework** (10 min)
   - When to fine-tune vs use API
   - Decision tree flowchart
   - Special considerations

8. **Production Best Practices** (10 min)
   - Error handling & retries
   - Monitoring checklist
   - Safety & content filtering

9. **Benchmark Suites** (5 min)
   - MMLU, HellaSwag, GSM8K, HumanEval
   - State-of-the-art scores

**Key Metrics Covered:**
-  Accuracy (task-specific)
-  Latency (ms)
-  Cost per query ($)
-  Cost per 1K queries
-  Monthly cost projections
-  LLM-as-judge scores (1-5 scale)
-  Benchmark performance (MMLU, etc.)

---

## Metrics Summary: Complete Coverage

### Classification (BERT - NLP12_1) 
- Accuracy, Precision, Recall, F1 (macro/micro/weighted)
- Confusion Matrix
- ROC Curves
- Per-class performance

### Question Answering (BERT - NLP12_2) 
- **Exact Match (EM)**: Binary correctness
- **F1 Score**: Token-level overlap
- **Confidence Scores**: Logit-based confidence

### Text Generation (GPT - NLP13_1) 
- **Perplexity**: Model confidence (lower is better)
- **Distinct-1/2/3**: Diversity (unique n-grams %)
- **Self-BLEU**: Inter-sample similarity (lower = more diverse)
- **BLEU**: N-gram overlap (translation/paraphrasing)
- **ROUGE**: Recall-oriented (summarization)
- **Inference Time**: Performance measurement

### Retrieval-Augmented Generation (RAG - NLP14_1) 
**Retrieval:**
- **Precision@K**: Relevant docs in top-K
- **Recall@K**: Coverage of all relevant docs
- **MRR**: Mean Reciprocal Rank (first relevant position)
- **NDCG**: Ranking quality with position discount

**Generation:**
- **Faithfulness**: Context grounding
- **Answer Relevance**: Semantic similarity to query
- **Answer Correctness**: Ground truth comparison
- **Latency**: End-to-end time
- **Cost**: Token usage and API cost

### Modern LLMs (API-based - NLP14_2) 
- **Accuracy**: Task-specific correctness
- **Latency**: Response time (ms)
- **Cost**: Per query and per 1K queries ($)
- **Monthly Projections**: Scaling costs
- **LLM-as-judge**: Multi-criteria evaluation (1-5)
- **Benchmark Scores**: MMLU, HellaSwag, GSM8K

---

## Student Learning Outcomes

By the end of this module, students will be able to:

### Technical Skills
1.  **Implement BERT** for classification and extractive Q&A
2.  **Use GPT** for text generation with controlled sampling
3.  **Build RAG pipelines** combining retrieval and generation
4.  **Work with modern LLM APIs** (OpenAI, Anthropic)
5.  **Apply prompt engineering** techniques effectively

### Evaluation & Metrics
6.  **Calculate and interpret** EM, F1, Precision, Recall
7.  **Measure generation quality** with perplexity, BLEU, ROUGE, diversity
8.  **Evaluate retrieval systems** using Precision@K, MRR, NDCG
9.  **Assess RAG pipelines** end-to-end with multiple metrics
10.  **Perform cost-benefit analysis** for model selection

### Decision Making
11.  **Choose appropriate models** for different tasks (BERT vs GPT vs LLM APIs)
12.  **Optimize for production** (cost, latency, quality tradeoffs)
13.  **Evaluate tradeoffs** between fine-tuning and API usage
14.  **Design evaluation frameworks** for subjective tasks

---

## Why This Structure Works for Quantitative Students

1. **Every notebook has concrete metrics**
   - Not just "it works" but "how well does it work?"
   - Quantifiable performance measures throughout

2. **Comparative analysis**
   - Side-by-side model comparisons
   - Cost vs accuracy vs latency tradeoffs
   - Clear decision frameworks

3. **Real-world considerations**
   - Production costs at scale
   - Latency requirements
   - ROI analysis

4. **Visualization of metrics**
   - Charts and tables throughout
   - Performance dashboards
   - Trend analysis

5. **Statistical rigor**
   - Average metrics across test sets
   - Confidence scores and calibration
   - Error analysis

---

## Connection to Final Projects

Students can apply these skills to their projects:

1. **Classification tasks** → Use BERT fine-tuning (NLP12_1 as template)
2. **Extractive Q&A** → Use BERT Q&A (NLP12_2 as template)
3. **Text generation** → Use GPT techniques (NLP13_1 as template)
4. **Document Q&A** → Build RAG system (NLP14_1 as template)
5. **Zero-shot tasks** → Use LLM APIs (NLP14_2 as template)

All with proper metrics and evaluation frameworks!

---

## Time Allocation Summary

| Module | Topic | Time | Metrics Focus |
|--------|-------|------|---------------|
| **BERT Theory** | Slides | 1h | Architecture understanding |
| **12-BERT** | Classification | 1.5h |  Precision, Recall, F1, ROC |
| **12-BERT** | Q&A | 0.5h |  EM, F1, Confidence |
| **13-GPT** | Generation | 2h |  Perplexity, Diversity, BLEU/ROUGE |
| **14-RAG** | Pipeline | 3h |  Retrieval + Generation metrics |
| **14-RAG** | Modern LLMs | 2h |  Cost, Latency, Quality tradeoffs |
| **Total** | | **10h** | **Complete metric coverage** |

---

## Instructor Notes

### What's Ready to Use
-  All 3 new notebooks created and structured
-  NLP12_2 enhanced with metrics
-  Complete code examples throughout
-  Visualizations and tables included
-  Exercises embedded in notebooks

### Before Class
1. Test all notebooks in Google Colab
2. Prepare API keys for NLP14_2 (or use mock mode)
3. Review metric calculations for Q&A
4. Prepare BERT theory slides (1 hour content)

### During Class
- **Emphasize metrics** at every stage
- **Show visualizations** of tradeoffs
- **Discuss cost implications** for real-world use
- **Connect to their projects** frequently

### Common Questions to Prepare For
1. "When should I fine-tune vs use an API?" → See NLP14_2 decision tree
2. "How much will this cost at scale?" → See cost projections in NLP14_2
3. "Which metric should I use?" → Each notebook explains when to use which
4. "Can I combine BERT and GPT?" → Yes! That's RAG (NLP14_1)

---

## Next Steps / Future Enhancements

Optional additions if time permits:
- Add slide decks matching notebooks
- Create exercise solutions
- Add more diverse datasets
- Include multimodal examples (CLIP, vision)
- Add deployment section (Docker, FastAPI)

---

**Created:** 2026-03-01
**Status:**  Complete and ready for delivery
**Total Development Time:** ~3 hours
**Student Learning Time:** 10 hours
**Metrics Coverage:** Comprehensive across all models
