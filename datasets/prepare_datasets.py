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

# ============================================================================
# TEAM 3: SPAM DETECTION
# ============================================================================

def prepare_team_03():
    """
    Spam Detection - Email/SMS classification
    """
    print("Preparing Team 03: Spam Detection...")

    spam_templates = [
        "WINNER! You've won ${amount}! Click {link} to claim your prize NOW!",
        "Congratulations! You've been selected for a {offer}. Reply with {info} to confirm.",
        "URGENT: Your {account} has been {action}. Verify at {link} immediately.",
        "FREE {product}! Limited time offer. Text {keyword} to {number} now!",
        "You have {amount} unclaimed. Click here: {link}",
        "Make ${amount} from home! {offer}. Visit {link} for details.",
        "Your loan has been approved for ${amount}! Call {number} now.",
        "ALERT: Suspicious activity on your {account}. Confirm identity at {link}.",
        "Hot singles in your area! Click {link} to meet them today!",
        "Get {product} for only ${amount}! Offer expires soon. Order at {link}."
    ]

    ham_templates = [
        "Hey, are you free for {activity} this {day}?",
        "Meeting scheduled for {time} tomorrow. See you there!",
        "Thanks for {action}. Really appreciate it!",
        "Can you pick up {item} on your way home?",
        "The report is ready. I'll send it by {time}.",
        "Happy {occasion}! Hope you have a great day.",
        "Reminder: {event} is scheduled for {day} at {time}.",
        "Just finished {activity}. How did yours go?",
        "Please review the {document} when you get a chance.",
        "Looking forward to seeing you at {event}!"
    ]

    amounts = ["1000", "5000", "500", "10000", "2500", "750"]
    links = ["bit.ly/xyz123", "tinyurl.com/abc", "secure-verify.com", "claim-now.net"]
    offers = ["free iPhone", "vacation package", "cash reward", "gift card"]
    accounts = ["bank account", "email account", "credit card", "PayPal account"]
    actions = ["suspended", "compromised", "locked", "flagged"]
    products = ["iPhone", "laptop", "gift card", "vacation"]
    keywords = ["YES", "CONFIRM", "CLAIM", "WIN"]
    numbers = ["12345", "555-0100", "88888"]
    info = ["your SSN", "credit card", "bank details", "account number"]

    activities = ["lunch", "coffee", "a movie", "dinner"]
    days = ["Monday", "Tuesday", "Friday", "the weekend", "next week"]
    times = ["2pm", "10am", "3:30pm", "noon"]
    items = ["milk", "groceries", "the package", "dinner"]
    occasions = ["birthday", "anniversary", "Monday"]
    events = ["the meeting", "the party", "the conference", "dinner"]
    documents = ["proposal", "contract", "presentation", "budget"]

    texts = []
    labels = []

    # Generate spam messages
    for _ in range(2000):
        template = random.choice(spam_templates)
        text = template.format(
            amount=random.choice(amounts),
            link=random.choice(links),
            offer=random.choice(offers),
            account=random.choice(accounts),
            action=random.choice(actions),
            product=random.choice(products),
            keyword=random.choice(keywords),
            number=random.choice(numbers),
            info=random.choice(info)
        )
        texts.append(text)
        labels.append("spam")

    # Generate ham (legitimate) messages
    for _ in range(2000):
        template = random.choice(ham_templates)
        text = template.format(
            activity=random.choice(activities),
            day=random.choice(days),
            time=random.choice(times),
            item=random.choice(items),
            action=random.choice(["helping", "coming", "the suggestion", "your time"]),
            occasion=random.choice(occasions),
            event=random.choice(events),
            document=random.choice(documents)
        )
        texts.append(text)
        labels.append("ham")

    df = pd.DataFrame({'text': texts, 'label': labels})
    df = shuffle_and_sample(df)

    # Split
    train_df = df.iloc[:3200]
    test_df = df.iloc[3200:]

    # Anonymize
    train_df = anonymize_column_names(train_df)
    test_df = anonymize_column_names(test_df)

    # Save
    team_folder = Path("team_03")
    train_df.to_csv(team_folder / "train.csv", index=False)
    test_df[['content']].to_csv(team_folder / "test.csv", index=False)

    readme = """# Team 03: Spam Detection

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 03 dataset created: {len(train_df)} train, {len(test_df)} test")

# ============================================================================
# TEAM 4: TOPIC CLASSIFICATION
# ============================================================================

def prepare_team_04():
    """
    Topic Classification - Research paper abstracts
    """
    print("Preparing Team 04: Topic Classification...")

    categories = ["computer_science", "physics", "biology", "mathematics", "chemistry"]

    templates = {
        "computer_science": [
            "We present a novel {method} for {problem}. Our approach achieves {metric} improvement over baseline methods.",
            "This paper introduces {system}, a {adjective} framework for {application}. Experimental results demonstrate {benefit}.",
            "We propose an efficient {algorithm} for {task}. The method leverages {technique} to optimize {objective}.",
            "Our work addresses {problem} using {method}. We evaluate on {dataset} and show significant performance gains."
        ],
        "physics": [
            "We investigate {phenomenon} in {system}. Experimental observations reveal {finding}.",
            "This study examines {property} of {material} under {conditions}. Results indicate {conclusion}.",
            "We report measurements of {quantity} using {technique}. The observed {pattern} suggests {interpretation}.",
            "Our analysis of {system} demonstrates {effect}. These findings have implications for {application}."
        ],
        "biology": [
            "We characterized {protein} in {organism}. Functional studies show {role} in {process}.",
            "This research investigates {mechanism} of {phenomenon} in {system}. Results reveal {finding}.",
            "We identified {gene} responsible for {trait} in {organism}. Expression analysis indicates {function}.",
            "Our study examines {interaction} between {component1} and {component2} during {process}."
        ],
        "mathematics": [
            "We prove {theorem} for {structure}. The proof utilizes {technique} and extends {previous_work}.",
            "This paper establishes {property} of {object}. We derive {bound} and show {implication}.",
            "We present a {adjective} solution to {problem}. Our method employs {approach} from {field}.",
            "We investigate {property} in {space}. The main result characterizes {condition} for {outcome}."
        ],
        "chemistry": [
            "We synthesized {compound} using {method}. Characterization reveals {property} with potential for {application}.",
            "This work reports {reaction} of {reactant} with {catalyst}. Product analysis shows {selectivity}.",
            "We studied {mechanism} of {reaction} using {technique}. Kinetic data indicates {pathway}.",
            "Our investigation of {system} under {conditions} reveals {phenomenon}. Applications include {use}."
        ]
    }

    # Computer Science
    methods_cs = ["deep learning model", "neural architecture", "optimization algorithm", "graph-based method"]
    problems_cs = ["image classification", "natural language processing", "recommendation systems", "anomaly detection"]
    metrics_cs = ["15% accuracy", "20% speed", "significant performance"]
    systems_cs = ["distributed system", "cloud platform", "mobile framework", "web service"]
    adjectives_cs = ["scalable", "efficient", "robust", "adaptive"]
    applications_cs = ["real-time processing", "big data analytics", "edge computing", "IoT systems"]
    algorithms_cs = ["clustering algorithm", "sorting method", "search technique", "optimization approach"]
    tasks_cs = ["data mining", "pattern recognition", "feature extraction", "model training"]
    techniques_cs = ["transfer learning", "ensemble methods", "attention mechanisms", "reinforcement learning"]
    datasets_cs = ["benchmark datasets", "real-world data", "synthetic datasets", "public repositories"]

    # Physics
    phenomena_phys = ["quantum entanglement", "phase transitions", "wave propagation", "particle interactions"]
    systems_phys = ["quantum systems", "condensed matter", "optical systems", "plasma"]
    properties_phys = ["thermal conductivity", "magnetic susceptibility", "optical properties", "electronic structure"]
    materials_phys = ["semiconductors", "superconductors", "metamaterials", "nanostructures"]
    conditions_phys = ["low temperatures", "high pressure", "external fields", "varying frequencies"]
    quantities_phys = ["energy levels", "cross sections", "resonance frequencies", "phase velocities"]

    # Biology
    proteins_bio = ["kinase", "transcription factor", "receptor", "enzyme"]
    organisms_bio = ["E. coli", "yeast", "mice", "plants"]
    processes_bio = ["cell division", "signal transduction", "metabolism", "development"]
    mechanisms_bio = ["regulatory mechanism", "transport mechanism", "signaling pathway", "metabolic pathway"]
    genes_bio = ["novel gene", "regulatory gene", "housekeeping gene", "oncogene"]
    traits_bio = ["stress resistance", "growth rate", "morphology", "disease susceptibility"]
    components_bio = ["proteins", "lipids", "nucleic acids", "metabolites"]

    # Mathematics
    theorems_math = ["convergence theorem", "existence theorem", "uniqueness theorem", "stability result"]
    structures_math = ["algebraic structures", "topological spaces", "metric spaces", "graph structures"]
    properties_math = ["continuity", "differentiability", "boundedness", "convergence"]
    objects_math = ["operators", "functionals", "manifolds", "sequences"]
    approaches_math = ["variational methods", "fixed point theory", "spectral analysis", "perturbation theory"]
    fields_math = ["functional analysis", "differential geometry", "number theory", "combinatorics"]
    spaces_math = ["Hilbert spaces", "Banach spaces", "function spaces", "probability spaces"]

    # Chemistry
    compounds_chem = ["organic catalyst", "metal complex", "polymer", "nanomaterial"]
    methods_chem = ["microwave synthesis", "sol-gel method", "electrochemical route", "hydrothermal synthesis"]
    reactions_chem = ["coupling reaction", "oxidation reaction", "polymerization", "cycloaddition"]
    reactants_chem = ["aromatic compounds", "metal ions", "organic substrates", "monomers"]
    catalysts_chem = ["Pd catalyst", "enzyme catalyst", "acid catalyst", "photocatalyst"]
    mechanisms_chem = ["reaction mechanism", "catalytic mechanism", "degradation mechanism", "formation mechanism"]
    techniques_chem = ["NMR spectroscopy", "mass spectrometry", "X-ray crystallography", "chromatography"]

    texts = []
    labels = []

    for category in categories:
        for _ in range(800):
            template = random.choice(templates[category])

            if category == "computer_science":
                text = template.format(
                    method=random.choice(methods_cs),
                    problem=random.choice(problems_cs),
                    metric=random.choice(metrics_cs),
                    system=random.choice(systems_cs),
                    adjective=random.choice(adjectives_cs),
                    application=random.choice(applications_cs),
                    algorithm=random.choice(algorithms_cs),
                    task=random.choice(tasks_cs),
                    technique=random.choice(techniques_cs),
                    objective="performance",
                    dataset=random.choice(datasets_cs),
                    benefit="superior results"
                )
            elif category == "physics":
                text = template.format(
                    phenomenon=random.choice(phenomena_phys),
                    system=random.choice(systems_phys),
                    finding="novel behavior",
                    property=random.choice(properties_phys),
                    material=random.choice(materials_phys),
                    conditions=random.choice(conditions_phys),
                    conclusion="strong correlation",
                    quantity=random.choice(quantities_phys),
                    technique="spectroscopy",
                    pattern="distinct signature",
                    interpretation="theoretical predictions",
                    effect="significant enhancement",
                    application="future devices"
                )
            elif category == "biology":
                text = template.format(
                    protein=random.choice(proteins_bio),
                    organism=random.choice(organisms_bio),
                    role="critical role",
                    process=random.choice(processes_bio),
                    mechanism=random.choice(mechanisms_bio),
                    phenomenon="gene expression",
                    system="cellular system",
                    finding="conserved pathway",
                    gene=random.choice(genes_bio),
                    trait=random.choice(traits_bio),
                    function="regulatory function",
                    interaction="direct interaction",
                    component1=random.choice(components_bio),
                    component2=random.choice(components_bio)
                )
            elif category == "mathematics":
                text = template.format(
                    theorem=random.choice(theorems_math),
                    structure=random.choice(structures_math),
                    technique=random.choice(approaches_math),
                    previous_work="classical results",
                    property=random.choice(properties_math),
                    object=random.choice(objects_math),
                    bound="optimal bound",
                    implication="important applications",
                    adjective="constructive",
                    problem="classical problem",
                    approach=random.choice(approaches_math),
                    field=random.choice(fields_math),
                    space=random.choice(spaces_math),
                    condition="necessary conditions",
                    outcome="convergence"
                )
            else:  # chemistry
                text = template.format(
                    compound=random.choice(compounds_chem),
                    method=random.choice(methods_chem),
                    property="high selectivity",
                    application="catalysis",
                    reaction=random.choice(reactions_chem),
                    reactant=random.choice(reactants_chem),
                    catalyst=random.choice(catalysts_chem),
                    selectivity="excellent yield",
                    mechanism=random.choice(mechanisms_chem),
                    technique=random.choice(techniques_chem),
                    pathway="two-step pathway",
                    system="reaction system",
                    conditions="mild conditions",
                    phenomenon="enhanced reactivity",
                    use="industrial applications"
                )

            texts.append(text)
            labels.append(category)

    df = pd.DataFrame({'text': texts, 'label': labels})
    df = shuffle_and_sample(df)

    # Split
    train_df = df.iloc[:3200]
    test_df = df.iloc[3200:]

    # Anonymize
    train_df = anonymize_column_names(train_df)
    test_df = anonymize_column_names(test_df)

    # Save
    team_folder = Path("team_04")
    train_df.to_csv(team_folder / "train.csv", index=False)
    test_df[['content']].to_csv(team_folder / "test.csv", index=False)

    readme = """# Team 04: Topic Classification

