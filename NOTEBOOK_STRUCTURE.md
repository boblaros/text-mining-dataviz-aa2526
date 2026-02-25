# Notebook Structure - Text Mining Course

**Last updated**: 2026-02-25

---

## 📚 Complete Course Structure

### 01 - NLP in Practice
- `NLP01-01_NLPBasics.ipynb`
- `NLP01-02_Tokenization.ipynb`
- `NLP01-03_Stemming.ipynb`
- `NLP01-04_Lemmatization.ipynb`
- `NLP01-05_Stop-Words.ipynb`
- `NLP01-06_POS-Basics.ipynb`
- `NLP01-07_Visualizing-POS.ipynb`
- `NLP01-08_NamedEntities.ipynb`
- `NLP01-09_Visualizing-NER.ipynb`
- `NLP01-10_EDA-Text-Analysis.ipynb`

### 02 - Text Classification
- `NLP02-01_SciKit-Learn-Basics.ipynb`
- `NLP02-02_N-grams.ipynb`
- `NLP02-03_Bag-of-Words.ipynb`
- `NLP02-04_Text-Classification-Project.ipynb`

### 03 - Neural Networks
- `NLP03-01_Simple_Classifier_with_Keras.ipynb`
- `NLP03-02_PyTorch_SimpleClassifier.ipynb`

### 04 - Embeddings
- `NLP04-01_Feature_Engineering_Text_Data.ipynb`
- `NLP04-02_Word-Vectors.ipynb`
- `NLP04-03_Word-Vectors-GloVe.ipynb`
- `NLP04-05_Sentence-Transformers-Embeddings.ipynb`

### 05 - LSTM
- `NLP05-01_Text-Generation-with-Neural-Networks.ipynb`
- `NLP05-02_LSTM-for-Classification.ipynb`
- `NLP05-03_Entity_Extraction/NLP05-03_LSTM_4_NER-v2.ipynb`

### 06 - Topic Modeling
- `NLP06-00_Latent-Dirichlet-Allocation.ipynb`
- `NLP06-01_Non-Negative-Matrix-Factorization.ipynb`
- `NLP06-02_Topic-Model-Evaluation.ipynb`
- `NLP06-03_BERTopic-Introduction.ipynb`

### 07 - Data Visualization
- `DATAVIZ0100_Matplotlib-and-Line-Plots.ipynb`
- `DATAVIZ0101_Area-Plots-Histograms-and-Bar-Charts.ipynb`
- `DATAVIZ0201_Pie-Charts-Box-Plots-Scatter-Plots-and-Bubble-Plots.ipynb`
- `DATAVIZ0202_Waffle-Charts-Word-Clouds-and-Regression-Plots.ipynb`
- `DATAVIZ0301_Generating-Maps-in-Python.ipynb`
- `DATAVIZ0302_Plotly_Basics.ipynb`

### 08 - Dashboards
*(No notebooks yet)*

---

## 🚀 **NEW STRUCTURE** (Updated 2026-02-25)

### 09 - Transfer Learning ✨ NEW
**Topics**: Transfer Learning fundamentals, evolution from Word2Vec to Transformers

**Notebooks**:
- `NLP09_Transfer_Learning_Demo.ipynb` - Practical comparison: From Scratch vs Feature Extraction vs Fine-tuning

**Slides**:
- `slides/12 - Transfer Learning.pptx` (English)
- `slides/09_Transfer_Learning_LECTURE_NOTES_EN.md` (Complete teaching guide)

**Learning Objectives**:
- Understand what Transfer Learning is and why it matters
- Know the evolution: Word2Vec → ELMo → ULMFiT → BERT/GPT
- Distinguish between Feature Extraction and Fine-tuning
- See practical performance differences

---

### 10 - Encoder/Decoder/Attention ✨ NEW
**Topics**: Sequence-to-sequence models, attention mechanism

**Notebooks**:
*(To be added)*

**Slides**:
- `slides/13 - DecoderEncoderAttention.pptx`
- `slides/13_Encoder_Decoder_Attention_NOTES_EN.md`

**Learning Objectives**:
- Understand encoder-decoder architecture
- Learn attention mechanism (Bahdanau)
- See limitations of RNN-based seq2seq
- Prepare for Transformers architecture

