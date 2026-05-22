# ============================================================
# 📈 MODEL INSIGHTS DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.figure_factory as ff

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Model Insights",
    page_icon="📈",
    layout="wide"
)

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv("dataset/global_poverty_economic_inequality.csv")
df.columns = df.columns.str.strip()

# ------------------------------------------------------------
# CREATE POVERTY CLASS
# ------------------------------------------------------------

df["Poverty_Class"] = pd.cut(
    df["poverty_rate_pct"],
    bins=[0, 30, 70, 100],
    labels=["Low", "Medium", "High"]
)

# ------------------------------------------------------------
# FEATURE & TARGET
# ------------------------------------------------------------

X = df.drop(["poverty_rate_pct", "Poverty_Class"], axis=1)
y = df["Poverty_Class"]

# ------------------------------------------------------------
# LABEL ENCODING
# ------------------------------------------------------------

from sklearn.preprocessing import LabelEncoder

categorical_cols = X.select_dtypes(include="object").columns

le = LabelEncoder()

for col in categorical_cols:
    X[col] = le.fit_transform(X[col])

# ------------------------------------------------------------
# TRAIN TEST SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------

model = pickle.load(open("models/inequality_model.pkl", "rb"))

# ------------------------------------------------------------
# PREDICTIONS
# ------------------------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------------------------
# METRICS
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("📈 Machine Learning Model Insights")

st.markdown("""
Performance evaluation and insights of the AI poverty classification model.
""")

st.markdown("---")

# ------------------------------------------------------------
# KPI CARDS
# ------------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", f"{accuracy:.2%}")

with col2:
    st.metric("Training Records", X_train.shape[0])

with col3:
    st.metric("Testing Records", X_test.shape[0])

# ------------------------------------------------------------
# CLASSIFICATION REPORT
# ------------------------------------------------------------

st.subheader("📋 Classification Report")

report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df, use_container_width=True)

# ------------------------------------------------------------
# CONFUSION MATRIX
# ------------------------------------------------------------

st.subheader("🧠 Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig = ff.create_annotated_heatmap(
    z=cm,
    x=["Low", "Medium", "High"],
    y=["Low", "Medium", "High"],
    colorscale="Blues",
    showscale=True
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------
# FEATURE IMPORTANCE
# ------------------------------------------------------------

st.subheader("🔥 Feature Importance")

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

fig2 = px.bar(
    importance_df.head(10),
    x="Importance",
    y="Feature",
    orientation="h",
    template="plotly_dark",
    title="Top 10 Important Features"
)

st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------
# MODEL INTERPRETATION
# ------------------------------------------------------------

st.subheader("🧠 Model Interpretation")

st.markdown("""
### Key Insights

- Random Forest achieved strong classification performance.
- Model successfully distinguishes poverty categories.
- Feature importance highlights major economic indicators.
- AI system is deployment-ready for real-time prediction.

### Why Random Forest?

✔ Handles complex relationships  
✔ Strong classification accuracy  
✔ Resistant to overfitting  
✔ Excellent for tabular economic data  
""")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")

st.markdown("""
🌍 Economic Inequality Intelligence Platform
""")