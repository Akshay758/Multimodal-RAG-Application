# 🤖 Multimodal PDF RAG Q&A System

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about processed PDF documents and receive context-grounded answers using a Large Language Model (LLM).

The project combines semantic search, vector embeddings, document retrieval, ChromaDB, Hugging Face embeddings, LangChain, Groq, and Streamlit to build an interactive PDF question-answering system.

---

## 🚀 Demo

🔗 **Live Demo:** YOUR_STREAMLIT_LINK_HERE

---

## 📌 Overview

This project demonstrates how a PDF-based question-answering system can be built using Retrieval-Augmented Generation (RAG).

Instead of sending the entire PDF directly to the LLM, the system processes the document, creates searchable representations, retrieves relevant information for a user's question, and then provides the retrieved information to the LLM as context.

The overall process is:

1. Process the PDF
2. Extract document content
3. Organize content into retrievable units
4. Generate vector embeddings
5. Store embeddings in ChromaDB
6. Receive a user question
7. Perform semantic similarity search
8. Retrieve relevant document content
9. Build a context-aware prompt
10. Send the context and question to the LLM
11. Generate the final answer
12. Display the answer through Streamlit

---

# ✨ Features

- 📄 PDF-based question answering
- 🔎 Semantic search
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤗 Hugging Face embeddings
- 🗄️ ChromaDB vector database
- ⚡ Groq LLM inference
- 🔗 LangChain integration
- 💬 Interactive Streamlit chat interface
- 🖼️ Multimodal PDF content handling
- 📊 Text and table retrieval
- 🖼️ Image-aware retrieval workflow
- 📝 Multiple question-and-answer interactions
- 📚 Context-aware document retrieval
- 🔐 Environment variable based API key configuration
- 💾 Persistent vector database and document store

---

# 🛠️ Tech Stack

## Programming Language

- Python

## AI / Generative AI

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Generative AI
- Semantic Search

## Frameworks

- LangChain
- Streamlit

## Embeddings

- Hugging Face
- Sentence Transformers
- `sentence-transformers/all-MiniLM-L6-v2`

## Vector Database

- ChromaDB

## LLM Inference

- Groq

## Environment Management

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

