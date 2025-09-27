import streamlit as st
from src.chatbot import get_chatbot_response
from src.utils import load_rules

# ------------------ Page config ------------------
st.set_page_config(page_title="Interview Preparation Chatbot",
                   page_icon="💼",
                   layout="wide")

# ---------- Custom CSS for shiny blue sidebar ----------
st.markdown(
    """
    <style>
    /* Sidebar background gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
    }
    /* Sidebar text color */
    [data-testid="stSidebar"] * {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Load rules ------------------
rules = load_rules("data/interview_rules.json")

# ------------------ Session State ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("💬 Chat History")
    if st.session_state.messages:
        for i, msg in enumerate(st.session_state.messages, 1):
            role = "You" if msg["role"] == "user" else "Bot"
            st.markdown(f"**{i}. {role}:** {msg['content']}")
    else:
        st.markdown("*No messages yet*")

# ------------------ Main Title ------------------
st.markdown("<h1 style='text-align: center;'>💼 Interview Preparation Chatbot</h1>",
            unsafe_allow_html=True)
st.markdown("---")

# ------------------ Chat Input ------------------
prompt = st.chat_input("Ask me about interview tips, questions, or preparation...")
if prompt:
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Bot response
    response = get_chatbot_response(prompt, rules)
    st.session_state.messages.append({"role": "assistant", "content": response})

# ------------------ Chat Display (center) ------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="
                display:inline-block;
                background-color:#DCF8C6;
                padding:10px 15px;
                border-radius:15px 15px 0 15px;
                max-width:60%;
                text-align:right;
                word-wrap:break-word;
                margin:5px 0;
            ">{msg['content']}</div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                display:inline-block;
                background-color:#F1F0F0;
                padding:10px 15px;
                border-radius:15px 15px 15px 0;
                max-width:60%;
                text-align:left;
                word-wrap:break-word;
                margin:5px 0;
            ">{msg['content'].replace(chr(10),'<br>')}</div>
            """,
            unsafe_allow_html=True
        )