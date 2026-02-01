# ⚙️ TeamMind AI: Technical Deep Dive

## Architecture Overview

TeamMind AI is a Retrieval-Augmented Generation (RAG) application built with Python. It follows a modular architecture designed for hackathon speed but production scalability.

### Core Components

#### 1. The Brain: IBM watsonx.ai & Granite 3.0
*   **Model**: `ibm/granite-3-8b-instruct`
*   **Why Granite?**: We chose Granite 3.0 because it provides an excellent balance of reasoning capability and latency for enterprise-specific tasks. It adheres to strict data governance, making it safer for corporate knowledge bases than generic consumer models.
*   **Role**:
    *   Synthesizes answers based on retrieved context.
    *   Summarizes complex technical text for the Voice Narrator.

#### 2. The Memory: ChromaDB (Vector Store)
*   **Implementation**: Local persistent ChromaDB instance.
*   **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (via HuggingFace).
*   **Process**:
    1.  Documents (`.md` files) are ingested from `knowledge-base/`.
    2.  Text is split into semantic chunks (size: 500 tokens, overlap: 50).
    3.  Chunks are embedded and stored in Chroma.
    4.  At query time, we use Cosine Similarity to find the top 3 relevant chunks.

#### 3. The Interface: Streamlit
*   **Frontend**: Pure Python web app using Streamlit.
*   **State Management**: Uses `st.session_state` to handle chat history, user mode (Onboarding vs Knowledge), and RAG engine persistence.
*   **UX**: Custom CSS styling for a "Cyber-Minimalist" dark theme.

#### 4. The Voice: ElevenLabs API
*   **Integration**: Direct HTTP REST API calls (to avoid heavy library dependencies).
*   **Workflow**:
    1.  Granite generates a "Voice Script" summary (simplifying the technical jargon).
    2.  Script is sent to ElevenLabs `text-to-speech` endpoint.
    3.  Returns MP3 bytes which are rendered via HTML5 Audio element.

## Key Design Decisions

### Why RAG instead of Fine-tuning?
*   **Freshness**: Team docs change daily. RAG allows us to update knowledge instantly by just dropping a new file in the folder, without expensive re-training.
*   **Accuracy**: RAG reduces hallucinations by grounding the model in retrieved facts (`rag_engine.py` explicitly prompts the model to use *only* the context).

### Why "Dual Mode" UX?
*   **Context Window Optimization**: By knowing if the user is in "Onboarding" mode, we inject a system prompt telling the model to be "welcoming and patient". In "Knowledge" mode, we prompt for "concise and direct". This uses different "personas" of the same underlying model.

## Potential Improvements (For Production)
*   **Live Data Sync**: Connect to Confluence/Google Drive APIs instead of local Markdown files.
*   **Hybrid Search**: Combine Vector Search with Keyword Search (BM25) for better precision on specific acronyms.
*   **Streaming**: Stream tokens to the UI for lower perceived latency.
*   **Containerization**: Dockerize the app for easier deployment on OpenShift.

## Security Considerations
*   API Keys are managed via `.env` and never committed to Git.
*   ChromaDB runs locally, keeping knowledge data within the deployment boundary (no external vector cloud used).
