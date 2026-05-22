# ============================================================
# 🌍 ECONOMIC INEQUALITY - ANALYTICS DASHBOARD (FIXED)
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Economic Inequality Analytics",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/global_poverty_economic_inequality.csv")
    df.columns = df.columns.str.strip()  # important fix
    return df

df = load_data()

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("🌍 Economic Inequality Intelligence - Analytics Dashboard")
st.markdown("Interactive insights into global poverty & economic inequality trends")

# ------------------------------------------------------------
# KPI SECTION
# ------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", df.shape[0])

with col2:
    st.metric("Total Features", df.shape[1])

with col3:
    st.metric("Avg Poverty Rate (%)", round(df["poverty_rate_pct"].mean(), 2))

with col4:
    st.metric("Max Poverty Rate (%)", round(df["poverty_rate_pct"].max(), 2))

# ------------------------------------------------------------
# DATA PREVIEW
# ------------------------------------------------------------

st.subheader("📂 Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

# ------------------------------------------------------------
# POVERTY RATE DISTRIBUTION
# ------------------------------------------------------------

st.subheader("🌍 Poverty Rate Distribution")

fig1 = px.histogram(
    df,
    x="poverty_rate_pct",
    nbins=30,
    color_discrete_sequence=["#636EFA"],
    template="plotly_dark"
)

fig1.update_layout(
    xaxis_title="Poverty Rate (%)",
    yaxis_title="Count"
)

st.plotly_chart(fig1, use_container_width=True)

# ------------------------------------------------------------
# CORRELATION HEATMAP
# ------------------------------------------------------------

st.subheader("📈 Feature Correlation Heatmap")

numeric_df = df.select_dtypes(include=np.number)

fig2 = px.imshow(
    numeric_df.corr(),
    text_auto=True,
    color_continuous_scale="RdBu_r",
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------
# FEATURE EXPLORATION
# ------------------------------------------------------------

st.subheader("📊 Feature Explorer")

feature = st.selectbox(
    "Select Feature",
    numeric_df.columns
)

fig3 = px.histogram(
    df,
    x=feature,
    nbins=30,
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------
# SCATTER INSIGHT (BONUS VISUAL)
# ------------------------------------------------------------

st.subheader("📉 Poverty Rate vs Selected Feature")

scatter_feature = st.selectbox(
    "Compare Poverty Rate with:",
    [col for col in numeric_df.columns if col != "poverty_rate_pct"]
)

fig4 = px.scatter(
    df,
    x=scatter_feature,
    y="poverty_rate_pct",
    trendline="ols",
    template="plotly_dark"
)

st.plotly_chart(fig4, use_container_width=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")
st.markdown("🌍 Built for Economic Inequality Intelligence Platform | Streamlit + ML + Data Science")