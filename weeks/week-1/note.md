# Week 01 — 2025-10-6 to 2024-10-12
progress till now: https://youtu.be/VGFpV3Qj4as?t=1359

## ✅ Topics Covered
### Supervised vs Unsupervised Algorithms
Supervised algorithm
- Regression
    - Polynomial Regression
    - Linear Regression
- Classification
    - Logistic Regression
    - Random forest
    - XG Boost
    - Decision trees

Unsupervised Algorithm
- DB Scan
- K-means
- Hierarchical clustering

### ML
###  Deep learning or Neural network
In Artifical neural network we these layers:
    -> input layer, 
    -> hidden layer 1 , 2 or n number of layers, 
    -> output layer etc.

### What to use when to use :
#### Use statistical machine Learning
    -> simple features like a structured etc
    -> Smal Datasets
    -> Limited compute resources
    -> Interpretability   requirements
#### Use Deep Learning
    -> Complex features
    -> Bid datasets
    -> Images videos, Audio
    -> Enough compute resources

### Different Type of neural network Architectures
#### 1. Feed Forward neural network (FNN) -> input layer -> hidden layers -> output
#### 2. Recurrent Neural network RNN
#### 3. Transformer architecture . GPT ( Generative  Pre-trained Transformer) ex: chatGpt

### Tooling or framework for Deep Learning
1. Pytorch - meta
2. TensorFlow - Google

### Generative AI
A category of AI example chat GPT, it can generate videos from text prompt. The whole purpose is generate content.
#### Few examples of different types of models
Text models
1 . GPT - open ai
2. Llama - meta
3. Gemini - Google
4. Claude - anthropic

Image models
1. Dall-E - open AI
2. Stable Diffusion

audio models
1. Audio Gen
2. MusicLM

Video Models
1. Sora

#### Traditional AI
Rule-based, symbolic logic

#### Gen AI
Data-driven, large-scale models

#### Traditional AI VS Gen AI
| **Feature** | **Traditional AI** | **Generative AI** |
|--------------|--------------------|-------------------|
| **Purpose** | Analyze, predict, classify, or make decisions | Generate new content: text, images, code, audio, etc. |
| **Examples of Tasks** | Fraud detection, price prediction, spam filtering | Writing essays, generating images, summarizing text |
| **Type of Output** | Fixed/structured outputs (yes/no, labels, numbers) | Creative/unstructured outputs (sentences, images, music, etc.) |
| **Model Types** | Decision trees, linear regression, SVM, rule-based systems | Large Language Models (LLMs), GANs, diffusion models |
| **Training** | Often supervised learning with labeled data | Pretrained on massive datasets, fine-tuned for specific tasks |
| **Human-Like Capabilities** | Limited (task-specific logic) | High (can mimic human writing, art, reasoning, conversation) |
| **Tools / Examples** | XGBoost, Scikit-Learn models, rule engines | GPT, DALL·E, Claude, Stable Diffusion, Gemini |

 ### Large Language Model (LLM)
 - Based on transformer architecture 
 - Use embeddings + attention mechanisms

Examples of LLMs
- GPt for chatGPT
- PaLM2 - by google
- LLaMA - by meta
- Claude - Anthropic aws

LLM use another technique RLHF - Reinforcement Learning with Human Feedback
to help the LLM to correct on human aspect like what toxic or not

### AI Agents & Agentic AI
You can two types of application using LLM, - Workflows & Agents

**Workflow** - are system where LLms and tools are orchestrated through predefined code paths
 - Workflows again divides into two types:
    - RAG system
    - Tool augmented system


**Agents** - are systems where LLMs dynamically direct their own processes and tools usage, maintaining control over how they accomplish tasks.
- Goal oriented Planning
- give access to tools and Mermory or data
- And it do action autonomous decision based on the data


Ai Agent - can perceive. its environment, make decisions, and take actions to achieve specific goals

Agentic AI - refers to an AI system having one or more advanced agents that operate with autonomy, reason through complex tasks, and proactively take multi-step actions to accomplish goals -without needing detailed instructions

Different types of ChatBot
- Rag chatbot -> Reactive to a question
- Tool Augmented Chatbot - Capability of RAG + tool use
- Agentic AI - Capability of Tool Augmented Chatbot + Reasoning, Planning and Proactivity.

