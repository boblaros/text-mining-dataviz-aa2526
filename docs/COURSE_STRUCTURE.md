# Complete Course Structure

## Data Visualization and Text Mining
**Università Cattolica del Sacro Cuore** | Academic Year 2025-2026

---

##  Course Overview

This course covers the complete journey from basic NLP to state-of-the-art transformer models and production-ready systems.

### Total: 14 Modules | 40+ Notebooks

---

##  Module Structure

```
text-mining-dataviz-aa2526/
│
├── 01-NLP_In_Practice/              [10 notebooks] Basics
├── 02-Text_Classification/          [4 notebooks]  ML for Text
├── 03-Neural_Networks/              [2 notebooks]  Deep Learning Intro
├── 04-Embeddings/                   [4 notebooks]  Word Vectors
├── 05-LSTM/                         [3 notebooks]  Recurrent Networks
├── 06-Topic_Modeling/               [4 notebooks]  Unsupervised Methods
├── 07-Data_Visualization/           [6 notebooks]  Plotting & Viz
├── 08-Dashboards/                   [6+ files]     Interactive Apps
├── 09-Transfer_Learning/            [2 notebooks]  Pre-training Concepts
├── 10-Attention/                    [1 notebook]   Attention Mechanism
├── 11-Transformers/                 [2 notebooks]  Transformer Architecture
│
├── 12-BERT/                         [2 notebooks]   Encoder Models
│   ├── NLP12_1_Classification.ipynb              (1.5h)
│   └── NLP12_2_Q&A.ipynb                         (0.5h)
│
├── 13-GPT/                          [1 notebook]    Decoder Models
│   └── NLP13_1_Text_Generation.ipynb             (2h)
│
└── 14-RAG/                          [2 notebooks]   Applications
    ├── NLP14_1_RAG_Pipeline.ipynb                (3h)
    └── NLP14_2_Modern_LLMs.ipynb                 (2h)
```

**NOTE:** Modules 12-14 are NEW (10 hours total) focused on modern transformers

---

##  Learning Path

### Phase 1: Foundations (Modules 01-06)
**Build your NLP toolkit**

```
Module 01: NLP In Practice
  └─→ Tokenization, POS, NER, EDA
       │
Module 02: Text Classification
  └─→ BoW, TF-IDF, scikit-learn
       │
Module 03: Neural Networks
  └─→ Keras, PyTorch basics
       │
Module 04: Embeddings
  └─→ Word2Vec, GloVe, Sentence-BERT
       │
Module 05: LSTM
  └─→ Text generation, sentiment, NER
       │
Module 06: Topic Modeling
  └─→ LDA, NMF, BERTopic
```

### Phase 2: Visualization & Applications (Modules 07-08)
**Communicate your findings**

```
Module 07: Data Visualization
  └─→ Matplotlib, Plotly, maps
       │
Module 08: Dashboards
  └─→ Dash, callbacks, interactive apps
```

### Phase 3: Advanced Deep Learning (Modules 09-11)
**Modern architectures**

```
Module 09: Transfer Learning
  └─→ Feature extraction, fine-tuning, ULMFit
       │
Module 10: Attention Mechanisms
  └─→ Bahdanau attention, seq2seq
       │
Module 11: Transformers
  └─→ Self-attention, multi-head, Hugging Face
```

### Phase 4: State-of-the-Art (Modules 12-14)
**Production-ready systems**

```
Module 12: BERT (Encoder Models)
  ├─→ Classification with metrics
  └─→ Q&A with EM & F1
       │
Module 13: GPT (Decoder Models)
  └─→ Text generation, sampling, perplexity
       │
Module 14: RAG & Modern LLMs
  ├─→ RAG pipeline with vector DB
  └─→ GPT-4, Claude, prompt engineering
```

---

##  Module 12-14: Deep Dive (10 Hours)

### Module 12: BERT - Understanding (2h)

**12.1 - Text Classification** (1.5h)
```
What You'll Learn:
├── Fine-tuning BERT for sentiment analysis
├── Hugging Face Trainer API
└── Comprehensive metrics
    ├── Accuracy, Precision, Recall
    ├── F1 (macro, micro, weighted)
    ├── Confusion Matrix
    └── ROC Curves

Key Takeaway: BERT excels at understanding tasks
```

**12.2 - Question Answering** (0.5h)
```
What You'll Learn:
├── Extractive Q&A with BERT
├── Span prediction (start/end tokens)
├── Exact Match (EM) metric
├── F1 score calculation
└── Confidence scoring

Key Takeaway: BERT can extract precise answers from text
```

---

### Module 13: GPT - Generation (2h)

**13.1 - Text Generation**
```
What You'll Learn:
├── Autoregressive generation
├── Sampling strategies
│   ├── Temperature (0.1 → 2.0)
│   ├── Top-k sampling
│   └── Top-p (nucleus) sampling
├── Generation metrics
│   ├── Perplexity (confidence)
│   ├── Distinct-n (diversity)
│   ├── Self-BLEU
│   ├── BLEU (translation)
│   └── ROUGE (summarization)
├── BERT vs GPT comparison
└── Practical applications

Key Takeaway: GPT excels at creative generation
```

