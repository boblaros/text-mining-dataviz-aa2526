# Dataset Preparation Summary

## Overview
Successfully created 10 complete datasets for text mining project, covering 5 text classification tasks and 5 entity extraction tasks.

## Dataset Details

### Text Classification Tasks (Teams 1-5)
**Format:** CSV files with `content` and `category` columns

| Team | Task | Classes | Description |
|------|------|---------|-------------|
| Team 01 | Sentiment Analysis | 2 | Movie review sentiment (positive/negative) |
| Team 02 | News Category Classification | 5 | News articles (politics, sports, technology, entertainment, business) |
| Team 03 | Spam Detection | 2 | Email/SMS classification (spam/ham) |
| Team 04 | Topic Classification | 5 | Research abstracts (computer_science, physics, biology, mathematics, chemistry) |
| Team 05 | Intent Classification | 5 | Customer queries (refund_request, technical_support, account_inquiry, product_information, complaint) |

### Entity Extraction Tasks (Teams 6-10)
**Format:** JSONL files with IOB2 tagging scheme

| Team | Task | Entity Types | Description |
|------|------|--------------|-------------|
| Team 06 | Named Entity Recognition | PER, LOC, ORG | Extract person, location, organization entities from news-like text |
| Team 07 | Product Attribute Extraction | BRAND, PRODUCT, PRICE, FEATURE | Extract attributes from product descriptions |
| Team 08 | Medical Entity Extraction | DISEASE, SYMPTOM, TREATMENT, MEDICATION | Extract medical entities from clinical text |
| Team 09 | Job Posting Entity Extraction | JOBTITLE, COMPANY, SKILL, LOCATION | Extract entities from job postings |
| Team 10 | Recipe Entity Extraction | INGREDIENT, QUANTITY, ACTION, EQUIPMENT | Extract components from recipe instructions |

## Dataset Statistics

- **Training samples per team:** 3,200
- **Test samples per team:** 800
- **Total samples generated:** 40,000
- **Data format:**
  - Teams 1-5: CSV (text classification)
  - Teams 6-10: JSONL (entity extraction with IOB2 labels)

## File Structure

```
datasets/
├── prepare_datasets.py          # Main script
├── team_01/
│   ├── train.csv               # Training data with labels
│   ├── test.csv                # Test data (content only, no labels)
│   └── README.md               # Task description and metrics
├── team_02/
│   ├── train.csv
│   ├── test.csv
│   └── README.md
...
├── team_06/
│   ├── train.jsonl             # Training data with IOB2 labels
│   ├── test.jsonl              # Test data (tokens only, no labels)
│   └── README.md
...
└── team_10/
    ├── train.jsonl
    ├── test.jsonl
    └── README.md
```

## Data Characteristics

### Text Classification Data
- **Training data:** Contains `content` (text) and `category` (label) columns
- **Test data:** Contains only `content` column (labels withheld)
- **Anonymization:** Column names changed from `text`/`label` to `content`/`category`

### Entity Extraction Data
- **Training data format:**
  ```json
  {
    "id": "unique_id",
    "tokens": ["word1", "word2", ...],
    "labels": ["O", "B-ENTITY", "I-ENTITY", ...]
  }
  ```
- **Test data format:**
  ```json
  {
    "id": "unique_id",
    "tokens": ["word1", "word2", ...]
  }
  ```
- **IOB2 Tagging:**
  - `B-{TYPE}`: Beginning of entity
  - `I-{TYPE}`: Inside entity (continuation)
  - `O`: Outside any entity

## Data Generation Approach

1. **Synthetic but Realistic:** All data is synthetically generated using template-based methods with varied vocabulary
2. **Balanced:** Classification tasks have balanced class distributions
3. **Diverse:** Multiple templates and vocabulary items ensure variety
4. **Reproducible:** Fixed random seed (42) ensures consistent generation

## Quality Assurance

- ✓ Correct sample counts (3,200 train, 800 test per team)
- ✓ Labels properly withheld from test data
- ✓ IOB2 format correctly implemented for entity extraction
- ✓ README files with task descriptions and evaluation metrics
- ✓ Anonymized column names for classification tasks
- ✓ Unique IDs for all samples
- ✓ Realistic and varied synthetic data

## Evaluation Metrics

Each team's README includes recommended evaluation metrics:
- **Classification tasks:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- **Entity extraction tasks:** Entity-level F1, Precision, Recall, Token-level accuracy

## Usage

To regenerate all datasets:
```bash
python prepare_datasets.py
```

This will create/overwrite all team folders with fresh datasets.
