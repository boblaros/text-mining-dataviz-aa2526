# Dataset 05: Intent Classification

## Task Description
Classify customer service queries by intent.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Classes**: 5 (refund_request, technical_support, account_inquiry, product_information, complaint)

## Data Format
- `content`: The customer query text
- `category`: Intent label

## Evaluation Metrics
- Accuracy
- Macro F1-Score
- Per-class Precision and Recall
- Confusion Matrix

## Tips
- Intent classification is crucial for routing customer queries
- Some intents may overlap (e.g., complaint + refund_request)
- Keywords and phrases are strong indicators
- Consider the emotional tone and urgency