## Task Description
Classify research paper abstracts into academic disciplines.

## Dataset
- **Training samples**: 3,200
- **Test samples**: 800
- **Classes**: 5 (computer_science, physics, biology, mathematics, chemistry)

## Data Format
- `content`: The abstract text
- `category`: Research topic/discipline

## Evaluation Metrics
- Accuracy
- Macro F1-Score
- Per-class Precision and Recall
- Confusion Matrix

## Tips
- Domain-specific terminology is key
- Multi-class classification with potentially overlapping concepts
- Consider scientific vocabulary and writing patterns
- Technical terms may be indicators of specific fields
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 04 dataset created: {len(train_df)} train, {len(test_df)} test")

# ============================================================================
# TEAM 5: INTENT CLASSIFICATION
# ============================================================================

def prepare_team_05():
    """
    Intent Classification - Customer query intent
    """
    print("Preparing Team 05: Intent Classification...")

    intents = ["refund_request", "technical_support", "account_inquiry", "product_information", "complaint"]

    templates = {
        "refund_request": [
            "I want to return my {product} and get a refund.",
            "Can I get my money back for {product}? It doesn't work properly.",
            "How do I request a refund for order {order_id}?",
            "I'd like to cancel my order and receive a full refund.",
            "The {product} arrived damaged. I need a refund please."
        ],
        "technical_support": [
            "My {product} won't {action}. Can you help?",
            "I'm having trouble {action} with my {product}.",
            "How do I {action} on my {product}?",
            "The {feature} feature isn't working on my {product}.",
            "I keep getting an error when trying to {action}."
        ],
        "account_inquiry": [
            "How do I {action} my account?",
            "I forgot my password. Can you help me reset it?",
            "When does my {subscription} renew?",
            "Can I update my {account_info}?",
            "How do I check my account {detail}?"
        ],
        "product_information": [
            "What are the {feature} of the {product}?",
            "Does the {product} come with {accessory}?",
            "Is the {product} compatible with {other_product}?",
            "What's the difference between {product1} and {product2}?",
            "Can you tell me more about the {feature} feature?"
        ],
        "complaint": [
            "I'm very disappointed with {aspect}.",
            "This is unacceptable. The {aspect} is terrible.",
            "I've been waiting {time} for {item} and still nothing!",
            "Your {aspect} is the worst I've experienced.",
            "I'm filing a complaint about {aspect}."
        ]
    }

    products = ["laptop", "phone", "tablet", "headphones", "smartwatch", "camera", "printer"]
    actions = ["connect", "charge", "turn on", "sync", "update", "install", "download"]
    features = ["battery life", "camera quality", "specifications", "warranty", "price", "dimensions"]
    subscriptions = ["subscription", "membership", "plan", "service"]
    account_info = ["email address", "payment method", "shipping address", "preferences"]
    details = ["balance", "history", "status", "settings"]
    accessories = ["charger", "case", "warranty", "manual", "cables"]
    aspects = ["service", "delivery time", "product quality", "customer support", "packaging"]
    times = ["2 weeks", "a month", "3 days", "over a week", "too long"]
    items = ["order", "response", "refund", "replacement"]

    texts = []
    labels = []

    for intent in intents:
        for _ in range(800):
            template = random.choice(templates[intent])

            if intent == "refund_request":
                text = template.format(
                    product=random.choice(products),
                    order_id=f"#{random.randint(10000, 99999)}"
                )
            elif intent == "technical_support":
                text = template.format(
                    product=random.choice(products),
                    action=random.choice(actions),
                    feature=random.choice(features)
                )
            elif intent == "account_inquiry":
                text = template.format(
                    action=random.choice(["change", "update", "delete", "verify", "access"]),
                    subscription=random.choice(subscriptions),
                    account_info=random.choice(account_info),
                    detail=random.choice(details)
                )
            elif intent == "product_information":
                text = template.format(
                    feature=random.choice(features),
                    product=random.choice(products),
                    accessory=random.choice(accessories),
                    other_product=random.choice(products),
                    product1=random.choice(products),
                    product2=random.choice(products)
                )
            else:  # complaint
                text = template.format(
                    aspect=random.choice(aspects),
                    time=random.choice(times),
                    item=random.choice(items)
                )

            texts.append(text)
            labels.append(intent)

    df = pd.DataFrame({'text': texts, 'label': labels})
    df = shuffle_and_sample(df)

    # Split
    train_df = df.iloc[:3200]
    test_df = df.iloc[3200:]

    # Anonymize
    train_df = anonymize_column_names(train_df)
    test_df = anonymize_column_names(test_df)

    # Save
    team_folder = Path("team_05")
    train_df.to_csv(team_folder / "train.csv", index=False)
    test_df[['content']].to_csv(team_folder / "test.csv", index=False)

    readme = """# Team 05: Intent Classification

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 05 dataset created: {len(train_df)} train, {len(test_df)} test")

# ============================================================================
# TEAM 6: NAMED ENTITY RECOGNITION
# ============================================================================

def prepare_team_06():
    """
    Named Entity Recognition - PER, LOC, ORG entities
    """
    print("Preparing Team 06: Named Entity Recognition...")

    persons = ["John Smith", "Maria Garcia", "David Chen", "Sarah Johnson", "Ahmed Hassan",
               "Emily Williams", "Robert Brown", "Lisa Anderson", "Michael Lee", "Anna Martinez"]
    locations = ["New York", "London", "Tokyo", "Paris", "Berlin", "Sydney", "Mumbai",
                 "Toronto", "Singapore", "Dubai"]
    organizations = ["Microsoft", "United Nations", "Harvard University", "Tesla",
                     "World Health Organization", "Goldman Sachs", "BBC", "NASA", "FIFA", "Amazon"]

    templates = [
        "{person} visited {location} last week for a conference.",
        "{organization} announced a new partnership with {person}.",
        "The meeting in {location} was attended by representatives from {organization}.",
        "{person}, CEO of {organization}, spoke at the event in {location}.",
        "According to {organization}, {person} will relocate to {location}.",
        "Researchers from {organization} in {location} published new findings.",
        "{person} and colleagues from {location} joined {organization} this month.",
        "The {location} office of {organization} welcomed {person} as director.",
        "{organization} is expanding operations to {location}, said {person}.",
        "{person} traveled from {location} to meet with {organization} officials."
    ]

    samples = []

    for _ in range(4000):
        template = random.choice(templates)
        person = random.choice(persons)
        location = random.choice(locations)
        org = random.choice(organizations)

        text = template.format(person=person, location=location, organization=org)
        tokens = text.split()

        entities = []
        # Find entity positions
        for i, token in enumerate(tokens):
            # Check for person (might be multi-token)
            if person.split()[0] == token:
                person_tokens = person.split()
                if i + len(person_tokens) <= len(tokens) and tokens[i:i+len(person_tokens)] == person_tokens:
                    entities.append((i, i + len(person_tokens), 'PER'))

            # Check for location
            if location.split()[0] == token:
                loc_tokens = location.split()
                if i + len(loc_tokens) <= len(tokens) and tokens[i:i+len(loc_tokens)] == loc_tokens:
                    entities.append((i, i + len(loc_tokens), 'LOC'))

            # Check for organization
            if org.split()[0] == token:
                org_tokens = org.split()
                if i + len(org_tokens) <= len(tokens) and tokens[i:i+len(org_tokens)] == org_tokens:
                    entities.append((i, i + len(org_tokens), 'ORG'))

        labels = create_iob_format(tokens, entities)

        samples.append({
            'id': f'sample_{len(samples):05d}',
            'tokens': tokens,
            'labels': labels
        })

    # Split
    train_samples = samples[:3200]
    test_samples = samples[3200:]

    # Save train with labels
    team_folder = Path("team_06")
    with open(team_folder / "train.jsonl", "w") as f:
        for sample in train_samples:
            f.write(json.dumps(sample) + "\n")

    # Save test without labels
    with open(team_folder / "test.jsonl", "w") as f:
        for sample in test_samples:
            test_sample = {'id': sample['id'], 'tokens': sample['tokens']}
            f.write(json.dumps(test_sample) + "\n")

    readme = """# Team 06: Named Entity Recognition

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 06 dataset created: {len(train_samples)} train, {len(test_samples)} test")

