"""
RAG Engine - Retrieval-Augmented Generation using IBM watsonx.ai and Granite
"""

import os
import sys
from pathlib import Path
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class RAGEngine:
    """RAG Engine using IBM watsonx.ai with Granite models."""
    
    def __init__(self):
        """Initialize the RAG engine with IBM watsonx.ai."""
        self.api_key = os.getenv("IBM_API_KEY")
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        self.url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        
        if not self.api_key or self.api_key == "your_ibm_api_key_here":
            raise ValueError("Please set IBM_API_KEY in your .env file")
        if not self.project_id or self.project_id == "your_project_id_here":
            raise ValueError("Please set WATSONX_PROJECT_ID in your .env file")
        
        self.documents = []
        self.chunks = []
        self.embeddings = None
        self.vector_store = None
        
        # Initialize watsonx.ai client
        self._init_watsonx()
    
    def _safe_print(self, text: str):
        """Safely print text handling unicode characters on Windows."""
        try:
            print(text)
        except UnicodeEncodeError:
            # Fallback for Windows consoles that can't handle emojis
            print(text.encode('ascii', 'replace').decode('ascii'))
            
    def _init_watsonx(self):
        """Initialize IBM watsonx.ai client."""
        try:
            from ibm_watsonx_ai import Credentials
            from ibm_watsonx_ai.foundation_models import ModelInference
            from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
            
            # Set up credentials
            self.credentials = Credentials(
                url=self.url,
                api_key=self.api_key
            )
            
            # Initialize the model - using Granite
            # Using IBM Granite 13B Instruct v2 for generation
            self.model = ModelInference(
                model_id="ibm/granite-13b-instruct-v2",
                credentials=self.credentials,
                project_id=self.project_id,
                params={
                    "decoding_method": "greedy",
                    "max_new_tokens": 1000,
                    "min_new_tokens": 50,
                    "temperature": 0.7,
                    "top_k": 50,
                    "top_p": 0.95,
                    "repetition_penalty": 1.1
                }
            )
            
            self._safe_print("✅ IBM watsonx.ai initialized successfully!")
            
        except ImportError:
            self._safe_print("⚠️ ibm-watsonx-ai not installed. Using fallback mode.")
            self.model = None
        except Exception as e:
            self._safe_print(f"⚠️ Error initializing watsonx: {e}")
            self.model = None
    
    def load_documents(self, knowledge_base_path: str):
        """Load documents from the knowledge base directory."""
        kb_path = Path(knowledge_base_path)
        
        if not kb_path.exists():
            self._safe_print(f"⚠️ Knowledge base path not found: {kb_path}")
            return
        
        # Load all markdown files
        for md_file in kb_path.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                self.documents.append({
                    "path": str(md_file),
                    "filename": md_file.name,
                    "content": content
                })
                self._safe_print(f"📄 Loaded: {md_file.name}")
            except Exception as e:
                self._safe_print(f"⚠️ Error loading {md_file}: {e}")
        
        # Create chunks from documents
        self._create_chunks()
        
        # Create vector store
        self._create_vector_store()
        
        self._safe_print(f"✅ Loaded {len(self.documents)} documents, {len(self.chunks)} chunks")
    
    def _create_chunks(self, chunk_size: int = 500, overlap: int = 50):
        """Split documents into chunks for better retrieval."""
        for doc in self.documents:
            content = doc["content"]
            
            # Split by sections (headers)
            sections = content.split("\n## ")
            
            for i, section in enumerate(sections):
                if i > 0:
                    section = "## " + section
                
                # If section is too long, split further
                if len(section) > chunk_size:
                    words = section.split()
                    current_chunk = []
                    current_length = 0
                    
                    for word in words:
                        current_chunk.append(word)
                        current_length += len(word) + 1
                        
                        if current_length >= chunk_size:
                            self.chunks.append({
                                "source": doc["filename"],
                                "content": " ".join(current_chunk)
                            })
                            # Keep overlap
                            current_chunk = current_chunk[-overlap:]
                            current_length = sum(len(w) + 1 for w in current_chunk)
                    
                    if current_chunk:
                        self.chunks.append({
                            "source": doc["filename"],
                            "content": " ".join(current_chunk)
                        })
                else:
                    if section.strip():
                        self.chunks.append({
                            "source": doc["filename"],
                            "content": section.strip()
                        })
    
    def _create_vector_store(self):
        """Create a simple vector store for retrieval."""
        try:
            import chromadb
            from chromadb.config import Settings
            
            # Create ChromaDB client
            self.chroma_client = chromadb.Client(Settings(
                anonymized_telemetry=False
            ))
            
            # Create or get collection
            self.collection = self.chroma_client.get_or_create_collection(
                name="team_knowledge",
                metadata={"hnsw:space": "cosine"}
            )
            
            # Add documents
            ids = [f"chunk_{i}" for i in range(len(self.chunks))]
            documents = [chunk["content"] for chunk in self.chunks]
            metadatas = [{"source": chunk["source"]} for chunk in self.chunks]
            
            self.collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
            
            self._safe_print("✅ Vector store created successfully!")
            
        except ImportError:
            self._safe_print("⚠️ ChromaDB not installed. Using simple search.")
            self.collection = None
        except Exception as e:
            self._safe_print(f"⚠️ Error creating vector store: {e}")
            self.collection = None
    
    def _retrieve_relevant_chunks(self, query: str, top_k: int = 3) -> List[dict]:
        """Retrieve relevant chunks for a query."""
        if self.collection:
            # Use ChromaDB for retrieval
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k
            )
            
            retrieved = []
            for i, doc in enumerate(results["documents"][0]):
                retrieved.append({
                    "content": doc,
                    "source": results["metadatas"][0][i]["source"]
                })
            return retrieved
        else:
            # Fallback: simple keyword matching
            query_words = set(query.lower().split())
            scored_chunks = []
            
            for chunk in self.chunks:
                chunk_words = set(chunk["content"].lower().split())
                score = len(query_words.intersection(chunk_words))
                scored_chunks.append((score, chunk))
            
            scored_chunks.sort(key=lambda x: x[0], reverse=True)
            return [chunk for _, chunk in scored_chunks[:top_k]]
    
    def query(self, user_query: str, context_prefix: str = "") -> str:
        """
        Process a user query using RAG.
        
        Args:
            user_query: The user's question
            context_prefix: Additional context about the mode
            
        Returns:
            Generated response
        """
        # Retrieve relevant chunks
        relevant_chunks = self._retrieve_relevant_chunks(user_query, top_k=3)
        
        # Build context from retrieved chunks
        context = "\n\n".join([
            f"[From {chunk['source']}]:\n{chunk['content']}"
            for chunk in relevant_chunks
        ])
        
        # Build prompt
        prompt = f"""You are TeamMind AI, a helpful assistant for team knowledge and onboarding.
{context_prefix}

Use the following context from team documentation to answer the question. If the answer is not in the context, say so but try to be helpful.

CONTEXT:
{context}

USER QUESTION: {user_query}

HELPFUL ANSWER:"""
        
        # Generate response
        if self.model:
            try:
                response = self.model.generate_text(prompt=prompt)
                return response.strip()
            except Exception as e:
                return f"Error generating response: {str(e)}"
        else:
            # Fallback response when model not available
            return self._fallback_response(user_query, relevant_chunks)
    
    def _fallback_response(self, query: str, chunks: List[dict]) -> str:
        """Generate a fallback response when model is not available."""
        if not chunks:
            return "I don't have specific information about that in my knowledge base. Please check with your team lead or the team wiki."
        
        response = "Based on our team documentation, here's what I found:\n\n"
        
        for chunk in chunks:
            # Extract a relevant snippet
            snippet = chunk["content"][:300]
            if len(chunk["content"]) > 300:
                snippet += "..."
            
            response += f"📄 **From {chunk['source']}**:\n{snippet}\n\n"
        
        response += "\n*Note: Running in fallback mode. Configure your IBM API key for full AI-powered responses.*"
        
        return response


# Test the RAG engine
if __name__ == "__main__":
    print("Testing RAG Engine...")
    
    try:
        engine = RAGEngine()
        engine.load_documents("knowledge-base")
        
        # Test query
        response = engine.query("How do I set up my development environment?")
        print("\n" + "="*50)
        print("Query: How do I set up my development environment?")
        print("="*50)
        print(response)
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. Created a .env file with your IBM API key")
        print("2. Installed requirements: pip install -r requirements.txt")
