import streamlit as st
from youtube_utils import extract_video_id_from_url, get_transcript_text
from openai_utils import get_quiz_data
from quiz_utils import string_to_list, get_randomized_options

st.set_page_config(
    page_title="quizz YouTube Videos with AI",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<div style='background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); padding: 2rem 1rem; border-radius: 12px; margin-bottom: 2rem;'>
    <h1 style='color: #fff; margin-bottom: 0;'>QuizTube <span style='font-size:1.5rem;'>AI</span> 🧩</h1>
    <p style='color: #e0e0e0; font-size:1.1rem;'>Test your understanding of any YouTube video with AI-generated quizzes!</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("👨‍💻 About the Creator")
    st.write("""
    <b>Richie</b> is a passionate learner who is starting his journey to learn AI. This project is a demonstration of AI-powered learning tools.
    """, unsafe_allow_html=True)
    st.divider()
    st.subheader("🔗 Connect")
    st.markdown(
        """
        - [GitHub](https://github.com/idn-programmer)
        - [Youtube](https://www.youtube.com/channel/UCDfIZZ57EZKuFlEn1ikOO-g)
        """
    )
    st.divider()
    st.write("Made with ❤️ using Streamlit and OpenAI")

st.markdown("""
Paste a YouTube video link below. The video must have English captions. The app will generate a quiz based on the video content!
""")

with st.form("user_input"):
    YOUTUBE_URL = st.text_input("YouTube Video URL", value="", placeholder="Enter YouTube video URL here")
    submitted = st.form_submit_button("Generate Quiz")

API_KEY = "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"

if submitted or ('quiz_data_list' in st.session_state):
    if not YOUTUBE_URL:
        st.info("Please provide a valid YouTube video link.")
        st.stop()
    with st.spinner("Generating your quiz..."):
        if submitted:
            video_id = extract_video_id_from_url(YOUTUBE_URL)
            video_transcription = get_transcript_text(video_id)
            quiz_data_str = get_quiz_data(video_transcription, API_KEY)
            st.session_state.quiz_data_list = string_to_list(quiz_data_str)
            if 'user_answers' not in st.session_state:
                st.session_state.user_answers = [None for _ in st.session_state.quiz_data_list]
            if 'correct_answers' not in st.session_state:
                st.session_state.correct_answers = []
            if 'randomized_options' not in st.session_state:
                st.session_state.randomized_options = []
            for q in st.session_state.quiz_data_list:
                options, correct_answer = get_randomized_options(q[1:])
                st.session_state.randomized_options.append(options)
                st.session_state.correct_answers.append(correct_answer)
        with st.form(key='quiz_form'):
            st.subheader("🧠 Quiz Time!")
            for i, q in enumerate(st.session_state.quiz_data_list):
                options = st.session_state.randomized_options[i]
                default_index = st.session_state.user_answers[i] if st.session_state.user_answers[i] is not None else 0
                response = st.radio(q[0], options, index=default_index)
                user_choice_index = options.index(response)
                st.session_state.user_answers[i] = user_choice_index
            results_submitted = st.form_submit_button(label='Show My Score')
            if results_submitted:
                score = sum([
                    ua == st.session_state.randomized_options[i].index(ca)
                    for i, (ua, ca) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers))
                ])
                st.success(f"Your score: {score}/{len(st.session_state.quiz_data_list)}")
                if score == len(st.session_state.quiz_data_list):
                    st.balloons()
                else:
                    incorrect_count = len(st.session_state.quiz_data_list) - score
                    st.warning(f"You got {incorrect_count} question(s) wrong. Review below:")
                for i, (ua, ca, q, ro) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers, st.session_state.quiz_data_list, st.session_state.randomized_options)):
                    with st.expander(f"Question {i + 1}", expanded=False):
                        if ro[ua] != ca:
                            st.info(f"Question: {q[0]}")
                            st.error(f"Your answer: {ro[ua]}")
                            st.success(f"Correct answer: {ca}")