# ============================================================================
# TEAM 7: PRODUCT ATTRIBUTE EXTRACTION
# ============================================================================

def prepare_team_07():
    """
    Product Attribute Extraction - BRAND, PRODUCT, PRICE, FEATURE
    """
    print("Preparing Team 07: Product Attribute Extraction...")

    brands = ["Apple", "Samsung", "Sony", "LG", "Dell", "HP", "Lenovo", "Nike", "Adidas", "Canon"]
    products = ["smartphone", "laptop", "camera", "headphones", "smartwatch", "tablet",
                "monitor", "keyboard", "speaker", "television"]
    price_patterns = ["$299", "$799", "$1,299", "$499", "$149", "$999", "$599", "$1,499"]
    features = ["waterproof", "wireless", "4K resolution", "noise cancelling", "touch screen",
                "fast charging", "lightweight", "HD display", "ergonomic", "portable"]

    templates = [
        "The {brand} {product} costs {price} and features {feature} technology.",
        "New {brand} {product} available for {price} with {feature} design.",
        "Looking for a {feature} {product}? The {brand} model is {price}.",
        "{brand} announces {product} with {feature} at {price}.",
        "Great deal: {brand} {product} ({feature}) now only {price}!",
        "The {feature} {brand} {product} is priced at {price}.",
        "Buy the {brand} {product} - {feature}, amazing quality, just {price}.",
        "{brand}'s latest {product} offers {feature} for {price}.",
        "Premium {brand} {product} with {feature} available at {price}.",
        "Get the {feature} {brand} {product} today for {price}."
    ]

    samples = []

    for _ in range(4000):
        template = random.choice(templates)
        brand = random.choice(brands)
        product = random.choice(products)
        price = random.choice(price_patterns)
        feature = random.choice(features)

        text = template.format(brand=brand, product=product, price=price, feature=feature)
        tokens = text.replace(',', ' , ').replace('(', ' ( ').replace(')', ' ) ').split()

        entities = []
        # Find entity positions
        i = 0
        while i < len(tokens):
            # Check for brand
            if brand.split()[0] == tokens[i]:
                brand_tokens = brand.split()
                if i + len(brand_tokens) <= len(tokens) and tokens[i:i+len(brand_tokens)] == brand_tokens:
                    entities.append((i, i + len(brand_tokens), 'BRAND'))
                    i += len(brand_tokens)
                    continue

            # Check for product
            if tokens[i] == product:
                entities.append((i, i + 1, 'PRODUCT'))

            # Check for price (with comma handling)
            if tokens[i].startswith('$'):
                price_end = i + 1
                # Check if next token is comma separated (like "1" "," "299")
                if price_end < len(tokens) and tokens[price_end] == ',':
                    price_end += 2  # Include comma and next number
                entities.append((i, price_end, 'PRICE'))

            # Check for feature
            if feature.split()[0] == tokens[i]:
                feature_tokens = feature.split()
                if i + len(feature_tokens) <= len(tokens) and tokens[i:i+len(feature_tokens)] == feature_tokens:
                    entities.append((i, i + len(feature_tokens), 'FEATURE'))

            i += 1

        labels = create_iob_format(tokens, entities)

        samples.append({
            'id': f'product_{len(samples):05d}',
            'tokens': tokens,
            'labels': labels
        })

    # Split
    train_samples = samples[:3200]
    test_samples = samples[3200:]

    # Save
    team_folder = Path("team_07")
    with open(team_folder / "train.jsonl", "w") as f:
        for sample in train_samples:
            f.write(json.dumps(sample) + "\n")

    with open(team_folder / "test.jsonl", "w") as f:
        for sample in test_samples:
            test_sample = {'id': sample['id'], 'tokens': sample['tokens']}
            f.write(json.dumps(test_sample) + "\n")

    readme = """# Team 07: Product Attribute Extraction

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 07 dataset created: {len(train_samples)} train, {len(test_samples)} test")

# ============================================================================
# TEAM 8: MEDICAL ENTITY EXTRACTION
# ============================================================================

def prepare_team_08():
    """
    Medical Entity Extraction - DISEASE, SYMPTOM, TREATMENT, MEDICATION
    """
    print("Preparing Team 08: Medical Entity Extraction...")

    diseases = ["diabetes", "hypertension", "asthma", "pneumonia", "arthritis",
                "migraine", "bronchitis", "gastritis", "dermatitis", "sinusitis"]
    symptoms = ["fever", "cough", "headache", "fatigue", "nausea", "dizziness",
                "pain", "shortness of breath", "chest pain", "inflammation"]
    treatments = ["physical therapy", "surgery", "counseling", "lifestyle changes",
                  "breathing exercises", "rest", "diet modification", "exercise",
                  "wound care", "compression therapy"]
    medications = ["ibuprofen", "aspirin", "amoxicillin", "metformin", "lisinopril",
                   "albuterol", "prednisone", "omeprazole", "atorvastatin", "levothyroxine"]

    templates = [
        "Patient presents with {symptom} and was diagnosed with {disease}.",
        "Treatment for {disease} includes {medication} and {treatment}.",
        "The {symptom} associated with {disease} improved after {medication} administration.",
        "Prescribed {medication} for {disease} management along with {treatment}.",
        "Common symptoms of {disease} include {symptom} which requires {treatment}.",
        "{disease} patient reports {symptom} despite taking {medication}.",
        "Initiated {treatment} and {medication} for {disease} with {symptom}.",
        "The {symptom} is characteristic of {disease} and treated with {medication}.",
        "{treatment} combined with {medication} effectively manages {disease} and {symptom}.",
        "For {disease} presenting with {symptom}, recommend {medication} and {treatment}."
    ]

    samples = []

    for _ in range(4000):
        template = random.choice(templates)
        disease = random.choice(diseases)
        symptom = random.choice(symptoms)
        treatment = random.choice(treatments)
        medication = random.choice(medications)

        text = template.format(
            disease=disease,
            symptom=symptom,
            treatment=treatment,
            medication=medication
        )
        tokens = text.split()

        entities = []
        i = 0
        while i < len(tokens):
            # Check for disease
            if disease.split()[0] == tokens[i]:
                disease_tokens = disease.split()
                if i + len(disease_tokens) <= len(tokens) and tokens[i:i+len(disease_tokens)] == disease_tokens:
                    entities.append((i, i + len(disease_tokens), 'DISEASE'))
                    i += len(disease_tokens)
                    continue

            # Check for symptom
            if symptom.split()[0] == tokens[i]:
                symptom_tokens = symptom.split()
                if i + len(symptom_tokens) <= len(tokens) and tokens[i:i+len(symptom_tokens)] == symptom_tokens:
                    entities.append((i, i + len(symptom_tokens), 'SYMPTOM'))
                    i += len(symptom_tokens)
                    continue

            # Check for treatment
            if treatment.split()[0] == tokens[i]:
                treatment_tokens = treatment.split()
                if i + len(treatment_tokens) <= len(tokens) and tokens[i:i+len(treatment_tokens)] == treatment_tokens:
                    entities.append((i, i + len(treatment_tokens), 'TREATMENT'))
                    i += len(treatment_tokens)
                    continue

            # Check for medication
            if medication.split()[0] == tokens[i]:
                medication_tokens = medication.split()
                if i + len(medication_tokens) <= len(tokens) and tokens[i:i+len(medication_tokens)] == medication_tokens:
                    entities.append((i, i + len(medication_tokens), 'MEDICATION'))
                    i += len(medication_tokens)
                    continue

            i += 1

        labels = create_iob_format(tokens, entities)

        samples.append({
            'id': f'medical_{len(samples):05d}',
            'tokens': tokens,
            'labels': labels
        })

    # Split
    train_samples = samples[:3200]
    test_samples = samples[3200:]

    # Save
    team_folder = Path("team_08")
    with open(team_folder / "train.jsonl", "w") as f:
        for sample in train_samples:
            f.write(json.dumps(sample) + "\n")

    with open(team_folder / "test.jsonl", "w") as f:
        for sample in test_samples:
            test_sample = {'id': sample['id'], 'tokens': sample['tokens']}
            f.write(json.dumps(test_sample) + "\n")

    readme = """# Team 08: Medical Entity Extraction

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 08 dataset created: {len(train_samples)} train, {len(test_samples)} test")

