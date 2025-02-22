import streamlit as st
import random

# Categories and dynamic components based on provided app ideas
categories = {
    "Health & Wellness": [
        ("AI-driven burnout detection & recovery planner", "An app that monitors stress levels and suggests recovery strategies."),
        ("Personalized mental health journaling assistant", "A smart journaling app that provides AI-driven emotional insights."),
        ("Real-time stress & anxiety tracker", "An AI-powered tool that tracks stress levels and offers coping mechanisms."),
        ("AI-powered sleep optimizer", "A sleep tracking app that adapts recommendations based on biometric data."),
        ("Smart hydration and nutrition tracker", "An app that ensures optimal hydration and nutrition through AI analysis.")
    ],
    "Productivity & Organization": [
        ("AI-powered time management assistant", "An intelligent scheduler that optimizes task management and deadlines."),
        ("Smart task prioritization tool", "An app that ranks tasks based on urgency, impact, and deadlines."),
        ("Automated workflow bottleneck detector", "A tool that identifies inefficiencies in workflows and suggests optimizations."),
        ("Personalized productivity coach", "A habit-building app that tailors strategies to improve productivity."),
        ("AI-driven focus enhancement app", "An app that minimizes distractions and optimizes deep work sessions.")
    ],
    "Finance & Wealth": [
        ("AI-driven budget optimizer", "A tool that analyzes spending and suggests the best saving strategies."),
        ("Personalized wealth growth assistant", "An AI advisor that customizes financial plans to maximize investments."),
        ("Automated tax-saving strategy generator", "A tax optimization app that finds legal ways to reduce taxable income."),
        ("Real-time credit score improvement coach", "An AI tool that helps users understand and boost their credit scores."),
        ("Financial planning AI", "A smart financial advisor that dynamically adjusts plans based on life changes.")
    ],
    "Education & Learning": [
        ("AI-powered interactive tutoring assistant", "A virtual tutor that adapts to students’ learning styles and progress."),
        ("Gamified learning platform", "An educational platform that makes learning fun through challenges and rewards."),
        ("Personalized knowledge retention trainer", "An AI tool that improves memory retention through adaptive learning."),
        ("Real-time skill gap analyzer", "An app that identifies weaknesses and suggests targeted learning resources."),
        ("AI-driven study optimizer", "A tool that schedules study sessions for maximum efficiency and recall.")
    ]
}

# Function to generate multiple unique app ideas with descriptions
def generate_ideas(category, num_ideas=5):
    return random.sample(categories[category], min(num_ideas, len(categories[category])))

# Streamlit UI
st.title("🚀 High-Value, Innovative & Non-Existing App Idea Generator")

# User selects a category
selected_category = st.selectbox("Choose a category:", list(categories.keys()))

# Button to generate multiple ideas
if st.button("Generate 5 Ideas"):
    ideas = generate_ideas(selected_category)
    st.session_state["current_ideas"] = ideas
    for idea, description in ideas:
        st.success(f"💡 {idea}")
        st.write(f"📌 Description: {description}")

# Display saved ideas
if "saved_ideas" not in st.session_state:
    st.session_state["saved_ideas"] = []

# Save button
if "current_ideas" in st.session_state and st.button("Save Ideas"):
    st.session_state["saved_ideas"].extend(st.session_state["current_ideas"])
    st.success("Ideas saved!")

# Show saved ideas
if st.session_state["saved_ideas"]:
    st.subheader("📌 Saved Ideas")
    for idea, description in st.session_state["saved_ideas"]:
        st.write(f"- **{idea}**: {description}")

# Clear saved ideas
if st.button("Clear Saved Ideas"):
    st.session_state["saved_ideas"] = []
    st.success("Saved ideas cleared!")
