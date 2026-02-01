# 🏆 Submission Kit: TeamMind AI

Use this content to fill out the hackathon submission form.

---

## 🏷️ Project Title
TeamMind AI

## 📣 Tagline (Short Description)
The personalized AI onboarding companion that turns documentation into conversation.

## 📝 The Problem (Elevator Pitch)
Every growing team faces the same nightmare: Knowledge Fragmentation. Critical information is scattered across wikis, Slack, and PDFs. New hires take weeks to get up to speed, and senior engineers burn hours answering the same "How do I install X?" questions repeatedly. The result? Slow onboarding, frustrated teams, and lost productivity.

## 💡 The Solution
TeamMind AI connects your team's scattered documentation into a single, intelligent brain. It’s not just a search bar; it’s an interactive companion with two distinct modes:

1.  **🎓 Onboarding Mode**: A patient, friendly guide for new hires that proactively suggests next steps.
2.  **📚 Knowledge Mode**: A terse, technical assistant for existing staff needing instant answers.

Featuring a **Voice Narrator** that converts complex technical docs into casual audio explainers for accessibility, and **Grounded RAG** to ensure every answer is backed by real source citations.

## 🛠️ How We Built It (Architecture)
We built TeamMind AI using a Retrieval-Augmented Generation (RAG) architecture:

1.  **Brain**: **IBM watsonx.ai** running the **Granite 3.0 (8B Instruct)** model. We chose Granite for its enterprise-grade compliance and reasoning capabilities.
2.  **Memory**: We use **ChromaDB** to index our Markdown knowledge base locally, ensuring secure and fast vector retrieval.
3.  **Voice**: We integrated **ElevenLabs API** to synthesize the "Voice Narrator", converting Granite's text summaries into human-like audio.
4.  **Interface**: Built with **Streamlit** for a responsive, "cyber-minimalist" UI that includes feedback loops and source citations.

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
