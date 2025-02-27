import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

# ✅ Set API key securely
GOOGLE_API_KEY = "AIzaSyAraCliOTkdG2NQcbfHTXNXsFNKPSB2qLM"  # 🔴 Replace with your actual API key
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY  # ✅ Store API key in environment

# ✅ Initialize LangChain's Google GenAI Model
llm = GoogleGenerativeAI(model="gemini-1.5-pro")

# ✅ Streamlit UI Configuration
st.set_page_config(page_title="AI Travel Planner", layout="wide")

# ✅ Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;  /* Light Background */
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .stTextInput>div>div>input {
            border: 2px solid #007bff !important;
            border-radius: 8px !important;
            padding: 8px !important;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stSpinner {
            color: #007bff !important;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ App Title
st.markdown("<h1 style='text-align: center; color: #007bff;'>🗺️ AI Travel Planner</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px; color: #555;'>Plan your journey with AI-powered recommendations.</p>", unsafe_allow_html=True)

# ✅ Centered Input Fields
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    source = st.text_input("Enter Source Location 🏙️")
    destination = st.text_input("Enter Destination 🏁")

# ✅ Define Prompt with LangChain
prompt_template = PromptTemplate(
    input_variables=["source", "destination"],
    template="""
    You are an AI travel planner. Suggest the best travel options between {source} and {destination}.
    Consider options like flights, trains, buses, and taxis with estimated costs.
    Provide a well-structured response.
    """
)

def get_travel_options(source, destination):
    """Fetch travel options using LangChain's Google GenAI."""
    try:
        prompt = prompt_template.format(source=source, destination=destination)
        response = llm(prompt)
        return response if response else "No travel data available."
    except Exception as e:
        return f"Error fetching travel options: {str(e)}"

# ✅ Button to Generate Travel Options
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    if st.button("🚀 Find Travel Options"):
        if source and destination:
            with st.spinner("🔍 Searching for best routes..."):
                response = get_travel_options(source, destination)
                st.success("✅ Travel recommendations fetched!")
                st.write(response)
        else:
            st.warning("⚠️ Please enter both source and destination.")

# GOOGLE_API_KEY = "AIzaSyAraCliOTkdG2NQcbfHTXNXsFNKPSB2qLM" 