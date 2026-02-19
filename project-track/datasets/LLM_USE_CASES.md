# LLM Use Cases for Project Datasets

This document provides guidance on how these datasets can be adapted or extended for Large Language Model (LLM) use cases, going beyond traditional classification tasks.

---

## Overview

While the current datasets are designed for traditional ML/DL classification approaches, they can be enhanced or repurposed for LLM-specific tasks that emphasize **reasoning**, **explanation**, and **generation** capabilities.

---

## Dataset-Specific LLM Applications

### 📊 Text Classification Datasets (01-05)

#### Dataset 01: Sentiment Analysis
**Current Task**: Binary sentiment classification

**LLM Enhancements**:
- **Sentiment + Reasoning**: "Classify the sentiment AND explain why"
- **Aspect-Based Sentiment**: Extract what aspects are positive/negative
- **Sentiment Intensity**: Rate sentiment on a scale with justification
- **Counterfactual Generation**: "How would you change this review to make it negative?"

**Example Prompt**:
```
Review: "This movie was absolutely fantastic! The acting exceeded my expectations."

Task: Classify sentiment and explain your reasoning.

Expected Output:
- Sentiment: Positive
- Reasoning: The review uses strong positive language ("absolutely fantastic") and explicitly states expectations were exceeded. The enthusiastic tone and exclamation mark reinforce the positive sentiment.
```

---

#### Dataset 02: News Category Classification
**Current Task**: Multi-class news categorization

**LLM Enhancements**:
- **Classification + Summarization**: Categorize AND provide a 1-sentence summary
- **Key Entity Extraction**: Identify main entities relevant to the category
- **Multi-Label Classification**: Assign multiple relevant categories with confidence
- **Category Reasoning**: Explain which keywords/phrases indicate the category

**Example Prompt**:
```
Headline: "New smartphone released with innovative AI technology."

Task:
1. Classify into category
2. Extract key concepts
3. Generate a brief summary

Expected Output:
- Category: Technology
- Key Concepts: smartphone, AI technology, product release
- Summary: Technology company announces new smartphone featuring artificial intelligence capabilities.
```

---

#### Dataset 03: Spam Detection
**Current Task**: Binary spam/ham classification

**LLM Enhancements**:
- **Spam Detection + Risk Analysis**: Classify and explain the threat level
- **Phishing Pattern Detection**: Identify specific manipulation techniques used
- **Safe Message Rewriting**: Show how to make a legitimate version
- **Urgency Detection**: Rate the urgency language on a scale

**Example Prompt**:
```
Message: "URGENT: Your bank account has been locked. Verify at secure-verify.com immediately."

Task: Detect spam and analyze manipulation techniques.

Expected Output:
- Classification: Spam
- Threat Level: High (phishing attempt)
- Manipulation Techniques:
  1. Urgency ("URGENT", "immediately")
  2. Fear induction ("account locked")
  3. Suspicious domain ("secure-verify.com")
- Recommendation: Delete immediately, never click links in unsolicited messages
```

---

#### Dataset 04: Topic Classification
**Current Task**: Academic discipline classification

**LLM Enhancements**:
- **Classification + Concept Extraction**: Identify key technical concepts
- **Cross-Domain Detection**: Identify if paper spans multiple fields
- **Methodology Identification**: Extract research methods mentioned
- **Difficulty Rating**: Estimate technical complexity level

**Example Prompt**:
```
Abstract: "We present a novel deep learning model for image classification..."

Task:
1. Classify discipline
2. Extract key concepts
3. Identify methodology
4. Rate technical difficulty (1-5)

Expected Output:
- Discipline: Computer Science
- Key Concepts: deep learning, image classification, neural networks
- Methodology: Experimental/empirical evaluation
- Difficulty: 4/5 (Advanced machine learning techniques)
```

---

#### Dataset 05: Intent Classification
**Current Task**: Customer query intent detection

**LLM Enhancements**:
- **Intent + Response Generation**: Detect intent AND generate appropriate response
- **Sentiment + Intent**: Combine emotional tone with intent
- **Multi-Intent Detection**: Handle queries with multiple intents
- **Priority Assessment**: Rate urgency and priority level