GEn AI - it is one component of AI AGentic AI

| **Aspect** | **Generative AI** | **Agentic AI** |
|-------------|------------------|----------------|
| **Core Purpose** | Create new content (text, images, code, etc.) | Autonomously reason, plan, and act toward goals without needing step-by-step instructions |
| **Output Type** | Unstructured content | Multi-step actions, proactive decisions, evolving plans |
| **Autonomy** | ❌ No autonomy (waits for each prompt) | ✅ High autonomy (initiates actions when needed) |
| **Planning / Reasoning** | ❌ No (or minimal) planning | ✅ Multi-step reasoning and planning |
| **Tool Use** | Rare or external (e.g., via plugins/APIs) | ✅ Uses tools strategically to fulfill complex tasks |
| **Proactivity** | ❌ Always reactive | ✅ Proactive — can initiate tasks when appropriate |
| **Examples** | ChatGPT, DALL·E, Midjourney | HR automation agent that plans onboarding, handles leave logistics, etc. |





## ❌ Skipped / Pending
- ...

## 
## 🔭 Things to explore
- in AI world 
    - inference - where ML generate output from input based on its training on sample data given. 
    - regression 
    - supervised ML  
    - unsupervised ML 
    - clustering 
    - outlier detection 
    - columns are called features
    - the term "Stochastic"
    - RAG - Retrieval Augmented generation
    - tool augmented Chatbot 
    - no - low code tools : -  N8N , Zapier







### Tools
- Python
- Pandas - numpy
- Jupyter
- dmlc XGBoost
- Scikit Learn


## 🔑 Key Insights
- ...
# How general ML Training
We give input &b output to ML Training and it will give model logic. During the Inference phase it take input and model will give output.

### AI Family Tree (0:16 – 3:01)
- AI → ML → Deep Learning → GenAI  
- Statistical AI vs neural approaches (deep learning)
- Hierarchy of concepts

Statistical AI

-sfjhkj 


### Machine Learning (3:02 – 15:54)
- ML = algorithms learn from data  
- Types:  
  - **Supervised**: labeled data (input → output)  
  - **Unsupervised**: no labels (clusters, PCA)  
- Algorithms: Linear/Logistic Regression, Decision Trees  
- Concepts: features, labels, overfitting/underfitting

### Deep Learning (15:55 – 34:17)
- Neural networks: neurons, activation functions  
- Multi-layer = "deep" networks  
- Advantages for high-dimensional data (images, text)  
- Example applications

### Generative AI (34:18 – 36:49)
- Generates new content (text, images, code)  
- Different from discriminative models  
- Use cases: Chatbots, content creation, code assistants

### Traditional AI vs GenAI (36:50 – 39:20)
- **Traditional AI**: rule-based, symbolic logic  
- **GenAI**: data-driven, large-scale models  
- Trade-offs between transparency vs flexibility

### Large Language Models (39:21 – 44:05)
- Based on transformer architectures  
- Use embeddings + attention mechanisms  
- Examples: GPT, LLaMA, Claude  
- Why scale matters

### AI Agents & Agentic AI (44:06 – 56:01)
- **Agent** = decision-making entity with a goal  
- **Agentic AI** = multiple agents working together  
- Features: planning, memory, coordination  
- Frameworks: LangGraph, CrewAI

### AI Agent vs Agentic AI vs GenAI (56:02 – end)
- **GenAI** = content generation  
- **Agent** = one intelligent unit  
- **Agentic AI** = orchestration of many agents  
- Each has unique use cases; often used together

---

## 🔑 Insights
- AI has evolved from rule-based → ML → DL → GenAI → Agentic AI.  
- Deep learning unlocked modern AI progress.  
- GenAI ≠ Agents; they complement each other.  
- LLMs are core enablers for both GenAI and Agentic AI.  

---

## 🎯 Follow-up Questions
- How do LLM embeddings differ from Word2Vec?  
- What makes an agent "intelligent" beyond just tool use?  
- Where does Agentic AI offer advantages over single-agent systems?  

---

## 🎯 Focus for Next Week
- ...

## 📂 Resources
- [Resource 1](link)
- [Resource 2](link)

## 📝 Code Snippets / Examples
```python
# Example code here
```

