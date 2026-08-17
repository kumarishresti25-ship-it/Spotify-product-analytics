import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Spotify Product Analytics & Feature Adoption", layout="wide")

st.title("🎧 Spotify Product Usage & Feature Adoption Dashboard")
st.markdown("Analyzing discovery retention, personalized playlist engagement, and Free-to-Premium conversion metrics.")

# Load mock dashboard metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Monthly Active Users", "600M+", "+8% YoY")
col2.metric("Premium Conversion Rate", "15.2%", "+0.5%")
col3.metric("Personalized Feature Adoption", "45%", "AI DJ & Discover Weekly")
col4.metric("Daily Listening Time", "2.4 Hours", "+12 mins")

st.markdown("---")

# Funnel Visualization Section
st.subheader("📉 App-to-Listening Conversion Funnel")
funnel_data = pd.DataFrame({
    'Stage': ['App Launch', 'Search / Browse', 'Track Play', 'Save / View Lyrics', 'Completed Session'],
    'Users': [10000, 8000, 5200, 2600, 1950]
})
st.bar_chart(funnel_data.set_index('Stage'))

st.success("✅ Spotify analytics pipeline and dashboard successfully simulated.")