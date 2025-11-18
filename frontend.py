import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Bangaluru House Prediction")
st.markdown("Enter your details below:")

location = st.text_input("Enter your location")
BHK = st.number_input("Enter your house category(BHK)", min_value=1)
bath = st.number_input("Enter number bathroom", min_value=1.0)
total_sqft = st.number_input("Enter your house area (sqft)", min_value=1.0)

def format_price(price):
    """Convert number to human-friendly text"""
    if price >= 1e7:
        return f"₹ {price/1e7:.2f} Crores"
    elif price >= 1e5:
        return f"₹ {price/1e5:.2f} Lakhs"
    else:
        return f"₹ {price:,.0f}"

if st.button("Predict House price"):
    input_data = {
        "location": location,
        "BHK": BHK,
        "bath": bath,
        "total_sqft": total_sqft
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "prediction category" in result:
                prediction = result["prediction category"]
                formatted_prediction = format_price(prediction)

                st.success(f"### 💰 Predicted House Price:\n**{formatted_prediction}**")

        else:
                st.error(f"API Error: {response.status_code}")
                st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")
