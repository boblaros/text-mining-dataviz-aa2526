# Datasets Summary

## Overview

This directory contains **10 anonymized datasets** for the Data Visualization & Text Mining project. The datasets are designed to prevent students from easily finding ready-made solutions online while providing realistic challenges for both text classification and entity extraction tasks.

## Quick Stats

- **Total Datasets**: 10
- **Text Classification**: 5 datasets (01-05)
- **Entity Extraction**: 5 datasets (06-10)
- **Training Samples per Dataset**: 3,200
- **Test Samples per Dataset**: 800
- **Total Samples**: 40,000

---

## Dataset Distribution

### Text Classification Datasets (01-05)
1. Sentiment Analysis (movie reviews)
2. News Category Classification (headlines)
3. Spam Detection (email/SMS)
4. Topic Classification (research abstracts)
5. Intent Classification (customer queries)

### Entity Extraction Datasets (06-10)
6. Named Entity Recognition (PER, LOC, ORG)
7. Product Attribute Extraction (BRAND, PRODUCT, PRICE, FEATURE)
8. Medical Entity Extraction (DISEASE, SYMPTOM, TREATMENT, MEDICATION)
9. Job Posting Entity Extraction (JOBTITLE, COMPANY, SKILL, LOCATION)
10. Recipe Entity Extraction (INGREDIENT, QUANTITY, ACTION, EQUIPMENT)

---

## Anonymization Strategy

1. **Custom Data Generation**: Synthetically generated with templates
2. **Anonymized Column Names**: Renamed to `content`/`category`
3. **Unique Distribution**: Random shuffling with fixed seed
4. **Withheld Test Labels**: Labels removed from test data

---

## Regenerating Datasets

```bash
cd datasets
python3 prepare_datasets.py
```

Last updated: 2026-02-19
