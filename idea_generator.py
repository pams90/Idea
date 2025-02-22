import streamlit as st
import random

# Sample idea categories and keywords
categories = {
    "Tech": ["AI-powered", "Blockchain-based", "IoT-enabled"],
    "Health & Wellness": ["Mindfulness app", "Personalized fitness", "Sleep tracker"],
    "Education": ["Gamified learning", "AI tutor", "Skill-sharing platform"],
    "Finance": ["Automated budgeting", "Crypto investment tool", "AI stock predictor"],
    "Entertainment": ["Interactive storytelling", "VR experiences", "AI-generated content"]
}

# Function to generate a random idea
def generate_idea():
    category = random.choice(list(categories.keys()))
    keyword = random.choice(categories[category])
    return f"{keyword} {category} Application"

# Streamlit UI
st.title("🚀 Idea Generator for Innovative Applications")

# Button to generate a new idea
if st.button("Generate Idea"):
    idea = generate_idea()
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
