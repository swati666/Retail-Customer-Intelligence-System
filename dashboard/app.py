import streamlit as st
import requests

st.title("Retail Churn Prediction Dashboard")

customer_id = st.number_input(
    "Enter Household Key",
    min_value=1,
    step=1,
    format="%d"
)


if st.button("Predict Churn"):

    url = f"http://127.0.0.1:8000/predict_customer_churn/{customer_id}"

    response = requests.get(url)

    data = response.json()

    prob = data["churn_probability"] * 100
    st.write(f"Churn Probability: {prob:.2f}%")

    prob = data["churn_probability"]

    if prob > 0.7:
        st.error("🔴 High churn risk")
    elif prob > 0.4:
        st.warning("🟡 Medium churn risk")
    else:
        st.success("🟢 Customer active")
        
    if prob > 0.7:
        st.info("Recommendation: Offer discount coupon")
    elif prob > 0.4:
        st.info("Recommendation: Send targeted promotion")
    else:
        st.info("Recommendation: Maintain engagement")
    