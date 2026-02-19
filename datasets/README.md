# Project Datasets

This folder contains 10 different datasets assigned to each team for the Data Visualization & Text Mining project.

## Dataset Distribution

### Text Classification Tasks (Teams 1-5)

- **Team 1**: Sentiment Analysis Dataset
- **Team 2**: News Category Classification Dataset
- **Team 3**: Spam Detection Dataset
- **Team 4**: Topic Classification Dataset
- **Team 5**: Intent Classification Dataset

### Entity Extraction Tasks (Teams 6-10)

- **Team 6**: Named Entity Recognition Dataset
- **Team 7**: Product Attribute Extraction Dataset
- **Team 8**: Medical Entity Extraction Dataset
- **Team 9**: Job Posting Entity Extraction Dataset
- **Team 10**: Recipe Entity Extraction Dataset

## Dataset Structure

Each team folder contains:
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
- Test sets may be partially or fully unlabeled depending on team assignment
- Ensure you perform proper train/validation split from the training data
- For entity extraction tasks, you must implement token-level classification

## Getting Started

1. Navigate to your team folder
2. Read the team-specific README.md
3. Explore the data structure
4. Perform exploratory data analysis
5. Build your classification pipeline

## Evaluation

Your models will be evaluated on:
- Accuracy/F1-Score for text classification
- Precision, Recall, F1-Score per entity type for entity extraction
- Overall model comparison and analysis quality
- Dashboard interactivity and visualization quality
