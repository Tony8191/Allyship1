import streamlit as st
import matplotlib.pyplot as plt

# Questions for the quiz
questions = {
    "listener": [
        "I feel comfortable sitting in silence while others express their thoughts.",
        "I focus on understanding others' perspectives rather than offering solutions.",
    ],
    "advocate": [
        "I challenge unfair practices or behavior, even if it's uncomfortable.",
        "I actively support systemic change in my workplace or community.",
    ],
    "educator": [
        "I enjoy explaining ideas or concepts to help others learn.",
        "I actively seek out opportunities to raise awareness about inclusion.",
    ],
    "amplifier": [
        "I ensure that everyone's voice is heard in group settings.",
        "I give credit to colleagues for their ideas and contributions.",
    ],
    "confidant": [
        "People often trust me with personal or sensitive information.",
        "I provide a safe space for others to share their experiences."
    ]
}

def generate_chart(scores):
    archetypes = list(scores.keys())
    values = list(scores.values())
    
    plt.figure(figsize=(8, 6))
    plt.bar(archetypes, values, color='skyblue')
    plt.title("Allyship Archetype Scores")
    plt.xlabel("Archetype")
    plt.ylabel("Score")
    st.pyplot(plt)

# Streamlit App
st.title("Allyship Archetype Quiz")
st.write("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")

if "scores" not in st.session_state:
    st.session_state.scores = {archetype: 0 for archetype in questions.keys()}

for archetype, archetype_questions in questions.items():
    st.header(f"{archetype.capitalize()} Archetype")
    for i, question in enumerate(archetype_questions):
        score = st.slider(question, 1, 5, 3, key=f"{archetype}_{i}")
        st.session_state.scores[archetype] += score

if st.button("Submit"):
    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_scores[0]
    secondary = sorted_scores[1]
    
    st.write(f"**Primary Archetype:** {primary[0].capitalize()} (Score: {primary[1]})")
    st.write(f"**Secondary Archetype:** {secondary[0].capitalize()} (Score: {secondary[1]})")
    
    generate_chart(st.session_state.scores)
