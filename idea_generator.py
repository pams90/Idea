import streamlit as st
import random

# Categories and dynamic components based on provided app ideas
categories = {
    "Health & Wellness": [
        "AI-driven burnout detection & recovery planner",
        "Personalized mental health journaling assistant",
        "Real-time stress & anxiety tracker",
        "AI-powered sleep optimizer",
        "Smart hydration and nutrition tracker"
    ],
    "Productivity & Organization": [
        "AI-powered time management assistant",
        "Smart task prioritization tool",
        "Automated workflow bottleneck detector",
        "Personalized productivity coach",
        "AI-driven focus enhancement app"
    ],
    "Finance & Wealth": [
        "AI-driven budget optimizer",
        "Personalized wealth growth assistant",
        "Automated tax-saving strategy generator",
        "Real-time credit score improvement coach",
        "Financial planning AI"
    ],
    "Education & Learning": [
        "AI-powered interactive tutoring assistant",
        "Gamified learning platform",
        "Personalized knowledge retention trainer",
        "Real-time skill gap analyzer",
        "AI-driven study optimizer"
    ],
    "Entertainment & Creativity": [
        "AI-generated dynamic storytelling platform",
        "Personalized AR/VR experience generator",
        "Interactive AI-driven content creator",
        "Music composition AI",
        "Adaptive interactive gaming platform"
    ],
    "Sustainability & Smart Living": [
        "AI-powered personal carbon footprint tracker",
        "Smart home energy efficiency optimizer",
        "Blockchain-based ethical shopping assistant",
        "Automated waste tracking tool",
        "Smart AI assistant for sustainable lifestyle planning"
    ],
    "Smart Cities & Mobility": [
        "AI-powered public transport efficiency tracker",
        "Autonomous smart parking system",
        "Community-driven urban improvement platform",
        "AI-enhanced pedestrian safety assistant",
        "Smart city waste monitoring AI"
    ],
    "Security & Privacy": [
        "Real-time personal safety assistant",
        "AI-driven cyber threat detection tool",
        "Blockchain-based identity management system",
        "Universal AI-powered fraud detection assistant",
        "Smart home security optimizer"
    ]
}

# Function to generate a unique app idea
def generate_idea(category):
    return random.choice(categories[category])

# Streamlit UI
st.title("🚀 High-Value, Innovative & Non-Existing App Idea Generator")

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
