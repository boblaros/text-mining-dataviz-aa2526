# Team 08: Medical Entity Extraction

## Task Description
Extract medical entities: DISEASE, SYMPTOM, TREATMENT, and MEDICATION from clinical text.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Entity types**: DISEASE, SYMPTOM, TREATMENT, MEDICATION
- **Format**: IOB2 tagging scheme

## Data Format
Training data (train.jsonl):
```json
{
  "id": "medical_00000",
  "tokens": ["Patient", "presents", "with", "fever", ...],
  "labels": ["O", "O", "O", "B-SYMPTOM", ...]
}
```

Test data (test.jsonl):
```json
{
  "id": "medical_00000",
  "tokens": ["Patient", "presents", "with", "fever", ...]
}
```

## Evaluation Metrics
- Entity-level F1-Score per entity type
- Precision and Recall
- Strict and relaxed matching scores

## Tips
- Medical terminology requires domain knowledge
- Multiple entities often co-occur in clinical text
- Distinguish between similar concepts (disease vs symptom)
- Context is crucial for accurate classification
- Consider using medical word embeddings
