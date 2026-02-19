# Dataset 03: Spam Detection

## Task Description
Classify messages as spam or legitimate (ham).

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Classes**: 2 (spam, ham)

## Data Format
- `content`: The message text
- `category`: Classification label (spam/ham)

## Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score (especially for spam class)
- Confusion Matrix
- ROC-AUC

## Tips
- Spam detection is critical for false positive minimization
- Look for patterns: urgency words, monetary amounts, suspicious links
- Consider character-level features (uppercase, special characters)
- Balance between catching spam and not blocking legitimate messages
