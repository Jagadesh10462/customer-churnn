import os
import streamlit as st
import pandas as pd
import snowflake.connector

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="wide")
st.title("📊 Customer Churn Prediction")
st.caption("Snowflake ML Classification demo")

st.info("This is a demonstration model trained on a small sample dataset. Results are not intended for production use.")

def get_connection():
    return snowflake.connector.connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database="CUSTOMER_CHURN_DB",
        schema="ML_SCHEMA"
    )

st.sidebar.header("Customer Details")
age = st.sidebar.number_input("Age", 18, 100, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
income = st.sidebar.number_input("Income", 0.0, 1000000.0, 40000.0)
frequency = st.sidebar.number_input("Purchase Frequency", 0.0, 100.0, 3.0)
aov = st.sidebar.number_input("Average Order Value", 0.0, 100000.0, 700.0)
spend = st.sidebar.number_input("Total Spend", 0.0, 1000000.0, 2500.0)
lifetime = st.sidebar.number_input("Customer Lifetime (months)", 1, 240, 24)

if st.button("Predict Churn", type="primary"):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = '''
        SELECT CUSTOMER_CHURN_MODEL!PREDICT(
            OBJECT_CONSTRUCT(
                'AGE', %s,
                'GENDER', %s,
                'INCOME', %s,
                'PURCHASE_FREQUENCY', %s,
                'AVERAGE_ORDER_VALUE', %s,
                'TOTAL_SPEND', %s,
                'CUSTOMER_LIFETIME_MONTHS', %s
            )
        ) AS PREDICTION
        '''

        cur.execute(query, (age, gender, income, frequency, aov, spend, lifetime))
        result = cur.fetchone()[0]

        prediction = result if isinstance(result, dict) else result
        predicted_class = prediction.get("class", "N/A")
        probabilities = prediction.get("probability", {})
        churn_probability = float(probabilities.get("1", 0))

        col1, col2 = st.columns(2)
        col1.metric("Predicted Class", "Churn" if str(predicted_class) == "1" else "No Churn")
        col2.metric("Churn Probability", f"{churn_probability:.0%}")

        st.subheader("Prediction Details")
        st.json(prediction)

        cur.close()
        conn.close()
    except Exception as e:
        st.error("Connection or prediction failed.")
        st.code(str(e))
        st.markdown("Check your Streamlit secrets and Snowflake credentials.")

st.divider()
st.subheader("Project")
st.write("Customer churn classification using Snowflake ML, with a Streamlit interface.")
