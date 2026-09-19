# 🤖 Multimodal PDF RAG Q&A System

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about processed PDF documents and receive context-grounded answers using an LLM.

The project combines semantic search, vector embeddings, document retrieval, and LLM generation through an interactive Streamlit interface.

---

## 🚀 Demo

🔗 **Live Demo:** YOUR_STREAMLIT_LINK_HERE

---

## 📌 Overview

This project demonstrates how a PDF-based question-answering system can be built using RAG.

Instead of sending the entire PDF directly to the LLM, the system:

1. Processes the PDF
2. Splits the document into retrievable content
3. Converts content into vector embeddings
4. Stores embeddings in ChromaDB
5. Retrieves relevant content based on the user's question
6. Sends the retrieved context to an LLM
7. Generates a context-based answer
8. Displays the answer through a Streamlit interface

---

## 🏗️ Architecture

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
                │ Groq LLM        │
                │ Generation      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Streamlit UI    │
                │ Final Answer    │
                └─────────────────┘
