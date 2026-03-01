# Data Visualization and Text Mining

**Università Cattolica del Sacro Cuore**
Academic Year 2025-2026

## About

This repository contains notebooks and materials for the Data Visualization and Text Mining course. Notebooks will be published the day before each lesson.

## Course Contents

### 01 - NLP In Practice
Introduction to Natural Language Processing using spaCy and NLTK.
- NLP Basics and pipeline overview
- Tokenization, Stemming, Lemmatization
- Stop Words
- Part of Speech (POS) Tagging and visualization
- Named Entity Recognition (NER) and visualization with displacy
- Exploratory Data Analysis on Text Data

### 02 - Text Classification
Machine Learning applied to text data.
- Scikit-Learn basics
- N-grams
- Bag-of-Words, CountVectorizer, TfidfVectorizer
- Text Classification project (end-to-end)

### 03 - Neural Networks
Introduction to Deep Learning for NLP.
- Simple Classifier with Keras
- PyTorch Simple Classifier

### 04 - Embeddings
Word vectors and text representation.
- Feature Engineering for Text Data
- Word2Vec (CBOW and Skip-gram)
- GloVe embeddings
- Sentence-Transformers (modern embeddings)

### 05 - LSTM
Recurrent Neural Networks for NLP.
- Text Generation with Neural Networks
- LSTM for Sentiment Classification
- LSTM for Named Entity Recognition (BiLSTM on CoNLL-2003)

### 06 - Topic Modeling
Unsupervised methods for discovering topics in text.
- Latent Dirichlet Allocation (LDA)
- Non-Negative Matrix Factorization (NMF)
- Topic Model Evaluation (coherence, perplexity, diversity)
- BERTopic (modern embedding-based approach)

### 07 - Data Visualization
Comprehensive guide to data visualization in Python.
- Matplotlib basics and line plots
- Area plots, histograms, and bar charts
- Pie charts, box plots, scatter plots, and bubble plots
- Waffle charts, word clouds, and regression plots
- Generating maps in Python
- Plotly basics for interactive visualizations

### 08 - Dashboards
Interactive dashboard development with Dash.
- Layout creation with HTML and Dash Bootstrap Components
- Navigation bars and cards
- HTML and core components
- Tables and interactive elements
- Callbacks (basic, multiple inputs/outputs, chained, with State)
- Real-world applications: COVID dashboard, sales app, NLP Q&A app

### 09 - Transfer Learning
Practical demonstrations of transfer learning in NLP.
- **Transfer Learning Demo**: Comparing three approaches on BERT
  - Training from scratch (random initialization)
  - Feature extraction (frozen BERT + classifier)
  - Fine-tuning (end-to-end adaptation)
  - Performance comparison and visualization
- **ULMFit Experiment**: Three-step transfer learning process
  - General-domain language model pre-training (simulated)
  - Target task language model fine-tuning
  - Classifier training with gradual unfreezing
  - Discriminative fine-tuning with layer-wise learning rates

### 10 - Attention Mechanisms
Understanding attention in neural networks.
- Bahdanau Attention (simplified implementation)
- Visualization of attention weights
- Seq2seq models with attention

### 11 - Transformers
Introduction to Transformer architecture and Hugging Face ecosystem.
- Transformer anatomy and self-attention mechanism
- Multi-head attention visualization
- Hugging Face Transformers library introduction
- Working with pre-trained models
- Tokenizers and model pipelines

### 12 - BERT (Encoder Models)
Advanced applications with BERT-based models.
- Text Classification with Transformers
  - Fine-tuning BERT for sentiment analysis
  - Model evaluation and comparison
  - Comprehensive metrics (Accuracy, Precision, Recall, F1, ROC)
- Question Answering with fine-tuned BERT
  - SQuAD dataset and QA task
  - Extractive QA implementation
  - Exact Match (EM) and F1 metrics
  - Confidence scores and answer extraction

### 13 - GPT (Decoder Models)
Text generation with GPT models.
- Autoregressive text generation
- Sampling strategies (temperature, top-k, top-p)
- Generation metrics
  - Perplexity (model confidence)
  - Diversity metrics (Distinct-n, Self-BLEU)
  - BLEU and ROUGE scores
- BERT vs GPT comparison
- Controlled generation techniques

### 14 - RAG & Modern LLMs
Real-world applications combining retrieval and generation.
- **RAG Pipeline**
  - Building knowledge bases with vector databases (FAISS)
  - Semantic search with embeddings
  - Retrieval-Augmented Generation architecture
  - Retrieval metrics (Precision@K, Recall@K, MRR, NDCG)
  - Generation quality metrics (faithfulness, relevance)
  - End-to-end performance analysis
- **Modern LLM APIs**
  - Working with GPT-4, Claude, and other modern LLMs
  - Prompt engineering techniques
  - Few-shot learning
  - Cost-performance optimization
  - LLM evaluation frameworks
  - Production best practices

---

## Modules 12-14: Advanced Transformers (10 Hours)

**NOTE:** Modules 12-14 are NEW content focused on modern transformer models with comprehensive metrics coverage, ideal for quantitative students.

### Time Allocation
- **Module 12 (BERT)**: 2 hours - Encoder models for understanding
- **Module 13 (GPT)**: 2 hours - Decoder models for generation
- **Module 14 (RAG)**: 5 hours - Real-world applications
- **Theory/Slides**: 1 hour - BERT architecture overview
- **Total**: 10 hours

### Complete Metrics Coverage

These modules emphasize quantitative evaluation throughout:

**Classification Tasks (Module 12.1):**
- Accuracy, Precision, Recall, F1 Score
- Macro/Micro/Weighted F1
- Confusion Matrix, ROC Curves
- Per-class performance analysis

