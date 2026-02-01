# 🏆 Submission Kit: TeamMind AI

Use this content to fill out the hackathon submission form.

---

## 🏷️ Project Title
TeamMind AI

## 📣 Tagline (Short Description)
The personalized AI onboarding companion that turns documentation into conversation.

## 📝 Problem and Solution Statement (500 Words Max)

**The Problem: The "New Hire" Knowledge Gap**
In modern agile teams, critical knowledge is fragmented. It lives in outdated wikis, buried Slack threads, and the minds of senior engineers. When a new developer joins, they face a steep "Time-to-Productivity" curve, spending weeks hunting for setup instructions or deployment keys. Meanwhile, senior staff are constantly interrupted to answer the same repetitive questions ("Where are the API keys?", "How do I deploy to staging?"). This inefficiency costs thousands of dollars per hire and burns out team leads.

**The Solution: TeamMind AI**
TeamMind AI is an intelligent, agentic onboarding companion that serves as the single source of truth for your team. Unlike a static search bar, it offers a dual-mode experience tailored to the user's context:

1.  **Onboarding Mode**: Designed for new hires, this agent acts as a patient mentor. It proactively guides users through setup, explains acronyms in plain English, and uses a simplified tone to reduce overwhelm.
2.  **Knowledge Mode**: Designed for existing engineers, this agent switches to a terse, technical persona for instant fact-retrieval and troubleshooting.

**Key Innovations:**
*   **Grounded RAG**: Every answer is strictly grounded in your actual team documentation (Markdown/Docs) to prevent hallucinations, with visible source citations for trust.
*   **Voice Narrator**: We integrated the ElevenLabs API to create an accessibility-first experience. The agent simplifies complex technical documentation into a casual audio script, allowing users to "listen and learn" while setting up their environment hands-free.
*   **Safety First**: Validates input and scans documents for accidental secret leaks (like AWS keys) before they enter the knowledge base.

TeamMind AI transforms the chaotic "first week" experience from a frustration into a streamlined, interactive conversation.

---

## 🤖 How we used Agentic AI and IBM watsonx Orchestrate

We architected TeamMind AI as an **Agentic Workflow** rather than a simple chatbot. The system does not just predict the next word; it orchestrates a multi-step reasoning process to fulfill user intent.

**1. The Brain (IBM Granite 3.0 via watsonx.ai)**
We utilized the **IBM Granite 3.0 (8B Instruct)** foundation model as the central reasoning agent. We chose Granite specifically for its enterprise-grade adherence to instructions and low latency. The model is effectively "orchestrating" the conversation by:
*   **Intent Classification**: Deciding if the user needs a detailed onboarding guide or a quick technical fact.
*   **Context Management**: Dynamically switching its system prompt "persona" based on the user's selected mode (Patient Mentor vs. Technical Lead).

**2. Tool Use (RAG & Voice)**
The agent has access to specialized tools to augment its capabilities:
*   **Retrieval Tool**: The agent queries our local **ChromaDB** vector store to retrieve relevant document chunks, ensuring all "thoughts" are grounded in reality.
*   **Synthesis Tool**: The agent acts as a "scriptwriter," taking technical data and summarising it into a casual script, which it then hands off to the **ElevenLabs API** for voice synthesis.

By combining IBM watsonx.ai's reasoning capabilities with these external tools, we created a system that perceives, reasons, acts, and speaks—a true AI agent for team productivity.

## 💻 Tech Stack Tags
Python, IBM watsonx, IBM Granite, RAG, ChromaDB, Streamlit, ElevenLabs, LangChain

## 🎬 Demo Video Script (Suggested)
*(2 Minutes Max)*

1.  **Intro (0:00-0:15)**: "Hi, I'm [Name]. We've all been the 'new hire' lost in documentation. Today we're solving that with TeamMind AI."
2.  **The "Ah-ha" Moment (0:15-0:45)**:
    *   *Action*: Click "Onboarding Mode". Ask "How do I set up my env?".
    *   *Voiceover*: "Notice the friendly tone. It doesn't just dump text; it guides me. And look—it cites the exact document source here."
3.  **The "Wow" Feature (0:45-1:15)**:
    *   *Action*: "Reading text is slow. Let's listen." (Click Audio Player).
    *   *Voiceover*: "Our Voice Narrator uses Granite to simplify the jargon and ElevenLabs to speak it. Perfect for auditory learners."
4.  **Governance/Trust (1:15-1:45)**:
    *   *Action*: Switch to "Knowledge Mode". Ask a query. Show the "Sources" expander.
    *   *Voiceover*: "For seniors, it switches to technical brevity. And we have a built-in security scanner that rejected a file with a fake AWS key during ingestion."
5.  **Closing (1:45-2:00)**: "TeamMind AI: From Idea to Onboarded, in minutes."

## 🔗 Repository URL
[Link to your GitHub Repo]
