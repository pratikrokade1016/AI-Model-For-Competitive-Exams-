# UPSC-project

# AI-Powered Chatbot using RAG Pipeline

## Overview
This project is an AI-powered chatbot that leverages the **Retrieval-Augmented Generation (RAG) pipeline** to provide accurate and context-aware responses. The backend is implemented in **Python** using **LangChain**, **FAISS** for vector storage, and **Ollama (Llama 2)** for generating responses. The frontend is built using **HTML, CSS, and JavaScript** to provide a dynamic and interactive chat interface.

## Project Architecture
1. **Frontend**: Built using **HTML, CSS, and JavaScript** to create a user-friendly chat interface.
2. **Backend**:
   - **PDF Processing**: Loads and processes documents using `PyPDFLoader`.
   - **Text Splitting**: Splits documents into smaller chunks using `RecursiveCharacterTextSplitter`.
   - **Vector Storage**: Converts text into embeddings and stores them in **FAISS**.
   - **Retriever**: Searches for relevant document chunks based on user queries.
   - **LLM Integration**: Uses **Llama 2 (via Ollama)** to generate responses.
   - **Retrieval Chain**: Combines retrieval and generation for precise answers.

## Technologies Used
- **Python** (Backend)
  - LangChain
  - FAISS (Vector Database)
  - Ollama (Llama 2 Model)
  - HuggingFace Embeddings
- **Frontend**
  - HTML, CSS (UI Styling)
  - JavaScript (Dynamic Chat Interaction)
  - Fetch API (Connecting to Backend)

## How It Works
1. **Upload and Process Documents**
   - The system loads a PDF (e.g., "Indian Polity by M. Laxmikanth").
   - The document is split into manageable chunks for better retrieval.
   
2. **Convert Text into Vector Format**
   - Each chunk is converted into embeddings using **HuggingFace Embeddings**.
   - The vectors are stored in **FAISS** for fast retrieval.
   
3. **Retrieval & Response Generation**
   - When a user asks a question, the **retriever** finds the most relevant document chunks.
   - The selected text is sent to **Llama 2**, which generates an answer based on the retrieved context.

4. **User Interaction**
   - The frontend displays chat responses dynamically.
   - Users can type questions and receive instant AI-generated responses.

## Setup Instructions
### Prerequisites
- Python 3.8+
- Node.js (for frontend, optional)
- Required Python Libraries:
  ```bash
  pip install langchain langchain-community faiss-cpu ollama
  ```

### Running the Backend
```bash
python app.py  # Run Flask or FastAPI server
```

### Running the Frontend
Open `index.html` in a browser or host it on a simple HTTP server.

## Future Enhancements
- Improve UI with animations and voice interactions.
- Expand support for more document types (e.g., Word, TXT).
- Optimize retrieval for better accuracy.

## Conclusion
This AI chatbot efficiently retrieves and generates responses using the **RAG pipeline**, combining **FAISS** for vector storage and **Llama 2** for natural language processing. It can be adapted to various domains requiring document-based Q&A solutions.

