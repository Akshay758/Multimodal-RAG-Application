# 🤖 Multimodal PDF RAG Q&A System

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about processed PDF documents and receive context-grounded answers using an LLM.

The project combines semantic search, vector embeddings, document retrieval, and LLM generation through an interactive Streamlit interface.

---

## 🚀 Demo

🔗 **Live Demo:** YOUR_STREAMLIT_LINK_HERE

---

## 📌 Overview

This project demonstrates how a PDF-based question-answering system can be built using Retrieval-Augmented Generation (RAG).

Instead of sending the entire PDF directly to the LLM, the system:

1. Processes the PDF
2. Extracts retrievable content
3. Splits the document into smaller retrievable units
4. Converts content into vector embeddings
5. Stores embeddings in ChromaDB
6. Retrieves relevant content based on the user's question
7. Builds a context-aware prompt
8. Sends the retrieved context to an LLM
9. Generates a context-based answer
10. Displays the answer through a Streamlit interface

---

## ✨ Features

- 📄 PDF-based question answering
- 🔎 Semantic search
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤗 Hugging Face embeddings
- 🗄️ ChromaDB vector database
- ⚡ Groq LLM inference
- 🔗 LangChain integration
- 💬 Interactive Streamlit chat interface
- 🖼️ Multimodal PDF content handling
- 📝 Multiple question-and-answer interactions
- 🔐 Environment variable based API key configuration
- 📚 Context-aware document retrieval

---

## 🛠️ Tech Stack

### Programming Language

- Python

### AI / Generative AI

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Generative AI

### Frameworks

- LangChain
- Streamlit

### Embeddings

- Hugging Face
- Sentence Transformers
- `sentence-transformers/all-MiniLM-L6-v2`

### Vector Database

- ChromaDB

### LLM Inference

- Groq

### Environment Management

- Python-dotenv

---

# 🏗️ Architecture

```text
                ┌─────────────────┐
                │   PDF Document  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Document        │
                │ Processing      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Content         │
                │ Extraction      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Hugging Face    │
                │ Embeddings      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   ChromaDB      │
                │ Vector Store    │
                └────────┬────────┘
                         │
                    User Question
                         │
                         ▼
                ┌─────────────────┐
                │ Semantic        │
                │ Retrieval       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Retrieved       │
                │ Context         │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Prompt          │
                │ Construction    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Groq LLM        │
                │ Generation      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Streamlit UI    │
                │ Final Answer    │
                └─────────────────┘

RAG Workflow

The complete Retrieval-Augmented Generation pipeline works as follows:

PDF
 │
 ▼
Document Processing
 │
 ▼
Content Extraction
 │
 ▼
Chunking
 │
 ▼
Embedding Generation
 │
 ▼
ChromaDB
 │
 │
 └──────────────┐
                │
         User Question
                │
                ▼
       Question Embedding
                │
                ▼
       Similarity Search
                │
                ▼
       Relevant Context
                │
                ▼
       Prompt Construction
                │
                ▼
           Groq LLM
                │
                ▼
        Generated Answer
                │
                ▼
          Streamlit UI
🧠 How It Works
1. PDF Processing

The PDF document is processed to extract useful content.

The processing stage can handle different types of document content such as:

Text
Tables
Images

The extracted content is prepared so that it can be used during retrieval.

2. Content Extraction

The extracted document content is organized into retrievable units.

Each unit can contain information such as:

Content
Content type
Metadata
Document identifier
Page information

This information helps the retrieval system locate relevant content.

Multimodal Workflow

The project is designed around PDF content that can include different types of information.

                    PDF
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
        Text       Tables      Images
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
              Document Processing
                     │
                     ▼
               Content Storage
                     │
                     ▼
                 Retrieval
                     │
                     ▼
                    LLM
                     │
                     ▼
                   Answer

Requirements

The project uses libraries such as:

streamlit
langchain
langchain-core
langchain-groq
langchain-chroma
langchain-huggingface
chromadb
sentence-transformers
python-dotenv

Install all dependencies using:

pip install -r requirements.txt
