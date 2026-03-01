# Module 13: GPT - Decoder Models

**Duration**: 2 hours
**Focus**: Text generation with decoder-only transformers

---

## Overview

This module explores decoder-only transformer models like GPT (Generative Pre-trained Transformer) for autoregressive text generation. Students learn controlled sampling strategies and how to measure generation quality quantitatively.

---

## Notebooks

### NLP13_1_Text_Generation.ipynb (2 hours)

**Topics Covered:**
1. Introduction to decoder architecture (15 min)
   - BERT vs GPT comparison
   - Autoregressive generation explained
   - Use cases: completion, creative writing, code generation

2. Basic text generation (25 min)
   - Load GPT-2 model
   - Greedy decoding demonstration
   - Limitations of deterministic approaches

3. Sampling strategies (30 min)
   - Temperature sampling (0.1 → 2.0)
   - Top-k sampling (k=10, 50, 100)
   - Top-p (nucleus) sampling (p=0.9, 0.95)
   - Combined strategies for production

4. Generation metrics (35 min)
   - Perplexity: Model confidence measurement
   - Distinct-n: Diversity metrics (unique n-grams)
   - Self-BLEU: Inter-sample similarity
   - BLEU Score: For translation/paraphrasing
   - ROUGE Score: For summarization
   - Human evaluation framework

5. Quantitative analysis (20 min)
   - Strategy comparison tables
   - Temperature vs diversity visualizations
   - Performance benchmarking
   - Cost-performance tradeoffs

6. BERT vs GPT comparison (15 min)
   - Side-by-side architecture
   - Task suitability matrix
   - Decision tree for model selection

7. Practical insights (10 min)
   - Use cases and limitations
   - Cost considerations
   - Bridge to RAG (Module 14)

---

## Key Metrics

Students will learn to calculate and interpret:

- **Perplexity**: Lower values indicate better model confidence
- **Distinct-1/2/3**: Measures uniqueness (higher = more diverse)
- **Self-BLEU**: Lower values indicate more diverse outputs
- **BLEU/ROUGE**: Task-specific quality measures
- **Inference Time**: Performance measurement

---

## Learning Outcomes

By completing this module, students will be able to:

1. Implement text generation with GPT-2
2. Apply different sampling strategies effectively
3. Measure generation quality with multiple metrics
4. Compare BERT (encoder) vs GPT (decoder) architectures
5. Make informed decisions about when to use generation models
6. Understand cost-performance tradeoffs

---

## Prerequisites

- Module 11: Transformers architecture
- Module 12: BERT (for comparison)
- Understanding of attention mechanisms
- Basic PyTorch/Transformers library knowledge

---

## Required Packages

```python
pip install transformers datasets torch numpy pandas matplotlib seaborn
```

---

## Connection to Other Modules

**From Module 12 (BERT):**
- Contrast encoder-only vs decoder-only
- Compare use cases: understanding vs generation

**To Module 14 (RAG):**
- Generation component of RAG pipeline
- Combining retrieval with generation
- Addressing hallucination problems

---

## Instructor Notes

**Preparation:**
- Test notebook in Colab
- Review metric calculations
- Prepare examples of good/bad generations
- Have backup examples if generation takes too long

**Teaching Tips:**
- Emphasize metrics at every step
- Show live generation with different temperatures
- Discuss hallucination problem (leads to RAG)
- Connect to real-world applications

**Common Student Questions:**
- "Why not always use GPT for everything?" → Discuss cost, latency, task suitability
- "How do I choose temperature?" → Show diversity vs coherence tradeoff
- "Can GPT do classification?" → Yes, but BERT is better/cheaper for it

---

## Additional Resources

- [GPT-2 Paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Nucleus Sampling Paper](https://arxiv.org/abs/1904.09751)
- [Hugging Face Generation Guide](https://huggingface.co/docs/transformers/main_classes/text_generation)

---

**Module 13** | Data Visualization and Text Mining
Università Cattolica del Sacro Cuore | Academic Year 2025-2026