# ============================================================================
# TEAM 9: JOB POSTING ENTITY EXTRACTION
# ============================================================================

def prepare_team_09():
    """
    Job Posting Entity Extraction - JOBTITLE, COMPANY, SKILL, LOCATION
    """
    print("Preparing Team 09: Job Posting Entity Extraction...")

    job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer",
                  "Marketing Manager", "Sales Representative", "Business Analyst",
                  "DevOps Engineer", "Financial Analyst", "HR Specialist"]
    companies = ["TechCorp", "DataSystems Inc", "Global Solutions", "InnovateLabs",
                 "CloudServices", "Digital Ventures", "SmartTech", "FutureSoft",
                 "NextGen Industries", "PrimeTech"]
    skills = ["Python", "machine learning", "SQL", "project management", "JavaScript",
              "data analysis", "cloud computing", "communication", "leadership", "Agile"]
    locations = ["San Francisco", "New York", "Seattle", "Boston", "Austin",
                 "Chicago", "Los Angeles", "Denver", "Atlanta", "Portland"]

    templates = [
        "{company} is hiring a {job_title} in {location} with {skill} experience.",
        "Seeking {job_title} at {company} located in {location}. Must have {skill} skills.",
        "{job_title} position available at {company}. Requirements: {skill}. Location: {location}.",
        "{company} in {location} needs {job_title} proficient in {skill}.",
        "Join {company} as a {job_title}! Location: {location}. Required: {skill}.",
        "{job_title} role at {company}, {location}. Key skill: {skill}.",
        "We're looking for a {job_title} with {skill} to join {company} in {location}.",
        "{company} ({location}) seeks {job_title}. Must know {skill}.",
        "Excellent opportunity: {job_title} at {company}, {location}. Skills: {skill}.",
        "Apply now: {job_title} position, {company}, {location}. Required: {skill}."
    ]

    samples = []

    for _ in range(4000):
        template = random.choice(templates)
        job_title = random.choice(job_titles)
        company = random.choice(companies)
        skill = random.choice(skills)
        location = random.choice(locations)

        text = template.format(
            job_title=job_title,
            company=company,
            skill=skill,
            location=location
        )
        tokens = text.replace(',', ' , ').replace(':', ' : ').replace('!', ' !').replace('(', ' ( ').replace(')', ' ) ').split()

        entities = []
        i = 0
        while i < len(tokens):
            # Check for job title
            if job_title.split()[0] == tokens[i]:
                jt_tokens = job_title.split()
                if i + len(jt_tokens) <= len(tokens) and tokens[i:i+len(jt_tokens)] == jt_tokens:
                    entities.append((i, i + len(jt_tokens), 'JOBTITLE'))
                    i += len(jt_tokens)
                    continue

            # Check for company
            if company.split()[0] == tokens[i]:
                company_tokens = company.split()
                if i + len(company_tokens) <= len(tokens) and tokens[i:i+len(company_tokens)] == company_tokens:
                    entities.append((i, i + len(company_tokens), 'COMPANY'))
                    i += len(company_tokens)
                    continue

            # Check for skill
            if skill.split()[0] == tokens[i]:
                skill_tokens = skill.split()
                if i + len(skill_tokens) <= len(tokens) and tokens[i:i+len(skill_tokens)] == skill_tokens:
                    entities.append((i, i + len(skill_tokens), 'SKILL'))
                    i += len(skill_tokens)
                    continue

            # Check for location
            if location.split()[0] == tokens[i]:
                location_tokens = location.split()
                if i + len(location_tokens) <= len(tokens) and tokens[i:i+len(location_tokens)] == location_tokens:
                    entities.append((i, i + len(location_tokens), 'LOCATION'))
                    i += len(location_tokens)
                    continue

            i += 1

        labels = create_iob_format(tokens, entities)

        samples.append({
            'id': f'job_{len(samples):05d}',
            'tokens': tokens,
            'labels': labels
        })

    # Split
    train_samples = samples[:3200]
    test_samples = samples[3200:]

    # Save
    team_folder = Path("team_09")
    with open(team_folder / "train.jsonl", "w") as f:
        for sample in train_samples:
            f.write(json.dumps(sample) + "\n")

    with open(team_folder / "test.jsonl", "w") as f:
        for sample in test_samples:
            test_sample = {'id': sample['id'], 'tokens': sample['tokens']}
            f.write(json.dumps(test_sample) + "\n")

    readme = """# Team 09: Job Posting Entity Extraction

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 09 dataset created: {len(train_samples)} train, {len(test_samples)} test")

# ============================================================================
# TEAM 10: RECIPE ENTITY EXTRACTION
# ============================================================================

def prepare_team_10():
    """
    Recipe Entity Extraction - INGREDIENT, QUANTITY, ACTION, EQUIPMENT
    """
    print("Preparing Team 10: Recipe Entity Extraction...")

    ingredients = ["flour", "sugar", "eggs", "butter", "milk", "salt", "chicken",
                   "onions", "garlic", "tomatoes", "cheese", "olive oil", "pepper", "rice"]
    quantities = ["2 cups", "1 tablespoon", "3 cloves", "500g", "1 teaspoon",
                  "2 pounds", "1/2 cup", "4 pieces", "100ml", "a pinch"]
    actions = ["mix", "chop", "bake", "sauté", "boil", "simmer", "whisk",
               "blend", "grill", "roast", "dice", "stir", "pour", "add"]
    equipment = ["oven", "mixing bowl", "pan", "pot", "blender", "whisk",
                 "baking sheet", "skillet", "knife", "spatula", "cutting board"]

    templates = [
        "{action} {quantity} of {ingredient} in a {equipment}.",
        "Add {quantity} {ingredient} to the {equipment} and {action}.",
        "Using a {equipment}, {action} the {ingredient} with {quantity} of {ingredient2}.",
        "{action} {quantity} {ingredient} until golden, then transfer to {equipment}.",
        "In a {equipment}, {action} {quantity} of {ingredient} with {ingredient2}.",
        "{action} the {ingredient} and {ingredient2} in {quantity}. Use a {equipment}.",
        "Combine {quantity} {ingredient} and {action} in a {equipment}.",
        "Place {quantity} of {ingredient} in {equipment} and {action} thoroughly.",
        "{action} {ingredient} with {quantity} of {ingredient2} using a {equipment}.",
        "Heat {equipment}, add {quantity} {ingredient}, and {action} for 5 minutes."
    ]

    samples = []

    for _ in range(4000):
        template = random.choice(templates)
        ingredient = random.choice(ingredients)
        ingredient2 = random.choice([ing for ing in ingredients if ing != ingredient])
        quantity = random.choice(quantities)
        action = random.choice(actions)
        equipment = random.choice(equipment)

        text = template.format(
            ingredient=ingredient,
            ingredient2=ingredient2,
            quantity=quantity,
            action=action,
            equipment=equipment
        )
        tokens = text.replace(',', ' , ').replace('.', ' .').split()

        entities = []
        i = 0
        while i < len(tokens):
            # Check for quantity
            if quantity.split()[0] == tokens[i]:
                quantity_tokens = quantity.split()
                if i + len(quantity_tokens) <= len(tokens) and tokens[i:i+len(quantity_tokens)] == quantity_tokens:
                    entities.append((i, i + len(quantity_tokens), 'QUANTITY'))
                    i += len(quantity_tokens)
                    continue

            # Check for ingredient
            if tokens[i] == ingredient or tokens[i] == ingredient2:
                entities.append((i, i + 1, 'INGREDIENT'))

            # Check for action
            if tokens[i].lower() == action or tokens[i].lower() == action.capitalize():
                entities.append((i, i + 1, 'ACTION'))

            # Check for equipment
            if equipment.split()[0] == tokens[i]:
                equipment_tokens = equipment.split()
                if i + len(equipment_tokens) <= len(tokens) and tokens[i:i+len(equipment_tokens)] == equipment_tokens:
                    entities.append((i, i + len(equipment_tokens), 'EQUIPMENT'))
                    i += len(equipment_tokens)
                    continue

            i += 1

        labels = create_iob_format(tokens, entities)

        samples.append({
            'id': f'recipe_{len(samples):05d}',
            'tokens': tokens,
            'labels': labels
        })

    # Split
    train_samples = samples[:3200]
    test_samples = samples[3200:]

    # Save
    team_folder = Path("team_10")
    with open(team_folder / "train.jsonl", "w") as f:
        for sample in train_samples:
            f.write(json.dumps(sample) + "\n")

    with open(team_folder / "test.jsonl", "w") as f:
        for sample in test_samples:
            test_sample = {'id': sample['id'], 'tokens': sample['tokens']}
            f.write(json.dumps(test_sample) + "\n")

    readme = """# Team 10: Recipe Entity Extraction

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
"""

    with open(team_folder / "README.md", "w") as f:
        f.write(readme)

    print(f"✓ Team 10 dataset created: {len(train_samples)} train, {len(test_samples)} test")

def main():
    """Main execution"""
    print("=" * 60)
    print("Creating Dataset Preparation Environment")
    print("=" * 60)

    create_team_folders()

    print("\n" + "=" * 60)
    print("Preparing Individual Team Datasets")
    print("=" * 60 + "\n")

    # Text Classification Tasks (Teams 1-5)
    prepare_team_01()  # Sentiment Analysis
    prepare_team_02()  # News Category Classification
    prepare_team_03()  # Spam Detection
    prepare_team_04()  # Topic Classification
    prepare_team_05()  # Intent Classification

    # Entity Extraction Tasks (Teams 6-10)
    prepare_team_06()  # Named Entity Recognition
    prepare_team_07()  # Product Attribute Extraction
    prepare_team_08()  # Medical Entity Extraction
    prepare_team_09()  # Job Posting Entity Extraction
    prepare_team_10()  # Recipe Entity Extraction

    print("\n" + "=" * 60)
    print("All Team Datasets Successfully Created!")
    print("=" * 60)
    print("\nDataset Summary:")
    print("- Teams 1-5: Text Classification Tasks (CSV format)")
    print("- Teams 6-10: Entity Extraction Tasks (JSONL format with IOB2 labels)")
    print("\nEach team has:")
    print("  - 3,200 training samples")
    print("  - 800 test samples (labels withheld)")
    print("  - README.md with task description and evaluation metrics")

if __name__ == "__main__":
    main()
