# Team 10: Recipe Entity Extraction

## Task Description
Extract recipe components: INGREDIENT, QUANTITY, ACTION, and EQUIPMENT from recipe instructions.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Entity types**: INGREDIENT, QUANTITY, ACTION, EQUIPMENT
- **Format**: IOB2 tagging scheme

## Data Format
Training data (train.jsonl):
```json
{
  "id": "recipe_00000",
  "tokens": ["Mix", "2", "cups", "of", "flour", "in", "a", "bowl", ...],
  "labels": ["B-ACTION", "B-QUANTITY", "I-QUANTITY", "O", "B-INGREDIENT", "O", "O", "B-EQUIPMENT", ...]
}
```

Test data (test.jsonl):
```json
{
  "id": "recipe_00000",
  "tokens": ["Mix", "2", "cups", "of", "flour", ...]
}
```

## Evaluation Metrics
- Entity-level F1-Score per entity type
- Precision and Recall
- Strict and relaxed matching

## Tips
- Quantities often include units (cups, tablespoons, grams)
- Actions are typically cooking verbs
- Multiple ingredients may appear in one instruction
- Equipment and ingredients can be confused - use context
- Consider sequential patterns in recipe instructions
