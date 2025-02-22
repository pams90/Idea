import streamlit as st
import random

# Categories and unique, high-value, non-existing app ideas that can be programmed
categories = {
    "Tech": ["AI-driven code optimization tool", "Smart bug detection with real-time fixes", "Automated UI/UX improvement AI"],
    "Health & Wellness": ["AI-powered burnout detection & recovery planner", "Personalized mental health journaling assistant", "Smart hydration and nutrition tracker"],
    "Education": ["AI-driven interactive learning modules", "Real-time AI tutor for coding challenges", "Personalized memory enhancement training"],
    "Finance": ["AI-driven budget optimization assistant", "Predictive tax-saving insights tool", "Automated investment strategy generator"],
    "Entertainment": ["AI-generated dynamic storytelling app", "Personalized movie/series script creator", "Interactive AR-based novel experience"],
    "Sustainability": ["Smart home energy waste tracker", "AI-powered personal carbon footprint optimizer", "Automated ethical shopping assistant"],
    "Smart Cities": ["AI-based public transport efficiency tracker", "Real-time smart parking space optimizer", "Community-driven local improvement app"],
    "Business & Productivity": ["Automated meeting note summarizer with action items", "AI-based client sentiment analysis tool", "Real-time workflow bottleneck identifier"]
}

# Function to generate a unique and innovative app idea that satisfies high-value needs
def generate_idea(category):
    keyword = random.choice(categories[category])
    return f"{keyword} ({category} Application)"

# Streamlit UI
st.title("🚀 High-Value Innovative App Idea Generator")

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
