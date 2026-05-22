# ============================================================
# 📖 ABOUT PROJECT PAGE
# ============================================================

import streamlit as st

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="About Project",
    page_icon="📖",
    layout="wide"
)

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("📖 About The Project")

st.markdown("""
# 🌍 Economic Inequality Intelligence Platform

A professional AI + Machine Learning dashboard designed to analyze,
visualize, and predict global poverty & economic inequality patterns.
""")

st.markdown("---")

# ------------------------------------------------------------
# PROJECT OVERVIEW
# ------------------------------------------------------------

st.header("🚀 Project Overview")

st.markdown("""
The Economic Inequality Intelligence Platform is a portfolio-grade
Machine Learning project developed using Python, Streamlit, and Scikit-learn.

This platform helps users:

- Analyze economic inequality trends
- Explore poverty-related indicators
- Visualize global poverty patterns
- Predict poverty classifications using AI
- Understand model performance through ML insights
""")

# ------------------------------------------------------------
# MACHINE LEARNING WORKFLOW
# ------------------------------------------------------------

st.header("🤖 Machine Learning Workflow")

st.markdown("""
### The project follows a complete professional ML pipeline:

1. Data Collection & Loading  
2. Data Cleaning & Missing Value Handling  
3. Exploratory Data Analysis (EDA)  
4. Data Visualization  
5. Label Encoding  
6. Feature Scaling  
7. SMOTE Balancing  
8. Train-Test Split  
9. Model Training  
10. Hyperparameter Tuning  
11. Model Evaluation  
12. Feature Importance Analysis  
13. Model Deployment using Streamlit
""")

# ------------------------------------------------------------
# TECHNOLOGIES USED
# ------------------------------------------------------------

st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### 📚 Python Libraries
    - Pandas
    - NumPy
    - Scikit-learn
    - Plotly
    - Streamlit
    - Matplotlib
    - Seaborn
    - Imbalanced-learn
    """)

with col2:

    st.markdown("""
    ### 🤖 Machine Learning Models
    - Logistic Regression
    - Random Forest Classifier
    - Support Vector Machine
    - K-Nearest Neighbors
    - Decision Tree Classifier
    """)

# ------------------------------------------------------------
# PROJECT FEATURES
# ------------------------------------------------------------

st.header("🔥 Platform Features")

st.markdown("""
✔ Premium Multi-Page Streamlit Dashboard  
✔ AI Poverty Prediction System  
✔ Interactive Analytics Dashboard  
✔ Feature Importance Analysis  
✔ Confusion Matrix Visualization  
✔ Model Performance Insights  
✔ Dark Professional UI  
✔ GitHub Portfolio Ready  
✔ Streamlit Deployment Ready  
""")

# ------------------------------------------------------------
# BUSINESS IMPACT
# ------------------------------------------------------------

st.header("🌍 Potential Real-World Impact")

st.markdown("""
This type of AI system can help:

- Economic researchers
- NGOs
- Policy makers
- Government organizations
- Social development analysts

to better understand poverty trends and economic inequality patterns.
""")

# ------------------------------------------------------------
# DEVELOPER SECTION
# ------------------------------------------------------------

st.header("👨‍💻 Developer")

st.markdown("""
### Developed By
**Syed Najam Ul Hassan Rizvi**

Aspiring Data Analyst & Machine Learning Developer

Focused on:
- Data Analytics
- Machine Learning
- AI Dashboards
- Streamlit Applications
- Data Visualization
""")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")

st.markdown("""
🌍 Economic Inequality Intelligence Platform  
Built with ❤️ using Streamlit & Machine Learning
""")