**Example Prompt**:
```
Query: "I want to return my laptop and get a refund. It doesn't work properly."

Task:
1. Detect intent(s)
2. Assess emotional tone
3. Suggest appropriate response
4. Rate priority level

Expected Output:
- Primary Intent: Refund Request
- Secondary Intent: Technical Support (underlying issue)
- Emotional Tone: Frustrated but polite
- Priority: High (product defect)
- Suggested Response: "I apologize for the inconvenience. Let me help you process the return and refund immediately. May I have your order number?"
```

---

### 🏷️ Entity Extraction Datasets (06-10)

#### Dataset 06: Named Entity Recognition
**Current Task**: Extract PER, LOC, ORG entities

**LLM Enhancements**:
- **Entities + Relations**: Extract entities AND relationships between them
- **Entity Disambiguation**: Resolve ambiguous entity references
- **Entity Linking**: Link entities to knowledge bases
- **Event Extraction**: Identify events involving the entities

**Example Prompt**:
```
Text: "Maria Garcia visited London last week for a conference organized by Microsoft."

Task:
1. Extract all entities
2. Identify relationships
3. Extract events

Expected Output:
- Entities:
  - Person: Maria Garcia
  - Location: London
  - Organization: Microsoft
- Relationships:
  - Maria Garcia [visited] London
  - Microsoft [organized] conference
  - Conference [held in] London
- Event: Business conference attendance
```

---

#### Dataset 07: Product Attribute Extraction
**Current Task**: Extract BRAND, PRODUCT, PRICE, FEATURE

**LLM Enhancements**:
- **Extraction + Comparison**: Compare products based on extracted attributes
- **Value Proposition**: Identify the main selling point
- **Recommendation Generation**: Suggest for whom this product is suitable
- **Competitive Analysis**: Compare with similar products

**Example Prompt**:
```
Text: "The Apple smartphone costs $799 and features wireless technology."

Task:
1. Extract product attributes
2. Generate value proposition
3. Suggest target customer

Expected Output:
- Attributes:
  - Brand: Apple
  - Product: smartphone
  - Price: $799
  - Feature: wireless technology
- Value Proposition: Premium smartphone with convenient wireless capabilities
- Target Customer: Tech-savvy users willing to invest in quality and convenience
```

---

#### Dataset 08: Medical Entity Extraction
**Current Task**: Extract DISEASE, SYMPTOM, TREATMENT, MEDICATION

**LLM Enhancements**:
- **Clinical Reasoning**: Explain relationships between entities
- **Severity Assessment**: Rate condition severity based on symptoms
- **Treatment Rationale**: Explain why treatment is appropriate
- **Drug Interaction Warnings**: Identify potential conflicts

**Example Prompt**:
```
Text: "Patient presents with fever and was diagnosed with pneumonia. Treatment includes amoxicillin and rest."

Task:
1. Extract medical entities
2. Explain treatment rationale
3. Identify entity relationships

Expected Output:
- Entities:
  - Symptom: fever
  - Disease: pneumonia
  - Medication: amoxicillin
  - Treatment: rest
- Relationships:
  - Fever is symptom of pneumonia
  - Amoxicillin treats bacterial pneumonia
  - Rest aids recovery
- Treatment Rationale: Amoxicillin is an antibiotic appropriate for bacterial pneumonia; rest supports immune response
```

---

#### Dataset 09: Job Posting Entity Extraction
**Current Task**: Extract JOBTITLE, COMPANY, SKILL, LOCATION

**LLM Enhancements**:
- **Job Matching**: Match candidates to requirements
- **Skill Gap Analysis**: Identify missing skills for a role
- **Salary Estimation**: Estimate salary range based on attributes
- **Career Path Suggestions**: Suggest progression paths

**Example Prompt**:
```
Text: "TechCorp is hiring a Software Engineer in San Francisco with Python experience."

Task:
1. Extract job attributes
2. Identify required skills
3. Suggest related roles
4. Estimate experience level

Expected Output:
- Attributes:
  - Job Title: Software Engineer
  - Company: TechCorp
  - Location: San Francisco
  - Required Skill: Python
- Experience Level: Mid-level (based on single skill requirement)
- Related Roles: Backend Developer, Full Stack Engineer, Data Engineer
- Career Progression: Senior Software Engineer → Tech Lead → Engineering Manager
```

---

#### Dataset 10: Recipe Entity Extraction
**Current Task**: Extract INGREDIENT, QUANTITY, ACTION, EQUIPMENT

