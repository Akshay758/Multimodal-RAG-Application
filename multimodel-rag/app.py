import streamlit as st

from rag_backend import chain_with_sources


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Multimodal RAG",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS - DARK AI INTERFACE (NO SIDEBAR)
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       GLOBAL
       ========================= */

    html, body {
        background: #05070c !important;
    }

    .stApp {
        background: #05070c !important;
        color: #f5f7fb;
    }


    .block-container {
        padding-top: 2rem;
        padding-bottom: 9rem;
        max-width: 1100px;
    }


    /* =========================
       HIDE STREAMLIT DEFAULT UI
       ========================= */

    /* Hide sidebar completely */
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    /* Hide the sidebar collapse/expand arrow */
    div[data-testid="collapsedControl"] {
        display: none !important;
    }

    /* Top header bar (the white "Deploy" toolbar area) */
    header[data-testid="stHeader"] {
        background: #05070c !important;
        border-bottom: 1px solid #1f2937;
    }

    /* Toolbar icons/menu inside header, keep them visible on dark bg */
    header[data-testid="stHeader"] * {
        color: #f5f7fb !important;
    }

    /* Footer / bottom whitespace area */
    footer {
        background: #05070c !important;
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    /* Bottom app container padding area (below chat input) */
    div[data-testid="stBottomBlockContainer"] {
        background: #05070c !important;
    }

    div[data-testid="stBottom"] {
        background: #05070c !important;
    }


    /* =========================
       HEADER TITLE
       ========================= */

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        color: #ffffff;
        margin-top: 10px;
        margin-bottom: 4px;
    }


    .gradient-text {
        background: linear-gradient(
            90deg,
            #8b5cf6,
            #6366f1,
            #22d3ee
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .subtitle {
        text-align: center;
        color: #8b95a7;
        font-size: 15px;
        margin-bottom: 35px;
    }


    /* =========================
       QUESTION
       ========================= */

    .question-box {
        background: linear-gradient(
            135deg,
            rgba(79, 70, 229, 0.20),
            rgba(99, 102, 241, 0.08)
        );

        border: 1px solid rgba(99, 102, 241, 0.35);

        padding: 15px 20px;
        border-radius: 16px;

        margin-top: 25px;
        margin-bottom: 12px;

        color: #e5e7eb;
        font-weight: 600;

        box-shadow:
            0 8px 30px rgba(0, 0, 0, 0.20);
    }


    /* =========================
       ANSWER
       ========================= */

    .answer-label {
        color: #a78bfa;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;

        margin-top: 10px;
        margin-bottom: 8px;
    }


    .answer-box {
        background: rgba(15, 23, 42, 0.75);

        border: 1px solid #263244;

        padding: 20px;

        border-radius: 16px;

        margin-bottom: 25px;

        color: #dbe2ea;

        line-height: 1.7;

        box-shadow:
            0 10px 35px rgba(0, 0, 0, 0.20);

        max-height: 420px;
        overflow-y: auto;
    }


    /* =========================
       DIVIDER
       ========================= */

    hr {
        border-color: #1f2937 !important;
    }


    /* =========================
       CHAT INPUT — FULL FIX
       ========================= */

    /* Outer fixed bottom strip that Streamlit renders behind the input.
       This was showing as a white/pink frame around the box. */
    div[data-testid="stBottom"],
    div[data-testid="stBottom"] > div,
    div[data-testid="stBottomBlockContainer"] {
        background: #05070c !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Give the whole bottom strip breathing room from the screen edge */
    div[data-testid="stBottomBlockContainer"] {
        padding: 24px 0 34px 0 !important;
        max-width: 1100px;
        margin: 0 auto;
    }

    /* The chat input's own wrapper (this had the leftover white edge) */
    div[data-testid="stChatInput"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        border-radius: 16px !important;
    }

    div[data-testid="stChatInput"] > div {
        background: #111827 !important;
        border: 1px solid #374151 !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
    }

    div[data-testid="stChatInput"] textarea {
        background: #111827 !important;
        color: #ffffff !important;

        border: none !important;

        border-radius: 16px !important;

        padding: 14px !important;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: #6b7280 !important;
    }

    /* Focus state — clean single-color ring, no red/white flash */
    div[data-testid="stChatInput"]:focus-within > div {
        border: 1px solid #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.35) !important;
    }

    /* Send button */
    div[data-testid="stChatInput"] button {
        background: #1f2937 !important;
        border-radius: 12px !important;
    }


    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        width: 100%;

        background: #111827;

        color: #e5e7eb;

        border: 1px solid #374151;

        border-radius: 10px;

        transition: 0.2s;
    }


    .stButton > button:hover {
        background: #1f2937;

        border-color: #6366f1;

        color: #ffffff;
    }


    /* =========================
       SCROLLBAR
       ========================= */

    ::-webkit-scrollbar {
        width: 7px;
    }


    ::-webkit-scrollbar-track {
        background: #05070c;
    }


    ::-webkit-scrollbar-thumb {
        background: #374151;
        border-radius: 10px;
    }


    ::-webkit-scrollbar-thumb:hover {
        background: #4b5563;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
    <div class="main-title">
        🤖 <span class="gradient-text">Multimodal RAG</span>
    </div>

    <div class="subtitle">
        Ask intelligent questions about your processed documents
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# ============================================================
# CLEAR CHAT BUTTON (moved from sidebar into main area)
# ============================================================

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for chat in st.session_state.chat_history:

    question = chat["question"]

    answer = chat["answer"]


    # --------------------------------------------------------
    # USER QUESTION
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="question-box">
            👤 &nbsp; {question}
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # AI ANSWER
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="answer-label">
            ✨ AI RESPONSE
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="answer-box">
            {answer}
        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask anything about your PDF..."
)


# ============================================================
# PROCESS NEW QUESTION
# ============================================================

if question:

    with st.spinner(
        "🔍 Retrieving context and generating answer..."
    ):

        response = chain_with_sources.invoke(
            question
        )


    answer = response["response"]


    # --------------------------------------------------------
    # SAVE CHAT
    # --------------------------------------------------------

    st.session_state.chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )


    # --------------------------------------------------------
    # REFRESH
    # --------------------------------------------------------

    st.rerun()