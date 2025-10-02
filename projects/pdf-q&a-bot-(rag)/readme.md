# 📄 PDF Q&A Bot (RAG)

## 📌 Overview
This project builds a **Retrieval-Augmented Generation (RAG)** app:
- Upload a PDF
- Extract embeddings
- Store in ChromaDB
- Query the document using an LLM

---

## 📂 Folder Structure
```
pdf-qa-bot/
├── app.py             # Main script
├── requirements.txt   # Dependencies
├── sample_docs/       # Example PDFs
└── README.md
```

---

## 🚀 How to Run
1. Clone repo & move into project:
   ```bash
   git clone https://github.com/yourusername/backend-to-ai.git
   cd projects/pdf-qa-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Upload a PDF and start asking questions.

---

## 🛠 Tech Stack
- LangChain
- ChromaDB (Vector DB)
- OpenAI API (or local LLM via Hugging Face)

---

## 📊 Demo
👉 [Demo Video Link] (upload to Loom/YouTube)

---

## 🔑 Learnings
- Working with embeddings
- Building RAG pipelines
- Connecting LLMs to external knowledge