**Question Answering (Module 12.2):**
- Exact Match (EM) - binary correctness
- F1 Score - token-level overlap
- Confidence scores

**Text Generation (Module 13):**
- Perplexity - model confidence
- Distinct-1/2/3 - diversity metrics
- Self-BLEU - inter-sample similarity
- BLEU/ROUGE - task-specific quality
- Inference time measurement

**RAG Pipeline (Module 14.1):**
- Retrieval: Precision@K, Recall@K, MRR, NDCG
- Generation: Faithfulness, Answer Relevance, Correctness
- Performance: Latency, Cost per query

**Modern LLMs (Module 14.2):**
- Accuracy, Latency (ms), Cost ($)
- Monthly cost projections at scale
- LLM-as-judge evaluation (1-5 scale)
- Benchmark performance (MMLU, etc.)

### Learning Outcomes

By completing modules 12-14, students will be able to:

**Technical Implementation:**
1. Fine-tune BERT for classification, NER, and extractive Q&A
2. Generate text with GPT using controlled sampling strategies
3. Build complete RAG systems with vector databases
4. Integrate modern LLM APIs (GPT-4, Claude) into applications
5. Create production-ready NLP systems with proper evaluation

**Evaluation & Analysis:**
6. Calculate and interpret all major NLP metrics (EM, F1, Precision, Recall, etc.)
7. Measure generation quality (perplexity, BLEU, ROUGE, diversity)
8. Evaluate retrieval systems (Precision@K, MRR, NDCG)
9. Perform comprehensive cost-benefit analysis
10. Conduct model comparisons with quantitative evidence

**Decision Making:**
11. Choose appropriate models for different tasks (BERT vs GPT vs LLM APIs)
12. Decide between fine-tuning and API usage based on data
13. Optimize systems for production (cost, latency, quality trade-offs)
14. Design evaluation frameworks for both objective and subjective tasks

### For Instructors

**Before Class:**
- Review notebooks in Google Colab
- Prepare API keys for Module 14.2 (or use mock mode)
- Prepare 1-hour BERT theory presentation
- Test metric calculations

**During Class:**
- Emphasize quantitative evaluation at every stage
- Show cost-performance trade-off visualizations
- Connect to student final projects
- Discuss real-world production considerations

**Resources Provided:**
- 5 complete notebooks with code and explanations
- Comprehensive metrics implementations
- Cost analysis frameworks
- Decision-making flowcharts

For detailed instructor guide, see [BERT_GPT_RAG_SUMMARY.md](docs/BERT_GPT_RAG_SUMMARY.md).
For complete course structure, see [COURSE_STRUCTURE.md](docs/COURSE_STRUCTURE.md).

---

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd text-mining-dataviz-aa2526
```

### Stay Updated

Since new content is added before each lesson, make sure to pull the latest changes regularly:

```bash
git pull origin main
```

**Tip:** Run this command before starting a lesson to get the new notebooks.

## Open Notebooks in Google Colab

You can open any notebook directly in Google Colab without cloning the repository:

1. Navigate to the notebook file on GitHub
2. Replace `github.com` in the URL with `colab.research.google.com/github`

**Example:**
```
# Original GitHub URL
https://github.com/nluninja/text-mining-dataviz-aa2526/blob/main/notebook.ipynb

# Colab URL
https://colab.research.google.com/github/nluninja/text-mining-dataviz-aa2526/blob/main/notebook.ipynb
```

Alternatively, from Google Colab:
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File** → **Open notebook**
3. Select the **GitHub** tab
4. Enter the repository URL and select the notebook you want to open

**Note:** Changes made in Colab are saved to your Google Drive, not to the repository. To keep your work, save a copy to your Drive.

## Workflow for Each Lesson

1. **Before the lesson:** Pull the latest updates
   ```bash
   git pull origin main
   ```

2. **During the lesson:** Work through the notebooks

3. **After the lesson:** Your local changes won't conflict with future updates as long as you don't modify the original files. If you want to experiment, consider creating a copy of the notebook.

## Handling Conflicts

If you've made changes to a notebook and encounter conflicts when pulling:

```bash
# Option 1: Stash your changes, pull, then reapply
git stash
git pull origin main
git stash pop

# Option 2: Discard local changes and get the latest version
git checkout -- .
git pull origin main
```

## Project Track

The [project-track/](project-track/) folder contains information and resources for the final course project:

- [README.md](project-track/README.md) - Complete project requirements and guidelines
- [datasets/](project-track/datasets/) - Collection of 10 curated datasets for text classification and entity extraction tasks
  - 5 Text Classification datasets (Sentiment Analysis, News Categorization, Spam Detection, etc.)
  - 5 Entity Extraction datasets (NER, Product Attributes, Medical Entities, etc.)
  - [LLM_USE_CASES.md](project-track/datasets/LLM_USE_CASES.md) - Optional guidance for using LLMs in your project

### Project Requirements Summary

Students must build a text processing pipeline that includes:
1. Data Exploratory Analysis with visualizations
2. Neural Network approach (LSTM, BiLSTM, RNN, etc.)
3. Transformer-based approach (BERT, etc.)
4. Model comparison and metrics
5. Interactive dashboard combining all aspects

See the [project-track README](project-track/README.md) for full details and submission guidelines.

## Tools

The [tools/](tools/) folder contains helpful resources and tutorials:

- [Git-Quick-Tutorial.md](tools/Git-Quick-Tutorial.md) - A quick reference guide for Git commands and workflows
- [Git-Exercises.md](tools/Git-Exercises.md) - Practice exercises to reinforce Git skills

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This repository is intended for academic and educational purposes.

## Contact

For questions about the course materials, please contact the instructor:

**Andrea Belli** - [andrea.belli@unicatt.it](mailto:andrea.belli@unicatt.it)
