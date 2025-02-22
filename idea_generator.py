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
    ],
    "Entertainment & Creativity": [
        ("AI-generated dynamic storytelling platform", "An interactive storytelling app that creates AI-driven plots in real-time."),
        ("Personalized AR/VR experience generator", "A tool that builds customized AR/VR environments based on user input."),
        ("Interactive AI-driven content creator", "An AI assistant that helps users create videos, images, and text content."),
        ("Music composition AI", "An app that generates unique music compositions based on user preferences."),
        ("Adaptive interactive gaming platform", "A game engine that changes levels dynamically based on player behavior.")
    ],
    "Sustainability & Smart Living": [
        ("AI-powered personal carbon footprint tracker", "An app that monitors daily habits and suggests ways to reduce carbon impact."),
        ("Smart home energy efficiency optimizer", "A tool that optimizes home energy usage for cost and environmental savings."),
        ("Blockchain-based ethical shopping assistant", "An app that verifies product origins to ensure ethical and sustainable choices."),
        ("Automated waste tracking tool", "An AI-powered app that tracks waste production and suggests reduction strategies."),
        ("Smart AI assistant for sustainable lifestyle planning", "A planner that helps users live more sustainably through AI-driven advice.")
    ],
    "Smart Cities & Mobility": [
        ("AI-powered public transport efficiency tracker", "An app that monitors and suggests improvements for public transport."),
        ("Autonomous smart parking system", "A tool that finds and reserves parking spots in real-time using AI."),
        ("Community-driven urban improvement platform", "A city development app that allows users to propose and vote on changes."),
        ("AI-enhanced pedestrian safety assistant", "A real-time pedestrian navigation system that enhances safety measures."),
        ("Smart city waste monitoring AI", "A system that optimizes waste collection through AI-powered predictions.")
    ],
    "Security & Privacy": [
        ("Real-time personal safety assistant", "An app that detects danger and alerts emergency contacts instantly."),
        ("AI-driven cyber threat detection tool", "A cybersecurity assistant that detects and prevents online threats."),
        ("Blockchain-based identity management system", "A secure identity management system using blockchain for authentication."),
        ("Universal AI-powered fraud detection assistant", "An AI-driven tool that identifies fraudulent activity across multiple platforms."),
        ("Smart home security optimizer", "An app that adapts home security settings based on user habits and threats.")
    ]
}

# Function to generate a unique app idea with description
def generate_idea(category):
    idea, description = random.choice(categories[category])
    return idea, description

# Streamlit UI
st.title("🚀 High-Value, Innovative & Non-Existing App Idea Generator")

# User selects a category
selected_category = st.selectbox("Choose a category:", list(categories.keys()))

# Button to generate a new idea
if st.button("Generate Idea"):
    idea, description = generate_idea(selected_category)
    st.session_state["current_idea"] = (idea, description)
    st.success(f"💡 {idea}")
    st.write(f"📌 Description: {description}")

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
    for idea, description in st.session_state["saved_ideas"]:
        st.write(f"- **{idea}**: {description}")

# Clear saved ideas
if st.button("Clear Saved Ideas"):
    st.session_state["saved_ideas"] = []
    st.success("Saved ideas cleared!")