---

### Module 14: Real-World Applications (5h)

**14.1 - RAG Pipeline** (3h)
```
Complete RAG Implementation:

1. RETRIEVAL
   ├── Sentence-BERT embeddings
   ├── FAISS vector database
   ├── Semantic search
   └── Metrics: Precision@K, Recall@K, MRR, NDCG

2. AUGMENTATION
   ├── Prompt engineering
   └── Context integration

3. GENERATION
   ├── GPT-2 integration
   └── Answer synthesis

End-to-End Metrics:
├── Retrieval quality
├── Generation quality (faithfulness, relevance)
├── Latency (ms)
└── Cost per query ($)

Key Takeaway: RAG combines retrieval + generation for grounded answers
```

**14.2 - Modern LLMs** (2h)
```
Production-Ready Skills:

├── API Integration
│   ├── OpenAI (GPT-4, GPT-3.5)
│   └── Anthropic (Claude)
│
├── Prompt Engineering
│   ├── Zero-shot vs Few-shot
│   ├── Chain-of-thought
│   └── Best practices
│
├── Evaluation Framework
│   ├── Task-specific metrics
│   ├── LLM-as-judge
│   └── Benchmark suites (MMLU, HellaSwag)
│
├── Cost-Performance Optimization
│   ├── Model selection (GPT-3.5 vs GPT-4 vs BERT)
│   ├── Monthly cost projections
│   └── Optimization strategies
│
└── Decision Framework
    ├── When to fine-tune
    ├── When to use APIs
    └── When to use RAG

Key Takeaway: Make data-driven decisions for production systems
```

---

##  Complete Metrics Coverage

### Classification Tasks
```
- Accuracy                    (overall correctness)
- Precision                   (positive predictive value)
- Recall                      (sensitivity)
- F1 Score                    (harmonic mean of P&R)
- Macro/Micro/Weighted F1     (multi-class handling)
- Confusion Matrix            (error patterns)
- ROC Curves / AUC            (threshold analysis)
- Per-class Performance       (class-specific metrics)
```

### Question Answering
```
- Exact Match (EM)            (binary correctness)
- F1 Score                    (token-level overlap)
- Confidence Scores           (model certainty)
```

### Text Generation
```
- Perplexity                  (model confidence, lower is better)
- Distinct-1/2/3              (unique n-grams, diversity)
- Self-BLEU                   (inter-sample similarity)
- BLEU                        (n-gram overlap for translation)
- ROUGE-1/2/L                 (recall for summarization)
- Inference Time              (latency in ms)
```

### Retrieval (RAG)
```
- Precision@K                 (relevant docs in top-K)
- Recall@K                    (coverage of relevant docs)
- MRR                         (Mean Reciprocal Rank)
- NDCG                        (Normalized Discounted Cumulative Gain)
```

### Generation Quality (RAG)
```
- Faithfulness                (grounded in context)
- Answer Relevance            (addresses question)
- Answer Correctness          (vs ground truth)
- Context Relevance           (retrieved docs useful)
```

### Production Metrics (LLMs)
```
- Accuracy                    (task-specific)
- Latency                     (response time in ms)
- Cost per Query              (API pricing)
- Cost per 1K Queries         (scaling costs)
- Monthly Projections         (budget planning)
- Tokens Used                 (input + output)
- LLM-as-Judge Scores         (subjective quality, 1-5)
```

---

##  Skills by Module Level

### Beginner (Modules 01-03)
-  Text preprocessing and feature engineering
-  Classical ML for text classification
-  Basic neural networks

### Intermediate (Modules 04-08)
-  Word embeddings and semantic representations
-  Recurrent neural networks (LSTM)
-  Topic modeling and visualization
-  Interactive dashboards

### Advanced (Modules 09-11)
-  Transfer learning concepts
-  Attention mechanisms
-  Transformer architecture
-  Hugging Face ecosystem

### Expert (Modules 12-14)
-  Fine-tuning BERT for classification and Q&A
-  Text generation with GPT
-  Building RAG systems
-  Working with modern LLM APIs
-  Cost-performance optimization
-  Production deployment considerations

---

##  Project Integration

Students apply these skills in their final projects:

### Text Classification Projects
```
Use:
├── Module 02: Feature engineering (BoW, TF-IDF)
├── Module 05: LSTM baseline
├── Module 12: BERT fine-tuning
└── Module 14: Few-shot with LLM APIs (optional)

Metrics:
└── Precision, Recall, F1, Confusion Matrix
```

### Entity Extraction Projects
```
Use:
├── Module 01: NER basics
├── Module 05: BiLSTM-CRF
└── Module 12: BERT for NER

Metrics:
└── Token-level F1, Entity-level F1, Per-class metrics
```

### Q&A / RAG Projects
```
Use:
├── Module 12: BERT extractive Q&A
├── Module 14.1: Complete RAG pipeline
└── Module 14.2: LLM APIs for generation

Metrics:
└── EM, F1, Precision@K, Faithfulness, Latency, Cost
```

