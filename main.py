import streamlit as st
from modules import health, finance, study

# ---- Streamlit Setup ----
st.set_page_config(page_title="SmartLife App", layout="wide")

# ---- Custom CSS Styling for Classy Look ----
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Inter:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #f5f3ef;
            color: #2e2e2e;
        }

        .welcome {
            font-family: 'Playfair Display', serif;
            font-size: 3em;
            font-weight: 600;
            text-align: center;
            color: #3a3a3a;
            padding: 20px 0;
            border-bottom: 2px solid #e0ddd7;
        }

        .block-container {
            padding-top: 2rem;
        }

        .stSidebar {
            background-color: #fbf9f5;
            border-right: 1px solid #e8e6e2;
        }

        .stSelectbox > div {
            background-color: #fffaf6;
            border-radius: 12px;
            padding: 10px;
            border: 1px solid #d8d4ce;
        }

        .stButton button {
            background-color: #a67c52;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-weight: 600;
            transition: 0.3s ease;
        }

        .stButton button:hover {
            background-color: #8b6e45;
        }

        .signature {
            text-align: center;
            font-size: 0.9rem;
            color: #888;
            margin-top: 3rem;
            padding-bottom: 2rem;
        }

        #MainMenu, header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---- Welcome Section ----
st.markdown('<div class="welcome">✨ SmartLife – Your Elegant Life Assistant</div>', unsafe_allow_html=True)

# ---- Sidebar Navigation ----
menu = st.sidebar.selectbox("📂 Choose a Section", [
    "🏥 SmartHealth",
    "💰 Personal Finance Tracker",
    "🤖 AI Study Assistant"
])

# ---- Section Routing ----
if menu == "🏥 SmartHealth":
    health.get_health_ui()

elif menu == "💰 Personal Finance Tracker":
     finance.show_finance_ui(st)

elif menu == "🤖 AI Study Assistant":
    study.show_study_ui(st)

# ---- Signature ----
st.markdown('<div class="signature">Crafted by Muqaddas Fatima © 2025</div>', unsafe_allow_html=True)
