import streamlit as st
import random

# Categories and innovative components to mix for unique app ideas
categories = {
    "Tech": ["AI-driven", "Blockchain-secured", "Decentralized", "Quantum-powered", "Automated"],
    "Health & Wellness": ["Personalized health tracking", "Mental wellness AI", "Smart habit-forming", "Biofeedback-based", "Holistic self-improvement"],
    "Education": ["AI-powered tutoring", "Gamified learning", "Adaptive knowledge retention", "Augmented reality education", "Neuroscience-backed training"],
    "Finance": ["Predictive financial AI", "Crypto investment automation", "Smart expense reduction", "AI-driven risk assessment", "Personalized wealth growth"],
    "Entertainment": ["AI-generated dynamic storytelling", "Interactive virtual experiences", "Personalized content creation", "AI-driven music composition", "Augmented reality gaming"],
    "Sustainability": ["AI-powered eco-lifestyle assistant", "Smart carbon footprint tracker", "Blockchain for sustainable shopping", "Decentralized green investments", "Automated waste reduction"],
    "Smart Cities": ["AI-optimized traffic control", "Decentralized energy grid management", "Community-driven improvement suggestions", "Real-time public infrastructure monitoring", "Autonomous smart mobility"],
    "Business & Productivity": ["AI-driven workflow automation", "Smart time management", "Predictive task prioritization", "Sentiment-based client engagement", "Real-time meeting summarization"]
}

problem_statements = [
    "solves an unmet market need by integrating", 
    "optimizes user experience through", 
    "disrupts the industry with", 
    "creates a new revenue model using", 
    "enhances productivity via", 
    "revolutionizes personal habits by leveraging"
]

# Function to generate a unique and innovative app idea
def generate_idea(category):
    tech = random.choice(categories[category])
    problem = random.choice(problem_statements)
    unique_twist = random.choice(categories[category])
    return f"{tech} app that {problem} {unique_twist}."

# Streamlit UI
st.title("🚀 AI-Generated Innovative App Ideas")

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
