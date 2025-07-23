import os
import streamlit as st
from utils import predict

# Get the absolute path of the directory where the script is located
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the page configuration and title
st.set_page_config(page_title="Cred Predictor", page_icon="💹", layout="wide")
st.title("💹 Cred Predictor")
st.caption("A dynamic tool for assessing creditworthiness with real-time risk analysis.")


# --- Sidebar ---
with st.sidebar:
    st.header("NovaCred")
    lauki_logo_path = os.path.join(_SCRIPT_DIR, "Cred_Predictor.jpg")
    st.image(lauki_logo_path, caption="Your Trusted Finance Partner")
    
    st.divider()
    
    st.header("Instructions")
    st.write("""
    1. Fill in the credit applicant's details across the tabs.
    2. Adjust sliders and dropdowns for interactive inputs.
    3. Click 'Calculate Risk' to view the assessment.
    """)

# --- Input Fields ---
st.subheader("🧮 Credit Applicant Snapshot")

tab1, tab2, tab3 = st.tabs(["👤 Personal Info", "🏦 Loan Details", "📜 Credit History"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=28, help="Enter borrower's age (18-100).")
    with col2:
        income = st.number_input("Annual Income", min_value=0, max_value=5000000, value=290875, step=50000, help="Borrower's annual income.")
    with col3:
        residence_type = st.selectbox("Residence Type", ['Owned', 'Rented', 'Mortgage'], help="Borrower's current residence type.")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input("Loan Amount", min_value=0, value=2560000, help="Total loan amount requested.")
        loan_purpose = st.selectbox("Loan Purpose", ['Education', 'Home', 'Auto', 'Personal'], help="Purpose of the loan.")
    with col2:
        loan_tenure_months = st.slider("Loan Tenure (Months)", min_value=6, max_value=240, step=6, value=36, help="Select the loan tenure in months.")
        loan_type = st.radio("Loan Type", ['Unsecured', 'Secured'], help="Choose the type of loan.", horizontal=True)

    lti = loan_amount / income if income > 0 else 0
    st.metric(label="Loan-to-Income Ratio (LTI)", value=f"{lti:.2f}", help="This shows the ratio of the loan amount to income.")

with tab3:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        avg_dpd_per_dm = st.number_input("Avg DPD", min_value=0, value=0, help="Average days past due, 0 if no loan history.")
    with col2:
        dmtlm = st.slider("DMTLM", min_value=0, max_value=100, value=0, help="Delinquent months to loan month ratio, 0 if no loans.")
    with col3:
        credit_utilization_ratio = st.slider("Credit Utilization (%)", min_value=0, max_value=100, value=0, help="Percentage of utilized credit, 0 if no credit.")
    with col4:
        total_loan_months = st.number_input("Total Loan Months", min_value=0, value=0, help="Cumulative loan tenure, 0 if no loans.")


# --- Action Button and Results ---
if st.button("Calculate Risk", type="primary"):
    probability, credit_score, rating = predict(
        age, avg_dpd_per_dm, credit_utilization_ratio, dmtlm, income,
        loan_amount, loan_tenure_months, total_loan_months,
        loan_purpose, loan_type, residence_type
    )

    st.divider()
    st.header("Risk Assessment Results")

    # --- Display Results ---
    res_col1, res_col2, res_col3 = st.columns(3)
    res_col1.metric(label="Default Probability", value=f"{probability:.2%}", help="The likelihood of the borrower defaulting on the loan.")
    res_col2.metric(label="Credit Score", value=credit_score, help="A score from 300-900 predicting creditworthiness.")
    res_col3.metric(label="Risk Rating", value=rating, help="A categorical rating based on the credit score.")

    if rating in ['Poor', 'Average']:
        st.warning(f"⚠ High-Risk Profile: The borrower's profile is rated as **{rating}**, suggesting a higher risk of default. Careful consideration is advised.", icon="⚠️")
    else:
        st.success(f"🌟 Low-Risk Profile: The borrower's profile is rated as **{rating}**. Loan approval is likely.", icon="✅")

    st.divider()

    # --- Expanders for additional context ---
    with st.expander("🔍 Understanding the Prediction"):
        st.write("The chart below shows the general importance of each feature in the model's decision-making process.")
        feature_importance_path = os.path.join(_SCRIPT_DIR, "..", "images", "Feature importance.png")
        st.image(feature_importance_path, caption="Model Feature Importance")

    with st.expander("📈 Model Performance"):
        st.write("The ROC curve illustrates the model's ability to distinguish between high-risk and low-risk applicants.")
        roc_curve_path = os.path.join(_SCRIPT_DIR, "..", "images", "ROC Curve.png")
        st.image(roc_curve_path, caption="Receiver Operating Characteristic (ROC) Curve")
