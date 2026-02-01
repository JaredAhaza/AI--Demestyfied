"""
TeamMind AI - Your Team's Knowledge & Onboarding Companion
IBM DevDay: AI Demystified Hackathon 2026
"""

import os
import sys
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TeamMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --background-dark: #0f0f23;
        --card-bg: rgba(30, 30, 60, 0.6);
        --text-primary: #ffffff;
        --text-secondary: #a1a1aa;
        --accent-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
    }
    
    /* Global styles */
    .stApp {
        background: linear-gradient(180deg, #0f0f23 0%, #1a1a3e 50%, #0f0f23 100%);
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        text-align: center;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        color: #a1a1aa;
    }
    
    /* Chat container */
    .chat-container {
        background: rgba(30, 30, 60, 0.4);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Message bubbles */
    .user-message {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: auto;
    }
    
    .assistant-message {
        background: rgba(50, 50, 80, 0.8);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem 0;
        max-width: 80%;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    /* Mode selector cards */
    .mode-card {
        background: rgba(30, 30, 60, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .mode-card:hover {
        border-color: #6366f1;
        transform: translateY(-5px);
        box-shadow: 0 10px 40px rgba(99, 102, 241, 0.3);
    }
    
    .mode-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .mode-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .mode-description {
        color: #a1a1aa;
        font-size: 0.9rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(15, 15, 35, 0.95);
    }
    
    /* Stats cards */
    .stat-card {
        background: rgba(30, 30, 60, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        color: #a1a1aa;
        font-size: 0.85rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 40px rgba(99, 102, 241, 0.4);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(30, 30, 60, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 12px;
        color: white;
        padding: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #6366f1;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mode" not in st.session_state:
    st.session_state.mode = None
if "rag_initialized" not in st.session_state:
    st.session_state.rag_initialized = False

def initialize_rag():
    """Initialize the RAG system with knowledge base documents."""
    from rag_engine import RAGEngine
    
    if not st.session_state.rag_initialized:
        with st.spinner("🔄 Loading knowledge base..."):
            st.session_state.rag_engine = RAGEngine()
            st.session_state.rag_engine.load_documents("knowledge-base")
            st.session_state.rag_initialized = True
    
    return st.session_state.rag_engine

def render_header():
    """Render the main header."""
    st.markdown("""
    <div class="main-header">
        <div class="main-title">🧠 TeamMind AI</div>
        <div class="main-subtitle">Your Team's Knowledge & Onboarding Companion</div>
    </div>
    """, unsafe_allow_html=True)

def render_mode_selection():
    """Render mode selection cards."""
    st.markdown("### Choose Your Mode")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎓 Onboarding Mode", use_container_width=True, key="onboard_btn"):
            st.session_state.mode = "onboarding"
            st.session_state.messages = [{
                "role": "assistant",
                "content": "👋 Welcome to the team! I'm TeamMind AI, your onboarding companion.\n\nI'm here to help you get up to speed quickly. I can answer questions about:\n\n• 🛠️ Setting up your development environment\n• 📋 Team processes and workflows\n• 🔧 Tools and technologies we use\n• 👥 Who to contact for what\n• 📚 Where to find documentation\n\nWhat would you like to know first?"
            }]
            st.rerun()
        st.markdown("""
        <div style="text-align: center; color: #a1a1aa; font-size: 0.9rem; margin-top: 0.5rem;">
            Perfect for new team members getting started
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("📚 Knowledge Mode", use_container_width=True, key="knowledge_btn"):
            st.session_state.mode = "knowledge"
            st.session_state.messages = [{
                "role": "assistant",
                "content": "👋 Hello! I'm TeamMind AI, your team knowledge assistant.\n\nI have access to our team's documentation, including:\n\n• 📖 Technical documentation & architecture\n• 🚀 Deployment processes\n• 💻 Coding standards\n• ❓ FAQs and troubleshooting guides\n\nAsk me anything about our team's processes, tools, or documentation!"
            }]
            st.rerun()
        st.markdown("""
        <div style="text-align: center; color: #a1a1aa; font-size: 0.9rem; margin-top: 0.5rem;">
            Quick answers from team documentation
        </div>
        """, unsafe_allow_html=True)

def render_chat():
    """Render the chat interface."""
    # Mode indicator
    mode_emoji = "🎓" if st.session_state.mode == "onboarding" else "📚"
    mode_name = "Onboarding" if st.session_state.mode == "onboarding" else "Knowledge"
    
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown(f"### {mode_emoji} {mode_name} Mode")
    with col2:
        if st.button("🔄 Switch", key="switch_mode"):
            st.session_state.mode = None
            st.session_state.messages = []
            st.rerun()
    
    # Chat messages container
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-end; margin: 1rem 0;">
                    <div class="user-message">{message["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-start; margin: 1rem 0;">
                    <div class="assistant-message">{message["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    user_input = st.chat_input("Ask me anything about the team...")
    
    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate response using RAG
        try:
            rag_engine = initialize_rag()
            
            # Add context based on mode
            context_prefix = ""
            if st.session_state.mode == "onboarding":
                context_prefix = "The user is a new team member going through onboarding. Be welcoming, patient, and thorough in explanations. "
            else:
                context_prefix = "The user is looking for quick information from team documentation. Be concise and direct. "
            
            response = rag_engine.query(user_input, context_prefix)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            error_msg = f"I encountered an error: {str(e)}\n\nPlease make sure your IBM API key is configured correctly in the `.env` file."
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
        
        st.rerun()

def render_sidebar():
    """Render the sidebar with info and stats."""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2.5rem;">🧠</div>
            <div style="font-size: 1.5rem; font-weight: 700; background: linear-gradient(135deg, #6366f1, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">TeamMind AI</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Stats
        st.markdown("### 📊 Knowledge Base Stats")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Documents", "5", delta=None)
        with col2:
            st.metric("Topics", "12", delta=None)
        
        st.markdown("---")
        
        # Quick links
        st.markdown("### 🔗 Quick Topics")
        quick_topics = [
            "How do I set up my environment?",
            "What's the deployment process?",
            "Who should I contact for help?",
            "What tools does the team use?"
        ]
        
        for topic in quick_topics:
            if st.button(topic, key=f"quick_{topic}", use_container_width=True):
                if st.session_state.mode is None:
                    st.session_state.mode = "knowledge"
                st.session_state.messages.append({"role": "user", "content": topic})
                st.rerun()
        
        st.markdown("---")
        
        # Tech stack
        st.markdown("### 🛠️ Powered By")
        st.markdown("""
        - 🔷 **IBM watsonx.ai**
        - 🪨 **IBM Granite**
        - 🔍 **RAG Pipeline**
        - 🐍 **Streamlit**
        """)
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #6366f1; font-size: 0.8rem;">
            IBM DevDay: AI Demystified<br>Hackathon 2026
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application entry point."""
    render_sidebar()
    render_header()
    
    if st.session_state.mode is None:
        render_mode_selection()
    else:
        render_chat()

if __name__ == "__main__":
    main()
