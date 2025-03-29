

import streamlit as st
import random


# Title & Introduction
st.title("🚀 Growth Mindset Challenge")
st.subheader("Adopt a growth mindset and unlock your full potential!")

st.write(
    """
    A **Growth Mindset** is the belief that abilities can be developed through hard work, 
    perseverance, and learning from mistakes. Let's explore how you can develop a growth mindset!
    """
)

# Growth Mindset Benefits
st.header("🌱 Why Adopt a Growth Mindset?")
st.write("""
- **Embrace Challenges** - Turn obstacles into learning opportunities.
- **Learn from Mistakes** - See errors as a path to improvement.
- **Persist Through Difficulties** - Keep going even when it's tough.
- **Celebrate Effort** - Focus on progress, not just results.
- **Stay Open-Minded** - Adapt and grow with new knowledge.
""")

# Interactive Growth Mindset Quiz
st.header("🧠 Growth Mindset Quiz")
st.write("Test yourself! How much do you believe in growth?")

questions = {
    "Do you believe intelligence can improve with effort?": ["Yes", "No"],
    "Do you see challenges as opportunities?": ["Yes", "No"],
    "Do you learn from failure?": ["Yes", "No"],
    "Do you seek feedback to improve?": ["Yes", "No"],
}

score = 0
for q, options in questions.items():
    answer = st.radio(q, options)
    if answer == "Yes":
        score += 1

# Show results
st.write(f"**Your Growth Mindset Score:** {score}/{len(questions)}")

if score == len(questions):
    st.success("🎉 You have a strong growth mindset! Keep learning and growing!")
elif score >= len(questions) // 2:
    st.info("👍 You have a good mindset, but there's room to improve!")
else:
    st.warning("🔄 Growth is a journey! Keep working on your mindset!")

# Motivational Quote Generator
st.header("💡 Daily Motivation")
if st.button("Get a Growth Mindset Quote"):
    quotes = [
        "Failure is not the opposite of success; it’s part of success.",
        "Your brain is like a muscle. The more you use it, the stronger it gets.",
        "Every mistake you make is progress.",
        "Challenges are what make life interesting.",
        "Success is the sum of small efforts repeated daily.",
    ]
    st.write(f"**💬 {random.choice(quotes)}**")

# Footer
st.write("---")
st.write("🌟 Developed with ❤️ by [mariam faizan]")

