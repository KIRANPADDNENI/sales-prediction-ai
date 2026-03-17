import streamlit as st
import pandas as pd

# ===== CSS =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
}

.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,255,255,0.25);
    color: white;
}
h1, h2, h3, p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard")

df = pd.read_csv("train.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="glass">📦 Total Products<br><h2>{len(df)}</h2></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="glass">💰 Avg Sales<br><h2>{int(df["Item_Outlet_Sales"].mean())}</h2></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="glass">📈 Max Sales<br><h2>{int(df["Item_Outlet_Sales"].max())}</h2></div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("📈 Sales Trend")
st.line_chart(df["Item_Outlet_Sales"])
st.markdown('</div>', unsafe_allow_html=True)