**LLM Enhancements**:
- **Recipe Adaptation**: Suggest ingredient substitutions
- **Dietary Restrictions**: Adapt for allergies/preferences
- **Cooking Time Estimation**: Estimate total preparation time
- **Skill Level Assessment**: Rate recipe difficulty

**Example Prompt**:
```
Text: "Mix 2 cups of flour in a mixing bowl."

Task:
1. Extract recipe components
2. Suggest ingredient substitution
3. Rate difficulty
4. Estimate time

Expected Output:
- Components:
  - Action: Mix
  - Quantity: 2 cups
  - Ingredient: flour
  - Equipment: mixing bowl
- Substitution: Can replace wheat flour with gluten-free flour blend (1:1 ratio)
- Difficulty: Beginner (simple mixing task)
- Time: ~2 minutes
```

---

## Advanced LLM Use Cases (Future Extension)

### 1. Few-Shot Learning
Convert datasets to few-shot prompts:
```
Example 1: [text] → [classification + reasoning]
Example 2: [text] → [classification + reasoning]
Example 3: [text] → [classification + reasoning]

Now classify: [new text]
```

### 2. Chain-of-Thought Reasoning
Add reasoning steps before final answer:
```
Text: [input]
Let's think step by step:
1. First, I notice...
2. This suggests...
3. Therefore...
Answer: [classification]
```

### 3. Multi-Task Learning
Combine multiple objectives:
```
Task: Given this text, perform:
1. Classification
2. Entity extraction
3. Summarization
4. Key insight generation
```

### 4. Instruction Following
Format as instruction-response pairs:
```
Instruction: Classify the sentiment of this review and explain your reasoning in 2-3 sentences.
Input: [review text]
Response: [classification + explanation]
```

---

## Implementation Considerations

### For Students Using LLMs:

1. **Prompt Engineering**: Design effective prompts that elicit desired behavior
2. **Output Parsing**: Structure LLM responses for evaluation
3. **Consistency**: Ensure reproducible results across runs
4. **Evaluation**: Compare LLM performance against fine-tuned models
5. **Cost Analysis**: Consider API costs vs. model training costs

### Metrics for LLM Evaluation:

- **Traditional**: Accuracy, F1, Precision, Recall
- **LLM-Specific**:
  - Explanation quality (human evaluation)
  - Reasoning coherence
  - Hallucination rate
  - Instruction following accuracy
  - Cost per prediction

---

## Suggested Project Extensions

If you want to incorporate LLM capabilities into your project:

### Option 1: Hybrid Approach
- Use traditional models for classification
- Use LLMs for explanation generation
- Compare both approaches

### Option 2: Prompt Engineering Study
- Design multiple prompt strategies
- Compare zero-shot vs. few-shot performance
- Analyze which prompts work best

### Option 3: LLM Fine-Tuning
- Fine-tune smaller LLMs on datasets
- Compare with larger models via API
- Analyze cost-performance tradeoffs

### Option 4: Evaluation Framework
- Create human evaluation rubrics
- Design automated quality metrics
- Build comparison dashboard

---

## Resources

### LLM APIs & Platforms:
- OpenAI (GPT-4, GPT-3.5)
- Anthropic Claude
- Google Gemini
- Hugging Face (open-source models)

### Frameworks:
- LangChain (LLM application framework)
- LlamaIndex (data framework for LLMs)
- Guidance (prompt engineering)
- LMQL (query language for LLMs)

### Evaluation Tools:
- BERTScore (semantic similarity)
- ROUGE (summarization quality)
- BLEU (generation quality)
- Human evaluation platforms

---

## Conclusion

These datasets provide a strong foundation for both traditional ML/DL and modern LLM approaches. Students can choose to:

1. **Stick to the original task**: Focus on classification/extraction with traditional models
2. **Add LLM components**: Enhance with explanations and reasoning
3. **Pure LLM approach**: Use prompt engineering and few-shot learning
4. **Comparative study**: Evaluate traditional models vs. LLMs

The choice depends on learning objectives, available resources, and project scope.

---

**Note**: This document is provided as additional guidance. The core project requirements remain focused on traditional ML/DL approaches with Neural Networks and Transformers. LLM enhancements are optional extensions for advanced students.

**Last Updated**: 2026-02-19
