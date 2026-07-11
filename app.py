import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("data/student_dropout_model.pkl")

st.markdown("""
<style>

/* Main background */
.stApp{
    background-color:#F4F8FB;
}

/* Main container */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Buttons */
div[data-testid="stButton"] > button{
    width:100%;
    background:linear-gradient(90deg,#4F46E5,#06B6D4);
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    padding:12px;
}

div[data-testid="stButton"] > button:hover{
    background:linear-gradient(90deg,#4338CA,#0891B2);
}

/* Select boxes */
div[data-baseweb="select"]{
    border-radius:10px;
}

/* Slider */
div[data-testid="stSlider"]{
    padding-top:10px;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="EduShield AI",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<div style="
background:linear-gradient(90deg,#4F46E5,#2563EB,#06B6D4);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
margin-bottom:20px;
">

<h1>🎓 EduShield AI</h1>

<h3>Student Dropout Risk Prediction System</h3>

<p>
Predict students who may be at risk of dropping out using Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🎓 EduShield AI")

    st.success("Machine Learning Project")

    st.write("---")

    st.subheader("📋 Project Details")

    st.write("**Dataset:** 101 Students")

    st.write("**Features:** 13")

    st.write("**Algorithm:** Random Forest")

    st.write("**Language:** Python")

    st.write("**Framework:** Streamlit")

    st.write("---")

    st.info(
        "Predict students who may require academic support based on educational and personal factors."
    )

st.write("")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📊 Dataset", "101")

c2.metric("📑 Features", "13")

c3.metric("🤖 Model", "Random Forest")

c4.metric("📈 Test Accuracy", "100%")
st.caption("Model accuracy on the testing dataset.")

st.divider()


with st.container(border=True):

    st.subheader("📝 Student Details")

    col1, col2 = st.columns(2)


# Mapping dictionaries
age_options = {
    "Below 15": 1,
    "15 - 17": 2,
    "18 - 20": 3,
    "Above 20": 4
}

education_options = {
    "High School": 1,
    "Intermediate": 2,
    "Diploma": 3,
    "Undergraduate": 4,
    "Postgraduate": 5
}

attendance_options = {
    "Below 50%": 1,
    "50 - 74%": 2,
    "75 - 90%": 3,
    "Above 90%": 4
}

percentage_options = {
    "Below 60%": 1,
    "60 - 74%": 2,
    "75 - 89%": 3,
    "Above 90%": 4
}

study_hours_options = {
    "Less than 1 hour": 1,
    "1–2 hours": 2,
    "3–4 hours": 3,
    "More than 4 hours": 4
}

failed_subject_options = {
    "No": 0,
    "Yes": 1
}

financial_options = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Often": 4,
    "Always": 5
}

distance_options = {
    "No Response": 0,
    "Less than 2 km": 1,
    "2–5 km": 2,
    "5–10 km": 3,
    "More than 10 km": 4
}

internet_options = {
    "No": 0,
    "Sometimes": 1,
    "Yes": 2
}

social_media_options = {
    "Less than 1 hour": 1,
    "1–2 hours": 2,
    "3–4 hours": 3,
    "More than 4 hours": 4
}

missed_classes_options = {
    "No": 0,
    "Yes": 1
}

break_thought_options = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Often": 4
}

col1, col2 = st.columns(2)

with col1:

    age = st.selectbox("👤 Age", list(age_options.keys()))
    age = age_options[age]

    attendance = st.selectbox("📅 Attendance", list(attendance_options.keys()))
    attendance = attendance_options[attendance]

    study_hours = st.selectbox("📚 Study Hours", list(study_hours_options.keys()))
    study_hours = study_hours_options[study_hours]

    course_interest = st.slider("Course Interest", 1, 5)

    distance = st.selectbox("Distance", list(distance_options.keys()))
    distance = distance_options[distance]

    missed_classes = st.selectbox("Missed Classes", list(missed_classes_options.keys()))
    missed_classes = missed_classes_options[missed_classes]

with col2:

    education = st.selectbox("🎓 Education", list(education_options.keys()))
    education = education_options[education]

    percentage = st.selectbox("Percentage", list(percentage_options.keys()))
    percentage = percentage_options[percentage]

    failed_subject = st.selectbox("Failed Subject", list(failed_subject_options.keys()))
    failed_subject = failed_subject_options[failed_subject]

    financial_difficulty = st.selectbox(
        "Financial Difficulty",
        list(financial_options.keys())
    )
    financial_difficulty = financial_options[financial_difficulty]

    internet_access = st.selectbox("🌐 Internet Access", list(internet_options.keys()))
    
    internet_access = internet_options[internet_access]

    social_media = st.selectbox(
        "Social Media Hours",
        list(social_media_options.keys())
    )
    social_media = social_media_options[social_media]

    break_thought = st.selectbox(
        "Thought About Taking a Break",
        list(break_thought_options.keys())
    )
    break_thought = break_thought_options[break_thought]


if st.button("🔍 Predict Dropout Risk", use_container_width=True):

    input_data = pd.DataFrame([[

        age,
        education,
        attendance,
        percentage,
        study_hours,
        failed_subject,
        course_interest,
        financial_difficulty,
        distance,
        internet_access,
        social_media,
        missed_classes,
        break_thought

    ]], columns=[
        "Age",
        "Education",
        "Attendance",
        "Percentage",
        "StudyHours",
        "FailedSubject",
        "CourseInterest",
        "FinancialDifficulty",
        "Distance",
        "InternetAccess",
        "SocialMediaHours",
        "MissedClasses",
        "BreakThought"
    ])

    prediction = model.predict(input_data)

    st.divider()

    if prediction[0] == 1:
        st.snow()
        st.markdown("""
<div style="
background:#FEE2E2;
padding:20px;
border-radius:15px;
border-left:8px solid red;
">
<h2>🔴 High Dropout Risk</h2>
<p>The student may require additional academic support.</p>
</div>
""", unsafe_allow_html=True)

        st.warning("""
### Recommendations

✅ Improve class attendance.

✅ Follow a daily study schedule.

✅ Reduce excessive social media usage.

✅ Meet an academic mentor.

✅ Seek financial or counseling support if needed.
""")

    else:
        st.balloons()

        st.markdown("""
<div style="
background:#DCFCE7;
padding:20px;
border-radius:15px;
border-left:8px solid green;
">
<h2>🟢 Low Dropout Risk</h2>
<p>The student is currently at low risk of dropping out.</p>
</div>
""", unsafe_allow_html=True)

        st.info("""
### Great Job!

Keep maintaining:

✅ Good attendance

✅ Regular study habits

✅ Positive interest in your course

✅ Healthy balance between study and social media
""")

st.divider()

st.caption("EduShield AI | Student Dropout Prediction using Machine Learning")