# Team 07: Product Attribute Extraction

## Task Description
Extract product attributes: BRAND, PRODUCT, PRICE, and FEATURE from product descriptions.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Entity types**: BRAND, PRODUCT, PRICE, FEATURE
- **Format**: IOB2 tagging scheme

## Data Format
Training data (train.jsonl):
```json
{
  "id": "product_00000",
  "tokens": ["The", "Apple", "smartphone", "costs", "$", "299", ...],
  "labels": ["O", "B-BRAND", "B-PRODUCT", "O", "B-PRICE", "I-PRICE", ...]
}
```

Test data (test.jsonl):
```json
{
  "id": "product_00000",
  "tokens": ["The", "Apple", "smartphone", ...]
}
```

## Evaluation Metrics
- Entity-level F1-Score per attribute type
- Precision and Recall
- Partial match score (for handling tokenization issues)

## Tips
- Price formats can vary ($299, $1,299)
- Features may be multi-token (e.g., "noise cancelling")
- Brands and products need context to distinguish
- Consider character-level features for price detection
