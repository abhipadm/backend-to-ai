# Wikipedia Search Agent

**Status:** 🔄 In Progress  
**Week:** 3 (Feb 4-10, 2026)

## 🎯 Project Overview

A simple AI agent that leverages GPT or Claude API to perform intelligent Wikipedia searches and provide natural language responses.

## 🛠️ Tech Stack

- **Python 3.10+**
- **OpenAI API** or **Anthropic Claude API**
- **Wikipedia-API** library
- **Python-dotenv** for environment variables

## 📋 Features

- [x] Basic project setup
- [ ] Wikipedia search integration
- [ ] OpenAI/Claude API integration
- [ ] Natural language query processing
- [ ] Formatted response generation
- [ ] Error handling and validation
- [ ] CLI interface
- [ ] Unit tests

## 🚀 Quick Start

```bash
# Install dependencies
pip install openai anthropic wikipedia-api python-dotenv

# Set up environment variables
cp .env.example .env
# Add your API keys to .env

# Run the agent
python agent.py "Tell me about Python programming language"
```

## 📁 Project Structure

```
wikipedia-search-agent/
├── readme.md              # This file
├── .env.example           # Environment variable template
├── .env                   # Your API keys (git-ignored)
├── requirements.txt       # Python dependencies
├── agent.py               # Main agent implementation
├── wikipedia_tool.py      # Wikipedia search tool
├── llm_interface.py       # LLM API wrapper
└── tests/
    └── test_agent.py      # Unit tests
```

## 🎓 Learning Objectives

- Understanding AI agent architecture
- Working with LLM APIs (OpenAI/Claude)
- Tool integration (Wikipedia)
- Prompt engineering basics
- Error handling in AI systems

## 🔑 Environment Variables

```
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_claude_key_here
```

## 📝 Example Usage

```python
from agent import WikipediaAgent

agent = WikipediaAgent()
response = agent.search("Who invented Python programming?")
print(response)
```

## 🧪 Testing

```bash
python -m pytest tests/
```

## 📚 Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com)
- [Wikipedia API](https://pypi.org/project/Wikipedia-API/)

---

**Next:** AI News & Blog Aggregator Agent (Week 4)
