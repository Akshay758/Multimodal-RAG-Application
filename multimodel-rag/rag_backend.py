import os
from dotenv import load_dotenv

from unstructured.partition.pdf import partition_pdf

from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ============================================================
# 1. ENV
# ============================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )


# ============================================================
# 2. PDF PATH
# ============================================================

PDF_PATH = os.path.join(
    "content",
    "attention.pdf"
)

if not os.path.exists(PDF_PATH):
    raise FileNotFoundError(
        f"PDF not found: {PDF_PATH}"
    )


# ============================================================
# 3. GROQ MODEL
# ============================================================

model = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-20b",
    temperature=0,
    reasoning_effort="low"
)


# ============================================================
# 4. EXTRACT TEXT FROM PDF
# ============================================================

elements = partition_pdf(
    filename=PDF_PATH,
    strategy="fast",
    chunking_strategy="by_title",
    max_characters=10000,
    combine_text_under_n_chars=2000,
    new_after_n_chars=6000
)

# ============================================================
# 5. CONVERT PDF ELEMENTS TO LANGCHAIN DOCUMENTS
# ============================================================

documents = []

for element in elements:

    text = str(element).strip()

    if text:

        documents.append(
            Document(
                page_content=text
            )
        )


if not documents:
    raise ValueError(
        "No text could be extracted from the PDF."
    )


# ============================================================
# 6. EMBEDDINGS
# ============================================================

embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================================
# 7. CHROMA VECTORSTORE
# ============================================================

vectorstore = Chroma(
    collection_name="transformer_rag_v2",
    embedding_function=embedding_function,
    persist_directory="./chroma_db_v2"
)


# ============================================================
# 8. ADD PDF TEXT TO CHROMA
# ============================================================

existing_count = vectorstore._collection.count()

if existing_count == 0:

    vectorstore.add_documents(
        documents
    )


# ============================================================
# 9. RETRIEVER
# ============================================================

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 8
    }
)


# ============================================================
# 10. BUILD PROMPT
# ============================================================

prompt = ChatPromptTemplate.from_template(
    """
Answer the question using only the provided PDF context.

Question:
{question}

Context:
{context}

Give a short answer focused specifically on the Transformer
encoder-decoder architecture.

Include:
- Encoder: N=6 layers, multi-head self-attention,
  feed-forward network, residual connections and layer normalization.
- Decoder: N=6 layers, the additional multi-head attention
  sub-layer over the encoder output, and autoregressive generation.

Do not include positional encoding, embeddings, softmax,
training time, GPUs, or other unrelated details unless the
question specifically asks for them.
"""
)


# ============================================================
# 11. ANSWER FUNCTION
# ============================================================

def generate_answer(question):

    docs = retriever.invoke(
        question
    )


    if not docs:

        return (
            "The information was not found in the PDF."
        )


    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )


    response = (
        prompt
        | model
        | StrOutputParser()
    ).invoke(
        {
            "context": context,
            "question": question
        }
    )


    return response


# ============================================================
# 12. CHAIN
# ============================================================

class RAGChain:

    def invoke(self, question):

        return {
            "response":
                generate_answer(question)
        }


chain_with_sources = RAGChain()