### Dashboard Component (All Projects)
```
Use:
├── Module 07: Visualization
└── Module 08: Interactive Dash apps

Deliverable:
└── Web-based dashboard combining all components
```

---

##  Course Progression

```
Complexity
    ↑
    │                                              ╭──── 14: Production
    │                                         ╭────┤
    │                                    ╭────┤    ╰──── 13: Generation
    │                               ╭────┤    ╰──── 12: Fine-tuning
    │                          ╭────┤    ╰──── 11: Transformers
    │                     ╭────┤    ╰──── 10: Attention
    │                ╭────┤    ╰──── 09: Transfer Learning
    │           ╭────┤    ╰──── 08: Dashboards
    │      ╭────┤    ╰──── 07: Visualization
    │ ╭────┤    ╰──── 06: Topic Modeling
    │ │    ╰──── 05: LSTM
    │ ╰──── 04: Embeddings
    ╰──── 03: Neural Networks
    ╰──── 02: Text Classification
    ╰──── 01: NLP Basics
    │
    └──────────────────────────────────────────────→ Time

    Classical ML → Deep Learning → Transformers → Production
```

---

##  Learning Outcomes

By the end of this course, students can:

### Technical Implementation
1.  Build complete NLP pipelines from scratch
2.  Fine-tune BERT for classification, NER, and Q&A
3.  Generate text with GPT using controlled sampling
4.  Implement RAG systems with vector databases
5.  Integrate modern LLM APIs (GPT-4, Claude)
6.  Create interactive dashboards for NLP systems

### Evaluation & Analysis
7.  Calculate and interpret all major NLP metrics
8.  Perform error analysis and model debugging
9.  Compare models quantitatively (accuracy, cost, latency)
10.  Conduct A/B tests for system improvements

### Decision Making
11.  Choose appropriate models for different tasks
12.  Decide between fine-tuning and API usage
13.  Optimize for production constraints
14.  Make cost-benefit tradeoff decisions

### Communication
15.  Visualize model performance and insights
16.  Build dashboards for non-technical stakeholders
17.  Present findings with quantitative evidence
18.  Document systems for reproducibility

---

##  Key Resources

### Official Documentation
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [OpenAI API](https://platform.openai.com/docs)
- [Anthropic Claude](https://docs.anthropic.com)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net)

### Foundational Papers
- **Attention Is All You Need** (Vaswani et al., 2017) - Transformers
- **BERT** (Devlin et al., 2018) - Bidirectional encoders
- **GPT-2** (Radford et al., 2019) - Language models
- **RAG** (Lewis et al., 2020) - Retrieval-augmented generation
- **Chain-of-Thought** (Wei et al., 2022) - Prompting techniques

### Benchmarks
- **GLUE/SuperGLUE** - General language understanding
- **SQuAD** - Question answering
- **MMLU** - Multitask knowledge
- **HumanEval** - Code generation

---

##  Teaching Philosophy

### For Quantitative Students

This course emphasizes **measurable outcomes** throughout:

1. **Every claim backed by numbers**
   - Not "model is good" → "achieves 94.2% F1"
   - Not "GPT is better" → "GPT-4: 86% MMLU vs GPT-3.5: 70%"

2. **Visual comparisons**
   - Side-by-side performance tables
   - Cost vs accuracy scatter plots
   - Latency distribution charts

3. **Decision frameworks**
   - Clear criteria for model selection
   - Quantified tradeoff analysis
   - ROI calculations

4. **Statistical rigor**
   - Confidence intervals
   - Significance testing
   - Cross-validation

5. **Production reality**
   - Real costs at scale
   - Latency requirements
   - Operational metrics

---

##  Getting Started

### For Students
```bash
# Clone repository
git clone <repository-url>
cd text-mining-dataviz-aa2526

# Pull latest updates before each lesson
git pull origin main

# Open in Google Colab (recommended)
# Navigate to notebook on GitHub
# Replace github.com with colab.research.google.com/github
```

### For Instructors
```
Pre-class:
1. Review BERT_GPT_RAG_SUMMARY.md for modules 12-14
2. Test notebooks in Colab
3. Prepare BERT theory slides (1h)
4. Get API keys for module 14 (or use mock mode)

During class:
- Emphasize metrics at every stage
- Show visualizations of tradeoffs
- Connect to student projects
- Discuss real-world costs

Post-class:
- Share notebook solutions
- Provide additional datasets
- Offer office hours for project help
```

---

##  Course Statistics

```
Total Modules:        14
Total Notebooks:      40+
New Content (12-14):  5 notebooks
Frameworks Covered:   10+ (spaCy, scikit-learn, PyTorch, Transformers, etc.)
Metrics Taught:       30+
Hours of Content:     50+ (self-paced)
Final Project:        Required, comprehensive
```

---

##  Contact

**Andrea Belli**
Email: andrea.belli@unicatt.it
Università Cattolica del Sacro Cuore

**Course Repository**
[text-mining-dataviz-aa2526](https://github.com/yourusername/text-mining-dataviz-aa2526)

---

**Last Updated:** March 1, 2026
**Version:** 2.0 (with Modules 12-14 enhancement)
**License:** MIT - Academic & Educational Use
