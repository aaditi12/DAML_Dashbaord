import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv(r"C:\Users\AADITI\Downloads\archive (3)\College_Admission.csv")  # change name if needed

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Student Admission Dashboard", layout="wide")

# -------------------------------
# Title & Description
# -------------------------------
st.title("🎓 Student Admission Prediction Dashboard")
st.markdown(
    "This dashboard provides insights into student admission probability, "
    "performance, and scholarship eligibility using interactive filters."
)

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("Filter Options")

preferred_stream = st.sidebar.selectbox(
    "Select Preferred Stream",
    df['preferred_stream'].unique()
)

gender = st.sidebar.selectbox(
    "Select Gender",
    df['gender'].unique()
)

# Filtered Data
filtered_df = df[
    (df['preferred_stream'] == preferred_stream) &
    (df['gender'] == gender)
]

# -------------------------------
# KPI Metrics
# -------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Admission Probability",
    round(filtered_df['admission_probability'].mean(), 2)
)



col2.metric(
    "Total Students",
    filtered_df.shape[0]
)

# -------------------------------
# Charts Section
# -------------------------------
st.subheader("📈 Visual Analysis")

# Admission Probability by State
st.markdown("### Average Admission Probability by State")
st.bar_chart(
    filtered_df.groupby('state')['admission_probability'].mean()
)

# Admission Status Distribution
st.markdown("### Admission Status Distribution")
st.bar_chart(
    filtered_df['admission_status'].value_counts()
)



# Scholarship Eligibility Analysis
st.markdown("### Scholarship Eligibility Count")
st.bar_chart(
    filtered_df['scholarship_eligibility'].value_counts()
)

# -------------------------------
# Data Preview
# -------------------------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head(10))
