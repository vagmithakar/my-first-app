import streamlit as st 
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()

st.set_page_config(
    page_title="My Cool App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.set_page_config(page_title="AI Travel Assistant", page_icon="🌍", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117;
    }
    .header-row {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 0 20px 0;
    }
    .header-row .globe {
        font-size: 28px;
    }
    .header-row .title {
        color: white;
        font-size: 28px;
        font-weight: 700;
    }
    .header-row .link-icon {
        color: #8b949e;
        font-size: 18px;
        margin-left: 4px;
    }
    .hero-card {
        background: linear-gradient(135deg, #17423f 0%, #0f2b2c 100%);
        border-radius: 16px;
        padding: 70px 20px;
        text-align: center;
    }
    .orbit-wrap {
        position: relative;
        width: 130px;
        height: 130px;
        margin: 0 auto 20px auto;
    }
    .globe-icon {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 48px;
    }
    .orbit {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        animation: spin 5s linear infinite;
    }
    .plane-icon {
        position: absolute;
        top: -6px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 26px;
        animation: counter-spin 5s linear infinite;
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes counter-spin {
        from { transform: translateX(-50%) rotate(0deg); }
        to { transform: translateX(-50%) rotate(-360deg); }
    }
    .hero-title {
        color: #b7f26a;
        font-size: 40px;
        font-weight: 800;
        margin-bottom: 15px;
    }
    .hero-subtitle {
        color: #9fb3ae;
        font-size: 18px;
        margin-bottom: 35px;
    }
    div.stButton {
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.05);
        color: #e6edf3;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 30px;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: 500;
        margin: 0 auto;
        display: block;
    }
    div.stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.3);
        color: #e6edf3;
    }
    </style>

    <div class="header-row">
        <span class="globe">🌍</span>
        <span class="title">Welcome to my Travel Assistant</span>
        <span class="link-icon">🔗</span>
    </div>

    <div class="hero-card">
        <div class="orbit-wrap">
            <div class="globe-icon">🌍</div>
            <div class="orbit"><div class="plane-icon">✈️</div></div>
        </div>
        <div class="hero-title">AI Travel Assistant</div>
        <div class="hero-subtitle">Your intelligent companion for seamless journeys, itineraries, and local secrets.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Centered button, placed to visually sit inside the hero card
st.markdown("<div style='margin-top:-55px;'></div>", unsafe_allow_html=True)

# Use columns as a bullet-proof centering fallback (works across all
# Streamlit versions, regardless of internal CSS class/testid names).
left, center, right = st.columns([1, 2, 1])
with center:
    if st.button("🚀 Ready for takeoff?  •  Let's explore the world!", use_container_width=True):
        st.balloons()
        st.toast("Let's plan your trip! ✈️")

location = st.text_input(label=r"$\textsf{\Large Where do you wish to go this time?}$")
days_nr = st.number_input(label=r"$\textsf{\Large How many days of trip are you planning?}$", min_value=1, max_value=30)
criterias = st.multiselect(
    label=r"$\textsf{\Large What would you like to experience throughout your trip?}$",
    options=["Adventure", "Spirituality", "Nature's Bliss", "Fun", "Pilgrimage"],
    default=None
)
budget = st.selectbox(r"$\textsf{\Large What is your travel budget?}$", ["Luxury", "Moderate", "Budgeted"])
travel_type = st.radio(r"$\textsf{\Large Who are you travelling with?}$", ["Family", "Solo", "Friends"])

prompt = f"""You are a Travel Planner, User is saying he/she wants to 
go to {location} and for {days_nr} days , they want to experience {criterias} criterias , they are on a budget of type {budget}
Travel Type is :  {travel_type}
Plan a tripo and share answer in bullet format"""

if st.button("Plan Trip"):
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)

    st.success("Voila !! Here are some fab suggestions")
    st.write(interaction.output_text)