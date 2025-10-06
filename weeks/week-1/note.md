# Week 01 — Learning Notes
**Duration:** October 6-12, 2025

## 📋 Table of Contents
- [Machine Learning Fundamentals](#machine-learning-fundamentals)
- [Deep Learning & Neural Networks](#deep-learning--neural-networks)
- [Generative AI](#generative-ai)
- [AI Agents & Agentic AI](#ai-agents--agentic-ai)
- [Tools & Frameworks](#tools--frameworks)
- [Key Comparisons](#key-comparisons)
- [Terms to Explore](#terms-to-explore)

---

## 🧠 Machine Learning Fundamentals

### Supervised Learning
**Purpose:** Learn from labeled data to make predictions

**Regression Algorithms:**
- Linear Regression
- Polynomial Regression

**Classification Algorithms:**
- Logistic Regression
- Decision Trees
- Random Forest
- XGBoost

### Unsupervised Learning
**Purpose:** Find patterns in unlabeled data

**Clustering Algorithms:**
- K-means
- Hierarchical Clustering
- DBSCAN

---

## 🤖 Deep Learning & Neural Networks

### Neural Network Structure
```
Input Layer → Hidden Layer(s) → Output Layer
```

### When to Use Each Approach

| **Statistical ML** | **Deep Learning** |
|-------------------|-------------------|
| ✅ Simple, structured features | ✅ Complex features |
| ✅ Small datasets | ✅ Big datasets |
| ✅ Limited compute resources | ✅ Images, videos, audio |
| ✅ Need interpretability | ✅ Abundant compute resources |

### Neural Network Architectures
1. **Feed Forward Neural Network (FNN)** - Basic linear flow
2. **Recurrent Neural Network (RNN)** - Handles sequences
3. **Transformer Architecture** - Powers GPT models

---

## 🎨 Generative AI

> **Definition:** AI that generates new content (text, images, audio, video)

### Popular Models by Category

**🔤 Text Models:**
- GPT (OpenAI)
- Llama (Meta)
- Gemini (Google)
- Claude (Anthropic)

**🖼️ Image Models:**
- DALL-E (OpenAI)
- Stable Diffusion

**🎵 Audio Models:**
- Audio Gen
- MusicLM

**🎬 Video Models:**
- Sora

### Large Language Models (LLMs)
- **Architecture:** Transformer-based
- **Key Components:** Embeddings + Attention mechanisms
- **Training Enhancement:** RLHF (Reinforcement Learning with Human Feedback)

---

## 🤝 AI Agents & Agentic AI

### Application Types Using LLMs

**🔄 Workflows** - Predefined code paths
- RAG Systems
- Tool Augmented Systems

**🧠 Agents** - Dynamic, autonomous systems
- Goal-oriented planning
- Tool and memory access
- Autonomous decision-making

### Chatbot Evolution
```
RAG Chatbot → Tool Augmented Chatbot → Agentic AI
   (Reactive)     (RAG + Tools)        (+ Reasoning & Planning)
```

---

## 🛠️ Tools & Frameworks

### Deep Learning Frameworks
- **PyTorch** (Meta)
- **TensorFlow** (Google)

### Data Science & ML Tools
- Python
- Pandas & NumPy
- Jupyter Notebooks
- XGBoost
- Scikit-Learn

### No-Code/Low-Code Tools
- N8N
- Zapier

---

## 🆚 Key Comparisons

### Traditional AI vs Generative AI

| **Feature** | **Traditional AI** | **Generative AI** |
|--------------|--------------------|-------------------|
| **Purpose** | Analyze, predict, classify | Generate new content |
| **Examples** | Fraud detection, spam filtering | Essay writing, image generation |
| **Output Type** | Fixed/structured | Creative/unstructured |
| **Model Types** | Decision trees, SVM, rule-based | LLMs, GANs, diffusion models |
| **Training** | Supervised with labeled data | Massive datasets, fine-tuning |

### Generative AI vs Agentic AI

| **Aspect** | **Generative AI** | **Agentic AI** |
|-------------|------------------|----------------|
| **Core Purpose** | Create content | Autonomous reasoning & planning |
| **Output Type** | Unstructured content | Multi-step actions & decisions |
| **Autonomy** | ❌ Reactive only | ✅ High autonomy |
| **Planning** | ❌ Minimal | ✅ Multi-step reasoning |
| **Tool Use** | ❌ Limited | ✅ Strategic tool usage |
| **Proactivity** | ❌ Always reactive | ✅ Proactive task initiation |




---

## � Terms to Explore

**Core ML Concepts:**
- **Inference** - ML generating output from input based on training data
- **Features** - Column names in datasets
- **Stochastic** - Random/probabilistic processes
- **Outlier Detection** - Identifying anomalous data points

**Advanced AI Concepts:**
- **RAG** - Retrieval Augmented Generation
- **Tool Augmented Chatbot** - Chatbots with external tool capabilities

---

## � Key Insights

> **AI Evolution Timeline:** Rule-based → ML → DL → GenAI → Agentic AI

- 🚀 **Deep learning** unlocked modern AI progress
- 🤝 **GenAI ≠ Agents** - they complement each other
- 🧠 **LLMs** are core enablers for both GenAI and Agentic AI
- 🎯 **Autonomy** is the key differentiator in Agentic AI

---

## ❓ Research Questions

- How do LLM embeddings differ from Word2Vec?
- What makes an agent "intelligent" beyond just tool use?
- Where does Agentic AI offer advantages over single-agent systems?

---

## 🎯 Next Week Focus

- [ ] Hands-on with PyTorch/TensorFlow
- [ ] Build a simple RAG system
- [ ] Explore transformer architecture in detail
- [ ] Practice with supervised learning algorithms

---

## 📂 Resources & References

- [Add your learning resources here]

---

## � Code Snippets & Examples
#### Variable
```python
# Variables
name = "Abhi"
age = 30
height = 1.78

# Printing values
print(name, age, height)

- Variable names are case-sensitive
- Can contain letters, numbers, and underscores
- Should start with a letter or underscore

```

#### Data Types

| Type    | Example            | Description        |
| ------- | ------------------ | ------------------ |
| `int`   | `10`               | Whole number       |
| `float` | `10.5`             | Decimal            |
| `str`   | `"Hello"`          | Text               |
| `bool`  | `True`, `False`    | Logical values     |
| `list`  | `[1, 2, 3]`        | Ordered collection |
| `dict`  | `{"key": "value"}` | Key-value pairs    |

```python
x = 42
y = 3.14
name = "AI Engineer"
is_ready = True

```
#### Lists - Lists store multiple values in order and are mutable

```python
skills = ["Python", "ML", "API", "Agentic AI"]

# Access elements
print(skills[0])   # Python
print(skills[-1])  # Agentic AI

# Modify
skills.append("LangChain")
skills.remove("API")

# Loop through
for skill in skills:
    print(skill)
```
#### Dictionaries
- Dictionaries store key-value pairs
```python
developer = {
    "name": "Abhi",
    "role": "Backend Developer",
    "experience": 10
}

# Access values
print(developer["name"])     # Abhi
# Add new key
developer["speciality"] = "AI"
# Loop through keys & values
for key, value in developer.items():
    print(f"{key}: {value}")

```
#### Loops
##### For Loop - Iterates over sequences (lists, strings, etc.)
``` python
for i in range(5):
    print("Iteration:", i)
```
#### While Loop
```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

---

## ✅ Completed Topics
- [x] AI Basic
   - [x] Supervised vs Unsupervised Learning
   - [x] Deep Learning Fundamentals
   - [x] Neural Network Architectures
   - [x] Generative AI Overview
   - [x] LLMs and Transformer Architecture
   - [x] AI Agents vs Workflows
   - [x] Traditional AI vs Modern AI Approaches
- [x] Install Anaconda installation
- [x] Python basics (variables, lists, dicts, loops); 

## 🔄 Pending Topics

- [ ] Write script to parse JSON + CSV

