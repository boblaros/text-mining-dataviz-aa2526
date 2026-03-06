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
- **RAG Pipeline** (NLP14_1_RAG_Pipeline.ipynb)
  - Building knowledge bases with vector databases (FAISS)
  - Semantic search with embeddings
  - Retrieval-Augmented Generation architecture
  - Retrieval metrics (Precision@K, Recall@K, MRR, NDCG)
  - Generation quality metrics (faithfulness, relevance)
  - End-to-end performance analysis
- **Modern LLM APIs** (NLP14_2_Modern_LLMs.ipynb)
  - Working with GPT-4, Claude, and other modern LLMs
  - Prompt engineering techniques
  - Few-shot learning
  - Cost-performance optimization
  - LLM evaluation frameworks
  - Production best practices
- **🆓 FREE Alternative: Gemini-based Notebooks**
  - **NLP14_2_Modern_LLMs_Gemini.ipynb** - Modern LLMs with FREE Gemini API
  - **NLP14_2_1_RAG_with_Gemini.ipynb** - Complete RAG pipeline with Gemini
  - Perfect for students (no credit card required!)
  - 60 requests/minute, 1,500 requests/day
  - See [GEMINI_NOTEBOOKS_INFO.md](GEMINI_NOTEBOOKS_INFO.md) for setup guide

### 15 - AI Agents
Autonomous systems that use LLMs with tools to complete complex tasks.
- **ReAct Agents** - Reasoning + Acting in iterative loops
- **Agent Components**
  - LLM brain for decision-making
  - Tool integration (APIs, calculators, databases)
  - Memory systems (short-term and long-term)
  - Multi-step planning and execution
- **Practical Implementation**
  - Building agents with OpenAI function calling
  - Building agents with Gemini function calling (FREE)
  - Calculator, Wikipedia search, weather, and datetime tools
  - Agent with conversation memory
  - Error handling and best practices
- **🆓 FREE Alternative: NLP15_1_AI_Agent_Gemini.ipynb**
  - Complete AI agent implementation with FREE Gemini API
  - Native function calling support
  - Multiple working tools and examples

**Note:** For detailed information about each module, see the README file in each module folder ([12-BERT/](12-BERT/), [13-GPT/](13-GPT/), [14-RAG/](14-RAG/), [15-AI_Agent/](15-AI_Agent/)).

---

## 🆓 FREE API Access for Students

Many modern LLM notebooks require paid API keys (OpenAI, Anthropic), which can be a barrier for students. We've created **free alternatives using Google Gemini** that require no credit card!

### Gemini-Based Notebooks

Three complete notebooks using **100% FREE** Google Gemini API:

1. **Modern LLMs with Gemini** ([14-RAG/NLP14_2_Modern_LLMs_Gemini.ipynb](14-RAG/NLP14_2_Modern_LLMs_Gemini.ipynb))
   - Prompt engineering, few-shot learning, evaluation
   - No credit card required

2. **RAG with Gemini** ([14-RAG/NLP14_2_1_RAG_with_Gemini.ipynb](14-RAG/NLP14_2_1_RAG_with_Gemini.ipynb))
   - Complete Retrieval-Augmented Generation pipeline
   - Free embeddings + Free LLM

3. **AI Agents with Gemini** ([15-AI_Agent/NLP15_1_AI_Agent_Gemini.ipynb](15-AI_Agent/NLP15_1_AI_Agent_Gemini.ipynb))
   - Autonomous agents with tool use
   - Function calling, memory, multi-step reasoning

### Getting Your Free Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key" → "Create API key"
4. Copy your key and use it in the notebooks

**Free Tier Limits:**
- 60 requests per minute
- 1,500 requests per day
- 1 million tokens per month
- More than enough for all coursework!

📖 See [GEMINI_NOTEBOOKS_INFO.md](GEMINI_NOTEBOOKS_INFO.md) for complete setup guide and troubleshooting.

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
