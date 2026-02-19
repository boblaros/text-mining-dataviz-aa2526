# Team 09: Job Posting Entity Extraction

## Task Description
Extract entities from job postings: JOBTITLE, COMPANY, SKILL, and LOCATION.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Entity types**: JOBTITLE, COMPANY, SKILL, LOCATION
- **Format**: IOB2 tagging scheme

## Data Format
Training data (train.jsonl):
```json
{
  "id": "job_00000",
  "tokens": ["TechCorp", "is", "hiring", "a", "Software", "Engineer", ...],
  "labels": ["B-COMPANY", "O", "O", "O", "B-JOBTITLE", "I-JOBTITLE", ...]
}
```

Test data (test.jsonl):
```json
{
  "id": "job_00000",
  "tokens": ["TechCorp", "is", "hiring", ...]
}
```

## Evaluation Metrics
- Entity-level F1-Score per entity type
- Precision and Recall
- Exact and partial match scores

## Tips
- Job titles are often multi-token (e.g., "Software Engineer")
- Skills can be technical or soft skills
- Company names may have variations (Inc, Corp, Ltd)
- Location context helps disambiguate company names
- Consider using job-domain specific features
