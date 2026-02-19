# Dataset 06: Named Entity Recognition

## Task Description
Extract person (PER), location (LOC), and organization (ORG) entities from text.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Entity types**: PER, LOC, ORG
- **Format**: IOB2 tagging scheme

## Data Format
Training data (train.jsonl):
```json
{
  "id": "sample_00000",
  "tokens": ["word1", "word2", ...],
  "labels": ["O", "B-PER", "I-PER", "O", "B-LOC", ...]
}
```

Test data (test.jsonl):
```json
{
  "id": "sample_00000",
  "tokens": ["word1", "word2", ...]
}
```

## IOB2 Format
- B-{TYPE}: Beginning of entity
- I-{TYPE}: Inside entity (continuation)
- O: Outside any entity

## Evaluation Metrics
- Entity-level F1-Score (exact match)
- Precision and Recall per entity type
- Token-level accuracy

## Tips
- Handle multi-token entities correctly
- Context is important for disambiguation
- Consider using BIO encoding in your model
- Evaluate at both token and entity level
