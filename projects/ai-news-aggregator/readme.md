# AI News & Blog Aggregator Agent

**Status:** 📋 Planned  
**Week:** 4 (Feb 11-17, 2026)

## 🎯 Project Overview

An intelligent news and blog aggregator that uses AI to fetch, summarize, and categorize content from multiple sources.

## 🛠️ Tech Stack

### Language Model Options
- **OpenAI GPT-4 Turbo** (Recommended for production)
- **Anthropic Claude** (Great for longer context)
- **Mistral** or **Mixtral** (Open-source alternatives)

### Agent Orchestration
- **LangChain** - Versatile framework for LLM applications
- **CrewAI** - Multi-agent collaboration
- **AutoGen** - Microsoft's agent framework

### Web Scraping & Parsing
- **Feedparser** - RSS feed parsing
- **BeautifulSoup4** - HTML parsing
- **Playwright** or **Puppeteer** - Dynamic content scraping
- **Requests** - HTTP requests

### Storage
- **Vector DB**: Chroma or Weaviate for semantic search
- **SQL**: SQLite or PostgreSQL for metadata
- **Notion API** - For bookmarking (optional)

### Scheduling
- **Cron jobs** - Simple daily/weekly runs
- **Airflow** - Advanced workflow orchestration
- **Schedule** - Python library for simple scheduling

## 📋 Core Features

### 🤖 Agent Capabilities
- [ ] **Scrape & Summarize**: Use Playwright to scrape dynamic content, then summarize with LLM
- [ ] **Smart Categorization**: Auto-tag content by topics (LLMs, MLOps, Backend, DevTools, GenAI)
- [ ] **Intelligent Ranking**: Score articles based on:
  - Recency and freshness
  - Popularity metrics (views, engagement)
  - Relevance to your learning interests
- [ ] **Multi-Source Aggregation**: Fetch from blogs, news, GitHub, YouTube, newsletters
- [ ] **Duplicate Detection**: Identify and merge similar content
- [ ] **Notification System**: Daily/weekly digests via Notion, Slack, or email

### 🎯 Standard Features
- [ ] RSS feed parsing from multiple sources
- [ ] AI-powered article summarization
- [ ] Sentiment analysis
- [ ] SQLite/Postgres metadata storage
- [ ] Vector database for semantic search

## 🚀 Quick Start

```bash
# Install dependencies
pip install openai anthropic feedparser beautifulsoup4 schedule requests

# Configure sources
cp config.example.json config.json
# Edit config.json with your RSS feeds

# Run the aggregator
python aggregator.py
```

## 📁 Project Structure

```
ai-news-aggregator/
├── readme.md              # This file
├── .env.example           # Environment variable template
├── .env                   # Your API keys (git-ignored)
├── config.json            # RSS feed sources
├── requirements.txt       # Python dependencies
├── aggregator.py          # Main aggregator agent
├── feed_parser.py         # RSS feed parsing
├── summarizer.py          # AI summarization
├── categorizer.py         # Content categorization
├── database.py            # SQLite storage
├── scheduler.py           # Automated runs
└── tests/
    └── test_aggregator.py # Unit tests
```

## 🎓 Learning Objectives

- Building autonomous AI agents
- Working with RSS feeds
- AI-powered text summarization
- Content categorization with LLMs
- Task automation and scheduling
- Data persistence with SQLite

## 🔑 Environment Variables

```
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_claude_key_here
```

## 📰 Curated News Sources

### 📝 Blogs & Technical Content
- **Towards Data Science** - ML & Data Science articles
- **Gradient** - AI research and insights
- **Andrej Karpathy's Blog** - Deep learning from first principles
- **Latent Space** - AI engineering podcast & blog
- **Raza Habib's Blog** - LLM applications and infrastructure

### 📰 News & Updates
- **The Decoder** - AI news and analysis
- **VentureBeat AI** - AI business and technology news
- **TechCrunch AI** - Startup and tech news
- **Ben's Bites** - Daily AI newsletter
- **Hacker News** - Tech community discussions

### 💻 GitHub Trending
- **AI/ML Repositories** - Trending projects in AI
- **Backend Architecture** - System design patterns
- **LangChain/CrewAI** - Agent framework updates

### 🎥 YouTube Channels
- **Tech With Tim** - Python & AI tutorials
- **Two Minute Papers** - AI research summaries
- **Yannic Kilcher** - Paper reviews and discussions

### 📧 Newsletters
- **Substack feeds** - AI thought leaders
- **Medium publications** - Technical deep-dives

## 🧩 Bonus Features (Advanced)

### 💬 Ask Me Anything (RAG)
- Query your curated content library using natural language
- Semantic search across all saved articles
- Context-aware answers from your aggregated knowledge base

### 🔖 Auto-Bookmark System
- Save top-ranked articles to Notion database
- Auto-commit summaries to GitHub repo
- Tag and organize by learning goals

### 🎧 Voice Briefings
- Convert daily summaries to audio using TTS (Text-to-Speech)
- Listen to your AI news digest during commute
- Podcast-style daily briefings

### 📊 Analytics Dashboard
- Track content consumption patterns
- Identify trending topics in your sources
- Visualize learning progress over time

### 🔔 Smart Notifications
- Slack/Discord integration
- Email digests with customizable frequency
- Push notifications for high-priority content

## 📝 Example Usage

```python
from aggregator import NewsAggregator

# Basic usage
aggregator = NewsAggregator()
aggregator.fetch_latest()
digest = aggregator.generate_daily_digest()
print(digest)

# Advanced RAG query
response = aggregator.ask("What are the latest developments in LangGraph?")
print(response)

# Voice briefing
aggregator.generate_audio_briefing(output="daily_briefing.mp3")
```

## 🧪 Testing

```bash
python -m pytest tests/
```

## 📚 Resources

- [Feedparser Documentation](https://feedparser.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Schedule Library](https://schedule.readthedocs.io/)

---

**Previous:** Wikipedia Search Agent (Week 3)  
**Next:** Titanic Data Analysis (Week 4)
