# Project Track A.Y. 2025-2026
## DATA VISUALIZATION & TEXT MINING

## Project Overview

The team has to build a **text processing pipeline** that performs text classification on the given corpus. All assigned datasets refer to **Entity Extraction** use cases, which can be solved by applying a text classification approach at token level (**Token-based Classification**).

---

## Project Requirements

### 1. Data Exploratory Analysis (DEA)

#### Data Preparation & Cleaning
- Clean the data from the raw dataset provided

#### Exploratory Data Analysis
Using Data Visualization tools to show data variables:
- **Statistical distribution**: frequency, coverage
- **Linguistic information**: POS tags, dependency parsing, lemmas
- **Optional**: LDA or NMF can be used for studying text distribution

---

### 2. Neural Network Approach

- Use **one** Neural Network type to classify the data:
  - Feed Forward
  - RNN
  - LSTM
  - BiLSTM
  - GRU
- **Show metrics** for the implementation strategy

---

### 3. Transformer-based Approach

- Use a **Transformer-based / Language Model** to classify the data (e.g., BERT)
- **Show metrics** for the implementation strategy

---

### 4. Model Comparison

- Provide a **comparison** of the different models implemented
- Compare performance metrics across approaches

---

### 5. Interactive Dashboard

The project **MUST** implement an interactive dashboard that combines:

- **Data Exploratory Analysis** with dynamic charts about the dataset
- **Metrics visualization** for the different strategies applied
- **Interactive input box** to test the categorizer and see how it works, with the ability to switch between models

---

## Project Artifacts

The project **MUST** be developed on **Jupyter** or **Colab**, in a **customer-ready form**, which means:

- **Well-documented** code
- **Descriptions** about all the steps
- **All materials** to reproduce results (data, models, instructions)
- **Dashboard instructions** for running the application
- **GitHub repository** is strongly recommended

---

## Datasets

### Dataset Selection

**You are free to choose your own dataset** for this project. The dataset should be suitable for:
- Text classification tasks, OR
- Entity extraction tasks (token-level classification)

### Prepared Datasets

If you don't have a specific dataset in mind, I have prepared a collection of **10 curated datasets** covering various domains:

- **Text Classification** (5 datasets): Sentiment Analysis, News Categorization, Spam Detection, Topic Classification, Intent Detection
- **Entity Extraction** (5 datasets): Named Entity Recognition, Product Attributes, Medical Entities, Job Postings, Recipe Extraction

**Location**: `datasets/` folder in this repository

**Documentation**: Each dataset includes a detailed README with task description, format, and evaluation metrics

**If you cannot find the datasets folder or need a specific dataset**, please contact me and let me know which type of dataset you need.

---

## Optional: LLM Integration

### Advanced Task (Optional)

You can **optionally** use Large Language Models (LLMs) for any use case in your project. This could include:

- Using LLMs for classification with prompt engineering
- Generating explanations for model predictions
- Few-shot learning experiments
- Comparing LLM performance vs. traditional models
- Hybrid approaches combining LLMs with traditional ML

**Guide Available**: See [`datasets/LLM_USE_CASES.md`](datasets/LLM_USE_CASES.md) for detailed guidance on:
- How to adapt datasets for LLM tasks
- Example prompts and use cases
- Evaluation strategies
- Implementation tips

**Note**: LLM integration is an **optional extension** for advanced students. The core project requirements remain focused on Neural Networks and Transformer-based models (BERT, etc.).

---

## Schedule

**Delivery deadline**: Previous Tuesday before the exam at **8pm CET**

(All exams are on Thursdays)