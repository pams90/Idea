import streamlit as st
import random

# Categories and dynamic components based on provided app ideas
categories = {
    "Health & Wellness": [
        "AI-driven burnout detection & recovery planner",
        "Personalized mental health journaling assistant",
        "Real-time stress & anxiety tracker with AI suggestions",
        "AI-powered sleep optimizer that adapts based on biometrics",
        "Smart hydration and nutrition tracker with wearable integration"
    ],
    "Productivity & Organization": [
        "AI-powered time management assistant",
        "Smart task prioritization tool based on urgency & importance",
        "Automated workflow bottleneck detector",
        "Personalized productivity coach with habit tracking",
        "AI-driven focus enhancement app with real-time distractions analysis"
    ],
    "Finance & Wealth": [
        "AI-driven budget optimizer and smart spending insights",
        "Personalized wealth growth assistant with AI investment suggestions",
        "Automated tax-saving strategy generator",
        "Real-time credit score improvement coach",
        "Financial planning AI that adapts to user life changes"
    ],
    "Education & Learning": [
        "AI-powered interactive tutoring assistant",
        "Gamified learning platform with AI-generated challenges",
        "Personalized knowledge retention trainer",
        "Real-time skill gap analyzer with curated learning paths",
        "AI-driven neuroscience-backed study optimizer"
    ],
    "Entertainment & Creativity": [
        "AI-generated dynamic storytelling platform",
        "Personalized AR/VR immersive experience generator",
        "Interactive AI-driven content creator assistant",
        "Music composition AI based on user mood and creativity",
        "Adaptive interactive gaming platform with AI-generated levels"
    ],
    "Sustainability & Smart Living": [
        "AI-powered personal carbon footprint tracker",
        "Smart home energy efficiency optimizer",
        "Blockchain-based ethical shopping assistant",
        "Automated waste tracking and recycling optimizer",
        "Smart AI assistant for sustainable lifestyle planning"
    ],
    "Smart Cities & Mobility": [
        "AI-powered real-time public transport efficiency tracker",
        "Autonomous smart parking optimization system",
        "Community-driven urban improvement feedback platform",
        "AI-enhanced pedestrian safety navigation assistant",
        "Smart city waste and pollution monitoring AI"
    ],
    "Security & Privacy": [
        "Real-time personal safety assistant with smart alerts",
        "AI-driven cyber threat detection and privacy protection tool",
        "Blockchain-based decentralized identity management system",
        "Universal AI-powered fraud detection assistant",
        "Smart home security optimizer with AI behavior tracking"
    ]
}

problem_statements = [
    "solves an unmet market need by introducing",
    "optimizes user experience through",
    "disrupts the industry by leveraging",
    "creates a new revenue model using",
    "enhances productivity via",
    "revolutionizes daily habits through",
    "automates complex decision-making by integrating"
]

# Function to generate a unique and innovative app idea
def generate_idea(category):
    feature = random.choice(categories[category])
    problem = random.choice(problem_statements)
    unique_twist = random.choice(categories[category])
    return f"{feature} app that {problem} {unique_twist}."

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
