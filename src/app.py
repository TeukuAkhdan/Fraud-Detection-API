import streamlit as st
import requests

# FastAPI endpoint URL
API_URL = "http://localhost:8000/prediction"  # Update with your FastAPI server URL

st.title("Credit Card Fraud Detector")

# Input form for user to enter transaction details
st.header("Enter Transaction Details")
step = st.number_input("Step", min_value=1, value=1)
trans_type = st.selectbox("Transaction Type", ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])
amount = st.number_input("Amount", min_value=0.0, value=100.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=500.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=450.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=1000.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=950.0)

# Make prediction button
if st.button("Make Prediction"):
    # Prepare data for API request
    data = {
        "step": step,
        "type": trans_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
    }

    # Make API request to FastAPI endpoint
    response = requests.post(API_URL, json=data)

    # Display prediction result
    result = response.json()
    st.subheader("Prediction Result:")
    st.write(result["Result"])
