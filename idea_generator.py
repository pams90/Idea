import streamlit as st
import random
import requests
import time

# Bing Search API Key (Replace with your own if needed)
BING_API_KEY = "your_bing_api_key"
BING_SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"

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
    ]
}

def check_uniqueness(idea):
    """Searches the internet to check if the app idea already exists."""
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": idea, "count": 5}
    response = requests.get(BING_SEARCH_URL, headers=headers, params=params)
    if response.status_code == 200:
        results = response.json().get("webPages", {}).get("value", [])
        return len(results) == 0  # If no search results, idea is likely unique
    return True  # Assume unique if search fails

def generate_unique_idea(category):
    """Generates an app idea and verifies its uniqueness on the web."""
    attempts = 0
    while attempts < 5:
        idea, description = random.choice(categories[category])
        if check_uniqueness(idea):
            return idea, description
        attempts += 1
        time.sleep(1)  # Prevent excessive API calls
    return "No unique ideas found, try again!", "Try another category or reattempt search."

# Streamlit UI
st.title("🚀 AI-Generated Non-Existing App Ideas")

# User selects a category
selected_category = st.selectbox("Choose a category:", list(categories.keys()))

# Button to generate a new idea
if st.button("Generate Idea"):
    idea, description = generate_unique_idea(selected_category)
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
