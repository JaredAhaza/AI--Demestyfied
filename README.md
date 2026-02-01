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

**TeamMind AI** is an intelligent assistant that acts as a single source of truth for your team, powered by IBM watsonx.ai.

### ✨ Key Features
*   **🎓 Onboarding Mode**: Guided experience specifically tailored for new hires.
*   **📚 Knowledge Mode**: Instant technical answers for existing team members.
*   **🎙️ Voice Narrator** (New!): Uses ElevenLabs to audibly summarize complex technical details into friendly, casual explainers.
*   **⚡ Quick Actions**: One-click solutions for common team questions.

## 🛠️ Technology Stack

*   **IBM watsonx.ai**: Powering the core AI capabilities.
*   **IBM Granite 3.0 (8B Instruct)**: The high-performance foundation model for text generation and summarization.
*   **RAG (Retrieval-Augmented Generation)**: Grounds answers in your actual team documentation (`knowledge-base/` folder).
*   **ChromaDB**: Vector storage for semantic search.
*   **Streamlit**: Fast, interactive web interface.
*   **ElevenLabs**: Text-to-Speech synthesis for the Voice Narrator.

## 🏗️ Architecture

```mermaid
graph LR
    User[User] --> UI[Streamlit UI]
    UI --> RAG[RAG Engine]
    RAG --> Chroma[ChromaDB Vector Store]
    RAG --> WatsonX[IBM watsonx.ai (Granite 3.0)]
    UI --> Voice[Voice Engine]
    Voice --> Eleven[ElevenLabs API]
```

## 🚀 Quick Start

### Prerequisites
*   Python 3.10+
*   IBM Cloud API Key
*   ElevenLabs API Key (Optional, for voice)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-repo/TeamMind-AI.git
    cd TeamMind-AI
    ```

2.  **Create virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment**
    Create a `.env` file with your credentials:
    ```env
    IBM_API_KEY=your_ibm_key
    WATSONX_PROJECT_ID=your_project_id
    WATSONX_URL=https://us-south.ml.cloud.ibm.com
    ELEVENLABS_API_KEY=your_elevenlabs_key
    ```

5.  **Run the application**
    ```bash
    streamlit run app.py
    ```

## 📁 Project Structure

```
AI--Demestyfied/
├── app.py              # Main Streamlit Application
├── rag_engine.py       # Core RAG Logic (Watsonx + ChromaDB)
├── voice_engine.py     # Voice Synthesis Logic (ElevenLabs)
├── requirements.txt    # Python Dependencies
├── .env                # Configuration Secrets
└── knowledge-base/     # Team Documentation (Markdown)
    ├── team-docs/
    │   ├── onboarding-guide.md
    │   ├── deployment-process.md
    │   └── ...
    └── faqs/
```

## 👥 Team

- **Jared Ahaza** - *Lead Developer*

## 📝 License

MIT License

---

*Built with ❤️ for IBM DevDay: AI Demystified Hackathon 2026*