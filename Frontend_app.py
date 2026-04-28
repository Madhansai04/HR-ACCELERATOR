import streamlit as st
from backend.llm_structure import read_docx, get_structured_data
from backend.llm_evaluator import evaluate_summary, generate_quiz, evaluate_answers

st.set_page_config(page_title="AI Training", layout="wide")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    file_path = "data/Retail_Domain_Knowledge_Guide.docx"
    text = read_docx(file_path)
    return get_structured_data(text)

subsections = load_data()

# -----------------------------
# SAFETY
# -----------------------------
if not subsections:
    st.error("❌ No content available")
    st.stop()

if "index" not in st.session_state:
    st.session_state.index = 0

if st.session_state.index >= len(subsections):
    st.session_state.index = 0

current = subsections[st.session_state.index]

# -----------------------------
# UI
# -----------------------------
st.title("🛍 AI Training Platform")
st.caption(f"Section {st.session_state.index+1}/{len(subsections)}")

st.markdown(f"### {current['title']}")
st.write(current["content"])
st.info(f"💡 {current['example']}")
st.caption(f"⏱ {current['time']}")

st.divider()

# -----------------------------
# SUMMARY
# -----------------------------
summary = st.text_area("✍️ Write your understanding")

if st.button("Evaluate Summary"):
    if summary.strip():
        result = evaluate_summary(summary)
        st.success(result)
    else:
        st.warning("Write something first")

st.divider()

# -----------------------------
# QUIZ
# -----------------------------
if st.button("Generate Quiz"):
    quiz = generate_quiz(current["content"])
    st.info(quiz)

answers = st.text_area("🧠 Your answers")

if st.button("Submit Answers"):
    if answers.strip():
        result = evaluate_answers(answers)
        st.success(result)
    else:
        st.warning("Write answers first")

st.divider()

# -----------------------------
# NAVIGATION
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Previous"):
        if st.session_state.index > 0:
            st.session_state.index -= 1

with col2:
    if st.button("Next ➡"):
        if st.session_state.index < len(subsections) - 1:
            st.session_state.index += 1
        else:
            st.success("🎉 Course Completed!")