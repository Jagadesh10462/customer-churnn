# Customer Churn Prediction using Snowflake ML

An end-to-end demonstration of customer churn classification using Snowflake ML and Streamlit.

## Features

- Snowflake database, schema and warehouse setup
- Customer data table
- Snowflake ML Classification model
- Model evaluation
- Customer churn prediction
- Streamlit web interface
- GitHub-ready project structure

## Project Structure

```text
customer-churn-snowflake/
├── README.md
├── customer_churn.sql
├── streamlit_app.py
├── requirements.txt
└── .gitignore
```

## Snowflake Setup

1. Open a Snowflake SQL Worksheet.
2. Open `customer_churn.sql`.
3. Run the SQL statements.
4. Confirm that `CUSTOMER_CHURN_MODEL` is created successfully.
5. Confirm that `CHURN_DASHBOARD` returns prediction results.

## Streamlit Deployment

This project can be deployed using Streamlit Community Cloud.

1. Push this repository to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `streamlit_app.py` as the main file.
5. Add Snowflake credentials under Streamlit Secrets.

Example secrets:

```toml
[snowflake]
account = "YOUR_ACCOUNT"
user = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
warehouse = "ML_WH"
```

Never commit `secrets.toml` or passwords to GitHub.

## Important Limitation

The included SQL uses 10 manually created demonstration records. This is sufficient to demonstrate the workflow but is not sufficient for reliable real-world model evaluation. A larger representative dataset should be used for production.

## Technologies

- Snowflake
- Snowflake ML Classification
- SQL
- Python
- Streamlit
- GitHub
