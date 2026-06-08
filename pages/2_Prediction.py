# ============================================================
# 🤖 POVERTY CLASS PREDICTION SYSTEM
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="AI Poverty Prediction",
    page_icon="🤖",
    layout="wide"
)

# ------------------------------------------------------------
# LOAD MODEL & SCALER
# ------------------------------------------------------------

model = pickle.load(open("models/inequality_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

# ------------------------------------------------------------
# LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("dataset/global_poverty_economic_inequality.csv")
df.columns = df.columns.str.strip()

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("🤖 AI Poverty Classification System")

st.markdown("""
Predict global poverty levels using Machine Learning and economic indicators.
""")

st.markdown("---")

# ------------------------------------------------------------
# FEATURE SELECTION
# ------------------------------------------------------------

feature_columns = [
    col for col in df.columns
    if col not in ["poverty_rate_pct", "Poverty_Class"]
]

# ------------------------------------------------------------
# USER INPUTS
# ------------------------------------------------------------

st.subheader("📥 Enter Economic Indicators")

input_data = {}

cols = st.columns(3)

for i, feature in enumerate(feature_columns):

    with cols[i % 3]:

        # Numeric Columns
        if pd.api.types.is_numeric_dtype(df[feature]):

            value = st.number_input(
                feature,
                value=float(df[feature].mean())
            )

        # Categorical Columns
        else:

            options = (
                df[feature]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            value = st.selectbox(
                feature,
                options
            )

        input_data[feature] = value

# ------------------------------------------------------------
# CONVERT INPUT TO DATAFRAME
# ------------------------------------------------------------

input_df = pd.DataFrame([input_data])

# ------------------------------------------------------------
# HANDLE CATEGORICAL DATA
# ------------------------------------------------------------

for col in input_df.columns:

    if not pd.api.types.is_numeric_dtype(input_df[col]):

        input_df[col] = pd.factorize(input_df[col])[0]

# ------------------------------------------------------------
# ENSURE COLUMN ORDER MATCHES TRAINING DATA
# ------------------------------------------------------------

input_df = input_df[feature_columns]

# ------------------------------------------------------------
# SCALE INPUT
# ------------------------------------------------------------

try:

    input_scaled = scaler.transform(input_df)

except Exception as e:

    st.error(f"Scaling Error: {e}")
    st.stop()

# ------------------------------------------------------------
# PREDICTION BUTTON
# ------------------------------------------------------------

if st.button("🚀 Predict Poverty Class"):

    try:

        prediction = model.predict(input_scaled)[0]

        st.markdown("---")

        st.subheader("📊 Prediction Result")

        if prediction == "Low":

            st.success("🟢 Low Poverty Region")

        elif prediction == "Medium":

            st.warning("🟡 Medium Poverty Region")

        else:

            st.error("🔴 High Poverty Region")

    except Exception as e:

        st.error(f"Prediction Error: {e}")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")

st.markdown("""
🌍 AI Powered Economic Inequality Intelligence Platform
""")