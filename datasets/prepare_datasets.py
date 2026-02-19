"""
Dataset Preparation Script for Text Mining Project
This script downloads and prepares 10 datasets for student teams.
"""

import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

def create_team_folders():
    """Create folder structure for 10 teams"""
    for i in range(1, 11):
        team_folder = Path(f"team_{i:02d}")
        team_folder.mkdir(exist_ok=True)
        print(f"Created {team_folder}")

def anonymize_column_names(df, text_col='text', label_col='label'):
    """
    Anonymize column names to prevent easy lookup
    """
    col_mapping = {
        text_col: 'content',
        label_col: 'category'
    }
    return df.rename(columns=col_mapping)

def shuffle_and_sample(df, sample_size=None, shuffle=True):
    """
    Shuffle and optionally sample dataset
    """
    if shuffle:
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    if sample_size and len(df) > sample_size:
        df = df.sample(n=sample_size, random_state=42).reset_index(drop=True)

    return df

def add_noise_to_labels(labels, noise_level=0.02):
    """
    Add slight noise to make dataset unique
    """
    labels = labels.copy()
    n_samples = len(labels)
    n_noise = int(n_samples * noise_level)

    if n_noise > 0:
        noise_indices = random.sample(range(n_samples), n_noise)
        unique_labels = labels.unique()

        for idx in noise_indices:
            current_label = labels.iloc[idx]
            other_labels = [l for l in unique_labels if l != current_label]
            if other_labels:
                labels.iloc[idx] = random.choice(other_labels)

    return labels

def create_iob_format(tokens, entities):
    """
    Create IOB2 format labels for entity extraction
    entities: list of tuples (start_idx, end_idx, entity_type)
    """
    labels = ['O'] * len(tokens)

    for start, end, entity_type in sorted(entities):
        if start < len(tokens):
            labels[start] = f'B-{entity_type}'
            for i in range(start + 1, min(end, len(tokens))):
                labels[i] = f'I-{entity_type}'

    return labels

# ============================================================================
# TEAM 1: SENTIMENT ANALYSIS
# ============================================================================

