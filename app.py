# ============================================================
# 🌍 ECONOMIC INEQUALITY INTELLIGENCE PLATFORM
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Economic Inequality Intelligence Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/global_poverty_economic_inequality.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Hero Section */
.hero-box {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #1F2937);
    border: 1px solid #374151;
    margin-bottom: 2rem;
}

/* KPI Cards */
.kpi-card {
    background: #1F2937;
    padding: 1.5rem;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #374151;
    transition: 0.3s;
}

.kpi-card:hover {
    transform: translateY(-5px);
    border: 1px solid #6366F1;
}

/* Section Headings */
.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title("🌍 Economic Intelligence")

st.sidebar.markdown("""
### 📌 Navigation

Use the sidebar pages to explore:

- 📊 Analytics Dashboard
- 🤖 AI Prediction System
- 📈 Model Insights
- 📖 About Project
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "AI + Machine Learning platform for analyzing global poverty and economic inequality."
)

# ------------------------------------------------------------
# HERO SECTION
# ------------------------------------------------------------

st.markdown("""
<div class="hero-box">
    <h1>🌍 Economic Inequality Intelligence Platform</h1>
    <p style='font-size:18px;'>
        A professional AI + Machine Learning dashboard designed to analyze,
        visualize, and predict global poverty & economic inequality patterns.
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# KPI SECTION
# ------------------------------------------------------------

st.markdown(
    "<div class='section-title'>📊 Global Dataset Overview</div>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <h2>{df.shape[0]}</h2>
        <p>Total Records</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <h2>{df.shape[1]}</h2>
        <p>Total Features</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_poverty = round(df["poverty_rate_pct"].mean(), 2)

    st.markdown(f"""
    <div class="kpi-card">
        <h2>{avg_poverty}%</h2>
        <p>Average Poverty Rate</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    max_poverty = round(df["poverty_rate_pct"].max(), 2)

    st.markdown(f"""
    <div class="kpi-card">
        <h2>{max_poverty}%</h2>
        <p>Highest Poverty Rate</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------
# PROJECT OVERVIEW
# ------------------------------------------------------------

st.markdown(
    "<div class='section-title'>🚀 Platform Highlights</div>",
    unsafe_allow_html=True
)

feature1, feature2 = st.columns(2)

with feature1:
    st.markdown("""
    ### 📊 Analytics Dashboard
    - Interactive visualizations
    - Poverty trend analysis
    - Correlation heatmaps
    - Feature exploration
    - Economic insights
    """)

    st.markdown("""
    ### 🤖 AI Prediction System
    - Machine Learning powered predictions
    - Random Forest Classifier
    - Real-time inference
    - Intelligent poverty classification
    """)

with feature2:
    st.markdown("""
    ### 📈 Model Insights
    - Model performance metrics
    - Confusion matrix analysis
    - Feature importance
    - Accuracy comparison
    """)

    st.markdown("""
    ### 🌐 Deployment Ready
    - Streamlit Cloud compatible
    - GitHub portfolio ready
    - Professional architecture
    - Scalable ML dashboard
    """)

# ------------------------------------------------------------
# DATA PREVIEW
# ------------------------------------------------------------

st.markdown(
    "<div class='section-title'>📂 Dataset Preview</div>",
    unsafe_allow_html=True
)

st.dataframe(df.head(10), use_container_width=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")

st.markdown("""
<div class="footer">
    🌍 Economic Inequality Intelligence Platform <br>
    Built with Streamlit • Machine Learning • Data Analytics
</div>
""", unsafe_allow_html=True)