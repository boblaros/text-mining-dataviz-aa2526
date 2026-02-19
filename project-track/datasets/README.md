# Project Datasets

This folder contains 10 different datasets assigned to each team for the Data Visualization & Text Mining project.

## Dataset Distribution

### Text Classification Tasks (Datasets 1-5)

- **Dataset 01**: Sentiment Analysis Dataset
- **Dataset 02**: News Category Classification Dataset
- **Dataset 03**: Spam Detection Dataset
- **Dataset 04**: Topic Classification Dataset
- **Dataset 05**: Intent Classification Dataset

### Entity Extraction Tasks (Datasets 6-10)

- **Dataset 06**: Named Entity Recognition Dataset
- **Dataset 07**: Product Attribute Extraction Dataset
- **Dataset 08**: Medical Entity Extraction Dataset
- **Dataset 09**: Job Posting Entity Extraction Dataset
- **Dataset 10**: Recipe Entity Extraction Dataset

## Dataset Structure

Each dataset folder contains:
- `train.csv` or `train.json` - Training data
- `test.csv` or `test.json` - Test data (unlabeled or partially labeled)
- `README.md` - Dataset description and task details
- `sample_output.txt` - Example of expected output format

## Data Format

### Text Classification Format
CSV files with columns:
- `text`: The input text
- `label`: The classification label (training data only)

### Entity Extraction Format
JSON files with structure:
```json
{
  "tokens": ["word1", "word2", ...],
  "labels": ["O", "B-ENTITY", "I-ENTITY", ...],
  "id": "unique_id"
}
```

Uses IOB2 (Inside-Outside-Beginning) tagging format.

## Notes

- All datasets have been preprocessed and anonymized
- Test sets may be partially or fully unlabeled depending on dataset assignment
- Ensure you perform proper train/validation split from the training data
- For entity extraction tasks, you must implement token-level classification

## Getting Started

1. Navigate to your assigned dataset folder
2. Read the dataset-specific README.md
3. Explore the data structure
4. Perform exploratory data analysis
5. Build your classification pipeline

## Evaluation

Your models will be evaluated on:
- Accuracy/F1-Score for text classification
- Precision, Recall, F1-Score per entity type for entity extraction
- Overall model comparison and analysis quality
- Dashboard interactivity and visualization quality
