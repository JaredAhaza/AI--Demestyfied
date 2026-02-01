# 🧠 TeamMind AI

### Your Team's Knowledge & Onboarding Companion

> **IBM DevDay: AI Demystified Hackathon 2026**
> Theme: "From Idea to Deployment" - Simplifying steps that slow teams down

---

## 🎯 The Problem

Teams lose countless hours to knowledge fragmentation:
- ⏰ New hires take weeks to get up to speed
- 🔄 Team members repeatedly answer the same questions
- 📂 Critical knowledge scattered across docs, wikis, Slack, and people's heads
- 🚪 Context gets lost when team members leave

## 💡 Our Solution

**TeamMind AI** is an intelligent assistant that serves dual purposes:

### 🎓 Onboarding Mode
- Guided onboarding with contextual answers
- Proactively suggests information new hires commonly need
- Reduces time-to-productivity for new team members

### 📚 Knowledge Mode
- Instant answers from team documentation, SOPs, and past decisions
- Reduces interruptions and speeds up daily work
- Preserves institutional knowledge

## 🛠️ Technology Stack

- **IBM watsonx.ai** - Foundation model inference and AI capabilities
- **IBM Granite** - Open-source, efficient language models
- **Langflow** - Visual AI workflow builder for RAG pipelines
- **RAG (Retrieval-Augmented Generation)** - Knowledge-grounded responses

## 🏗️ Architecture

```
User Interface (Web Chat)
         │
         ▼
    Langflow RAG Pipeline
         │
    ┌────┴────┐
    ▼         ▼
Vector DB   IBM Granite
(Knowledge) (via watsonx.ai)
```

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start the development server
npm run dev
```

## 📁 Project Structure

```
AI--Demestyfied/
├── frontend/          # Web interface
├── backend/           # API server
├── knowledge-base/    # Sample team documents
├── langflow/          # Langflow workflow configs
└── docs/              # Documentation
```

## 👥 Team

- [Your Name]

## 📝 License

MIT License

---

*Built with ❤️ for IBM DevDay: AI Demystified Hackathon 2026*