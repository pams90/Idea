import streamlit as st
import random

# Expanded idea categories and keywords with more innovative and unique concepts
categories = {
    "Tech": ["AI-powered emotion recognition", "Decentralized identity verification", "Quantum computing simulation"],
    "Health & Wellness": ["AI-driven mental health assistant", "Personalized microbiome analysis", "Virtual reality therapy"],
    "Education": ["AI-generated personalized curriculum", "Blockchain-based credential verification", "Neuroscience-backed learning methods"],
    "Finance": ["Predictive AI for smart investing", "Automated tax optimization", "Crowdsourced economic forecasting"],
    "Entertainment": ["AI-driven script writing assistant", "Interactive holographic concerts", "Personalized AR storytelling"],
    "Sustainability": ["AI-powered waste sorting", "Blockchain for ethical supply chains", "Personalized carbon footprint tracker"],
    "Smart Cities": ["AI-powered traffic optimization", "Blockchain-based energy trading", "Autonomous waste collection"],
    "Space & Exploration": ["AI for asteroid mining", "Crowdsourced exoplanet discovery", "VR-based space training simulator"]
}

# Function to generate a truly unique and innovative app idea
def generate_idea(category):
    keyword = random.choice(categories[category])
    return f"{keyword} {category} Application"

# Streamlit UI
st.title("🚀 Idea Generator for Innovative & Non-Existing Applications")

# User selects a category
selected_category = st.selectbox("Choose a category:", list(categories.keys()))

# Button to generate a new idea
if st.button("Generate Idea"):
    idea = generate_idea(selected_category)
    st.session_state["current_idea"] = idea
    st.success(f"💡 {idea}")

# Display saved ideas
if "saved_ideas" not in st.session_state:
    st.session_state["saved_ideas"] = []

# Save button
if "current_idea" in st.session_state and st.button("Save Idea"):
    st.session_state["saved_ideas"].append(st.session_state["current_idea"])
    st.success("Idea saved!")

# Show saved ideas
if st.session_state["saved_ideas"]:
    st.subheader("📌 Saved Ideas")
    for idea in st.session_state["saved_ideas"]:
        st.write(f"- {idea}")

# Clear saved ideas
if st.button("Clear Saved Ideas"):
    st.session_state["saved_ideas"] = []
    st.success("Saved ideas cleared!")
