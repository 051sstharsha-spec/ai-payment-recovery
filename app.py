
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("payment_recovery_model.pkl")

# Page settings
st.set_page_config(
    page_title="AI Revenue Recovery",
    page_icon="💳",
    layout="centered"
)

st.title("💳 AI Revenue Recovery")
st.write(
    "Predict the probability of recovering a failed payment "
    "and get an recommended recovery action."
)

st.divider()

# User inputs
amount_inr = st.number_input(
    "Payment Amount (₹)",
    min_value=1.0,
    value=2500.0
)

payment_method = st.selectbox(
    "Payment Method",
    ["UPI", "Credit Card", "Debit Card", "Wallet", "Net Banking"]
)

failure_reason = st.selectbox(
    "Failure Reason",
    [
        "Insufficient Funds",
        "Network Error",
        "Bank Error",
        "Technical Error",
        "Authentication Failed",
        "Other"
    ]
)

previous_successful_payments = st.number_input(
    "Previous Successful Payments",
    min_value=0,
    value=5
)

previous_failed_payments = st.number_input(
    "Previous Failed Payments",
    min_value=0,
    value=1
)

retry_count = st.number_input(
    "Retry Count",
    min_value=0,
    value=0
)

customer_tenure_days = st.number_input(
    "Customer Tenure (Days)",
    min_value=0,
    value=300
)

transaction_hour = st.slider(
    "Transaction Hour",
    min_value=0,
    max_value=23,
    value=14
)

day_of_week = st.slider(
    "Day of Week (0 = Monday)",
    min_value=0,
    max_value=6,
    value=2
)

# Prediction
if st.button("🔮 Predict Recovery", use_container_width=True):

    input_data = pd.DataFrame({
        "amount_inr": [amount_inr],
        "payment_method": [payment_method],
        "failure_reason": [failure_reason],
        "previous_successful_payments": [previous_successful_payments],
        "previous_failed_payments": [previous_failed_payments],
        "retry_count": [retry_count],
        "customer_tenure_days": [customer_tenure_days],
        "transaction_hour": [transaction_hour],
        "day_of_week": [day_of_week]
    })

    probability = model.predict_proba(input_data)[0][1]

    if probability >= 0.80:
        recommendation = "Retry Payment"
    elif probability >= 0.50:
        recommendation = "Try Alternate Payment Method"
    else:
        recommendation = "Do Not Retry Immediately"

    st.success(f"Recovery Probability: {probability:.2%}")

    st.subheader("Recommendation")

    if probability >= 0.80:
        st.success(f"✅ {recommendation}")
    elif probability >= 0.50:
        st.warning(f"⚠️ {recommendation}")
    else:
        st.error(f"❌ {recommendation}")

    st.caption(
        "This prototype uses a machine-learning model trained on synthetic payment data."
    )