---

### 11 - Transformers (Previously 09)
**Topics**: Transformer architecture, self-attention, positional encoding

**Notebooks**:
- `NLP11_1_transformer-anatomy.ipynb` - Transformer architecture deep dive
- `NLP11_2_Huggingface_intro.ipynb` - Introduction to HuggingFace library

**Slides**:
- `slides/14 - Transformers.ppt`

**Learning Objectives**:
- Understand "Attention Is All You Need"
- Learn self-attention mechanism in detail
- Multi-head attention, positional encoding
- Encoder-only, Decoder-only, Encoder-Decoder variants

---

### 12 - BERT (Previously 11)
**Topics**: BERT pre-training and fine-tuning, practical applications

**Notebooks**:
- `NLP12_1_Classification_with_Transformers.ipynb` - Text classification with BERT
- `NLP12_2_QA_with_finetuned_BERT.ipynb` - Question Answering with fine-tuned BERT

**Learning Objectives**:
- Understand BERT architecture (encoder-only)
- Masked Language Model pre-training
- Fine-tuning for downstream tasks
- Practical applications with HuggingFace

---

## 🎯 Logical Flow

The new structure follows a clear learning path:

```
Word Embeddings (04)
    ↓
LSTM (05)
    ↓
Transfer Learning (09) ← WHY it's important
    ↓
Encoder/Decoder/Attention (10) ← WHAT architectures enable it
    ↓
Transformers (11) ← HOW modern architecture works
    ↓
BERT (12) ← PRACTICAL application
```

---

## 📝 Notebook Naming Convention

**Format**: `NLP[XX]_[Description].ipynb` or `NLP[XX]_[Y]_[Description].ipynb`

Where:
- `XX` = Module number (matches folder number)
- `Y` = Sub-notebook number within module (optional)
- `Description` = Snake_case or hyphen-separated description

**Examples**:
- ✅ `NLP09_Transfer_Learning_Demo.ipynb`
- ✅ `NLP11_1_transformer-anatomy.ipynb`
- ✅ `NLP12_2_QA_with_finetuned_BERT.ipynb`

---

## 🔄 Changes Log

### 2026-02-25
- ✅ Created new module **09 - Transfer Learning**
  - New notebook: `NLP09_Transfer_Learning_Demo.ipynb`
  - New slides: English version with 11 slides
  - Complete lecture notes in English (60+ pages)

- ✅ Created placeholder for **10 - Encoder_Decoder_Attention**

- ✅ Renumbered existing modules:
  - `09-Transformers` → `11-Transformers`
  - `11-BERT` → `12-BERT`

- ✅ Renumbered all notebooks to match new folder structure:
  - `NLP10_1_transformer-anatomy.ipynb` → `NLP11_1_transformer-anatomy.ipynb`
  - `NLP10_2_Huggingface_intro.ipynb` → `NLP11_2_Huggingface_intro.ipynb`
  - `NLP10_3_Classification with Transformers.ipynb` → `NLP12_1_Classification_with_Transformers.ipynb`
  - `NLP11_Q&A with finetuned BERT.ipynb` → `NLP12_2_QA_with_finetuned_BERT.ipynb`

---

## 📚 Additional Materials

### Slides
All slides located in `slides/` folder:
- Module 09: `12 - Transfer Learning.pptx`
- Module 10: `13 - DecoderEncoderAttention.pptx`
- Module 11: `14 - Transformers.ppt`

### Lecture Notes
- `slides/09_Transfer_Learning_LECTURE_NOTES_EN.md` - Complete teaching guide for Transfer Learning
- `slides/13_Encoder_Decoder_Attention_NOTES_EN.md` - Teaching guide for Encoder/Decoder

---

## ✅ Quality Checklist

All new materials (Module 09) include:
- [x] Slides in English
- [x] Complete lecture notes with scripts
- [x] Practical notebook with runnable code
- [x] Clear learning objectives
- [x] Logical flow connecting to next modules
- [x] Q&A sections in lecture notes
- [x] References and further reading

---

**Maintained by**: Andrea Belli
**Course**: Text Mining
**Academic Year**: 2025-2026