def prepare_team_01():
    """
    Sentiment Analysis - Movie Reviews
    Using a subset of IMDB reviews (will be anonymized)
    """
    print("Preparing Team 01: Sentiment Analysis...")

    # Create synthetic movie review dataset
    positive_templates = [
        "This movie was absolutely {adj}! The {element} was {quality}.",
        "I {adverb} enjoyed this film. The {element} exceeded my expectations.",
        "What a {adj} {element}! This is definitely worth watching.",
        "{adj} performances and {quality} {element}. Highly recommended!",
        "The {element} in this movie is {quality}. I was {emotion} throughout."
    ]

    negative_templates = [
        "This movie was {adj}. The {element} was {quality}.",
        "I {adverb} disliked this film. The {element} was disappointing.",
        "What a {adj} waste of time. The {element} was terrible.",
        "{adj} acting and {quality} {element}. Not recommended.",
        "The {element} in this movie is {quality}. I was {emotion} throughout."
    ]

    pos_adj = ["fantastic", "amazing", "brilliant", "outstanding", "excellent", "wonderful", "superb", "magnificent"]
    neg_adj = ["terrible", "awful", "horrible", "disappointing", "poor", "mediocre", "dreadful", "atrocious"]

    elements = ["plot", "acting", "cinematography", "direction", "soundtrack", "screenplay", "dialogue", "pacing"]
    pos_quality = ["exceptional", "remarkable", "impressive", "captivating", "engaging", "stunning", "masterful"]
    neg_quality = ["weak", "unconvincing", "boring", "confusing", "predictable", "lackluster", "uninspired"]

    pos_adverbs = ["really", "absolutely", "completely", "thoroughly", "genuinely"]
    neg_adverbs = ["really", "absolutely", "completely", "thoroughly", "unfortunately"]

    pos_emotions = ["captivated", "moved", "entertained", "amazed", "thrilled"]
    neg_emotions = ["bored", "disappointed", "frustrated", "confused", "annoyed"]

    reviews = []
    labels = []

    # Generate positive reviews
    for _ in range(2000):
        template = random.choice(positive_templates)
        review = template.format(
            adj=random.choice(pos_adj),
            element=random.choice(elements),
            quality=random.choice(pos_quality),
            adverb=random.choice(pos_adverbs),
            emotion=random.choice(pos_emotions)
        )
        reviews.append(review)
        labels.append("positive")

    # Generate negative reviews
    for _ in range(2000):
        template = random.choice(negative_templates)
        review = template.format(
            adj=random.choice(neg_adj),
            element=random.choice(elements),
            quality=random.choice(neg_quality),
            adverb=random.choice(neg_adverbs),
            emotion=random.choice(neg_emotions)
        )
        reviews.append(review)
        labels.append("negative")

    df = pd.DataFrame({'text': reviews, 'label': labels})
    df = shuffle_and_sample(df)

    # Split train/test
    train_df = df.iloc[:3200]
    test_df = df.iloc[3200:]

    # Anonymize
    train_df = anonymize_column_names(train_df)
    test_df = anonymize_column_names(test_df, label_col='label')

    # Save
    team_folder = Path("team_01")
    train_df.to_csv(team_folder / "train.csv", index=False)
    test_df[['content']].to_csv(team_folder / "test.csv", index=False)

    # Create README
    readme = """# Team 01: Sentiment Classification

## Task Description
Classify movie reviews into positive or negative sentiment.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Classes**: 2 (positive, negative)

## Data Format
- `content`: The review text
- `category`: Sentiment label (positive/negative)

## Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score per class
- Confusion Matrix

## Tips
- Consider using TF-IDF or word embeddings
- Watch for class imbalance
- Try different preprocessing techniques (stemming, lemmatization)
- Experiment with different model architectures
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 01 dataset created: {len(train_df)} train, {len(test_df)} test")

# ============================================================================
# TEAM 2: NEWS CATEGORY CLASSIFICATION
# ============================================================================

def prepare_team_02():
    """
    News Category Classification
    """
    print("Preparing Team 02: News Category Classification...")

    categories = ["politics", "sports", "technology", "entertainment", "business"]

    templates = {
        "politics": [
            "The {noun} announced new {topic} policy today.",
            "Government officials discussed {topic} in parliament.",
            "Political debate over {topic} continues to divide opinions.",
            "New legislation regarding {topic} was proposed yesterday."
        ],
        "sports": [
            "The team won the {event} championship after a thrilling match.",
            "Athletes prepare for the upcoming {event} season.",
            "Record broken in {event} competition last weekend.",
            "Coach discusses strategy for the {event} tournament."
        ],
        "technology": [
            "New {product} released with innovative {feature} technology.",
            "Tech company unveils breakthrough in {topic} development.",
            "Researchers achieve milestone in {topic} advancement.",
            "Software update brings improvements to {feature} functionality."
        ],
        "entertainment": [
            "New {media} release breaks box office records.",
            "Celebrity announces upcoming {media} project.",
            "Critics praise innovative {aspect} in latest {media}.",
            "Award ceremony celebrates excellence in {aspect}."
        ],
        "business": [
            "Company reports {trend} in quarterly earnings.",
            "Market shows {trend} following economic indicators.",
            "New startup disrupts {industry} industry.",
            "CEO announces strategic changes in {industry} operations."
        ]
    }

    nouns_politics = ["president", "minister", "senator", "governor", "official"]
    topics_politics = ["healthcare", "education", "taxation", "immigration", "defense"]

    events_sports = ["football", "basketball", "tennis", "swimming", "athletics"]

    products_tech = ["smartphone", "laptop", "tablet", "smartwatch", "software"]
    features_tech = ["AI", "security", "interface", "processing", "connectivity"]
    topics_tech = ["artificial intelligence", "quantum computing", "cybersecurity", "machine learning"]

    media_entertainment = ["film", "series", "album", "concert", "show"]
    aspects_entertainment = ["cinematography", "music", "performance", "storytelling"]

    trends_business = ["growth", "decline", "stability", "improvement", "change"]
    industries_business = ["retail", "manufacturing", "finance", "logistics", "energy"]

    articles = []
    labels = []

    for category in categories:
        for _ in range(800):
            template = random.choice(templates[category])

            if category == "politics":
                article = template.format(
                    noun=random.choice(nouns_politics),
                    topic=random.choice(topics_politics)
                )
            elif category == "sports":
                article = template.format(event=random.choice(events_sports))
            elif category == "technology":
                article = template.format(
                    product=random.choice(products_tech),
                    feature=random.choice(features_tech),
                    topic=random.choice(topics_tech)
                )
            elif category == "entertainment":
                article = template.format(
                    media=random.choice(media_entertainment),
                    aspect=random.choice(aspects_entertainment)
                )
            else:  # business
                article = template.format(
                    trend=random.choice(trends_business),
                    industry=random.choice(industries_business)
                )

            articles.append(article)
            labels.append(category)

    df = pd.DataFrame({'text': articles, 'label': labels})
    df = shuffle_and_sample(df)

    # Split
    train_df = df.iloc[:3200]
    test_df = df.iloc[3200:]

    # Anonymize
    train_df = anonymize_column_names(train_df)
    test_df = anonymize_column_names(test_df)

    # Save
    team_folder = Path("team_02")
    train_df.to_csv(team_folder / "train.csv", index=False)
    test_df[['content']].to_csv(team_folder / "test.csv", index=False)

    readme = """# Team 02: News Category Classification

## Task Description
Classify news articles into one of five categories.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Classes**: 5 (politics, sports, technology, entertainment, business)

## Data Format
- `content`: The article headline or snippet
- `category`: News category

## Evaluation Metrics
- Accuracy
- Macro and Micro F1-Score
- Per-class Precision and Recall
- Confusion Matrix

## Tips
- Multi-class classification problem
- Consider class balance
- Topic-specific vocabulary is important
- Try different vectorization techniques
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 02 dataset created: {len(train_df)} train, {len(test_df)} test")

def main():
    """Main execution"""
    print("=" * 60)
    print("Creating Dataset Preparation Environment")
    print("=" * 60)

    create_team_folders()

    print("\n" + "=" * 60)
    print("Preparing Individual Team Datasets")
    print("=" * 60 + "\n")

    prepare_team_01()
    prepare_team_02()

    # Note: Teams 3-10 will be implemented in similar fashion
    print("\n" + "=" * 60)
    print("⚠ Teams 3-10 require additional implementation")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Implement prepare_team_03() through prepare_team_10()")
    print("2. Add real dataset downloads or create more synthetic data")
    print("3. Test each dataset for quality and anonymization")

if __name__ == "__main__":
    main()
