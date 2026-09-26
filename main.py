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

st.title("🌍 Welcome to my Travel Assistant!!")

# 1. CSS Styles adding the custom orbit keyframe loop
st.markdown(
    """
    <style>
    /* Card design layout */
    .travel-card {
        background: linear-gradient(135deg, #092027 0%, #153c44 50%, #20535d 100%);
        padding: 40px 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    
    /* Dedicated relative container for the animating icons */
    .animation-container {
        position: relative;
        width: 100px;
        height: 100px;
        margin: 0 auto 20px auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Fixed centerpiece globe */
    .static-globe {
        font-size: 3rem;
        z-index: 1;
    }

    /* Floating airplane orbit wrapper */
    .orbiting-plane-wrapper {
        position: absolute;
        width: 100%;
        height: 100%;
        z-index: 2;
        animation: spin-orbit 6s linear infinite; /* Adjust '6s' to speed up or slow down */
    }

    /* The individual plane position offset inside the spinning wrapper */
    .moving-plane {
        position: absolute;
        top: 0px;
        left: 50%;
        transform: translateX(-50%) rotate(45deg); /* Flips the nose to face the flight angle */
        font-size: 1.8rem;
    }

    /* Core keyframe to rotate the airplane container seamlessly */
    @keyframes spin-orbit {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
    
    /* Layout text stylings */
    .travel-title {
        color: #d1ff84 !important;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .travel-desc {
        color: #a0b2b6;
        font-size: 1.05rem;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto 25px auto;
        line-height: 1.5;
    }

    div.stButton {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.08) !important;
        color: #c9d1d9 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 30px !important;
        padding: 8px 24px !important;
        font-size: 0.85rem !important;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.15) !important;
        border-color: rgba(255, 255, 255, 0.3) !important;
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Updated HTML Card with Nested Animation Nodes
st.markdown(
    """
    <div class="travel-card">
        <!-- Floating Elements Box -->
        <div class="animation-container">
            <div class="static-globe">🌍</div>
            <div class="orbiting-plane-wrapper">
                <div class="moving-plane">🛫</div>
            </div>
        </div>
        
        <div class="travel-title">AI Travel Assistant</div>
        <div class="travel-desc">
            Your intelligent companion for seamless journeys, itineraries, and local secrets.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 3. Interactive badge button
if st.button("🚀 Ready for takeoff? • Let's explore the world!", key="takeoff_badge"):
    st.balloons()


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