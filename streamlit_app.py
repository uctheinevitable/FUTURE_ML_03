import streamlit as st
from dialogflow_utils import detect_intent_texts
import uuid
import time

# ──────────────────────────────────────────────────
# APP CONFIG
# ──────────────────────────────────────────────────
st.set_page_config(page_title="SupportPro Bot",
                   page_icon="🤖",
                   layout="wide",
                   initial_sidebar_state="collapsed")

# ──────────────────────────────────────────────────
# STYLE SHEET
# ──────────────────────────────────────────────────
st.markdown("""
    <style>
        /* --- General Page --- */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #f0f2f5;
        }
        #MainMenu, footer {visibility: hidden;}

        /* --- Main Chat Panel --- */
        .chat-container {
            max-width: 800px;
            margin: 2rem auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            display: flex;
            flex-direction: column;
            height: 85vh;
        }

        /* --- Chat Header --- */
        .chat-header {
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #e5e5e5;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .chat-header h3 {
            margin: 0;
            font-size: 1.5rem;
            color: #1c1e21;
        }
        .chat-header .status {
            color: #34c759;
            font-weight: 500;
        }

        /* --- Message Area --- */
        .message-area {
            flex-grow: 1;
            padding: 1.5rem;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }

        /* --- Welcome/Initial View --- */
        .welcome-view {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: #65676b;
            height: 100%;
        }
        .welcome-view .icon {
            font-size: 4rem;
            margin-bottom: 1rem;
        }

        /* --- Quick Actions (Initial View) --- */
        .quick-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            justify-content: center;
            margin-top: 2rem;
        }
        .quick-actions .stButton button {
            background-color: #e7f3ff;
            color: #0084ff;
            border: 1px solid #e7f3ff;
            border-radius: 18px;
            font-weight: 500;
            transition: all 0.2s ease;
        }
        .quick-actions .stButton button:hover {
            background-color: #d0e7ff;
            border-color: #0084ff;
            color: #0084ff;
        }

        /* --- Message Bubbles --- */
        .msg-row {
            display: flex;
            margin-bottom: 1rem;
            animation: fadeIn 0.3s ease-out;
        }
        .msg-row.user {
            justify-content: flex-end;
        }
        .msg-row.bot {
            justify-content: flex-start;
        }
        .bubble {
            max-width: 70%;
            padding: 0.8rem 1.2rem;
            border-radius: 18px;
            line-height: 1.5;
            font-size: 1rem;
        }
        .user .bubble {
            background-color: #0084ff;
            color: white;
            border-bottom-right-radius: 4px;
        }
        .bot .bubble {
            background-color: #e4e6eb;
            color: #1c1e21;
            border-bottom-left-radius: 4px;
        }
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 1.2rem;
            margin: 0 0.75rem;
        }
        .user .avatar { display: none; } /* Hide user avatar for a cleaner look */
        .bot .avatar {
            background-color: #0084ff;
            color: white;
        }


        /* --- Input Bar --- */
        .input-area {
            padding: 1rem 1.5rem;
            border-top: 1px solid #e5e5e5;
            background: #ffffff;
            border-radius: 0 0 12px 12px;
        }

        /* --- Animation --- */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* --- Mobile Responsive --- */
        @media (max-width: 768px) {
            .chat-container {
                margin: 0;
                border-radius: 0;
                height: 100vh;
            }
        }
    </style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────
# STATE & FUNCTIONS
# ──────────────────────────────────────────────────
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def handle_input():
    user_msg = st.session_state.user_input_field
    if user_msg:
        # Append user message
        st.session_state.chat_history.append(("user", user_msg))
        
        # Get bot response
        reply = detect_intent_texts(user_msg, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("bot", reply))
        
        # Clear input field
        st.session_state.user_input_field = ""

def handle_quick_action(option):
    st.session_state.chat_history.append(("user", option))
    reply = detect_intent_texts(option, session_id=st.session_state.session_id)
    st.session_state.chat_history.append(("bot", reply))


# ──────────────────────────────────────────────────
# UI LAYOUT
# ──────────────────────────────────────────────────
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <div class='chat-header'>
        <h3>🤖 SupportPro Bot</h3>
        <span class='status'>● Online</span>
    </div>
""", unsafe_allow_html=True)

# --- Message Area ---
st.markdown("<div class='message-area'>", unsafe_allow_html=True)

if not st.session_state.chat_history:
    # --- Welcome View ---
    st.markdown("""
        <div class='welcome-view'>
            <div class='icon'>💬</div>
            <h2>How can I help you today?</h2>
            <p>Select an option below or type your question.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # --- Quick Actions ---
    MENU_OPTIONS = [
        "Track my order", "Return an item", "Shipping info",
        "Payment methods", "Contact support", "Product availability"
    ]
    st.markdown("<div class='quick-actions'>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, option in enumerate(MENU_OPTIONS):
        with cols[i % 3]:
            if st.button(option, key=f"quick_{option}", on_click=handle_quick_action, args=[option], use_container_width=True):
                pass
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- Chat History ---
    for role, message in st.session_state.chat_history:
        avatar_char = "🤖" if role == "bot" else "U"
        if role == "bot":
            st.markdown(f"""
                <div class='msg-row bot'>
                    <div class='avatar'>{avatar_char}</div>
                    <div class='bubble'>{message}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
             st.markdown(f"""
                <div class='msg-row user'>
                    <div class='bubble'>{message}</div>
                </div>
            """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # Close message-area

# --- Input Bar ---
st.markdown("<div class='input-area'>", unsafe_allow_html=True)
st.text_input(
    "Type your message...",
    key="user_input_field",
    on_change=handle_input,
    label_visibility="collapsed",
    placeholder="Type your message and press Enter..."
)
st.markdown("</div>", unsafe_allow_html=True) # Close input-area

st.markdown("</div>", unsafe_allow_html=True) # Close chat-container
