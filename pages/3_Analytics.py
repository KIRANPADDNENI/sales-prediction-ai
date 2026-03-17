import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===== CSS =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
}

.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,255,255,0.25);
    color: white;
}
h1, h2, h3, p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📈 Analytics")

df = pd.read_csv("train.csv")

# Scatter
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("Sales vs MRP")

fig, ax = plt.subplots()
ax.scatter(df["Item_MRP"], df["Item_Outlet_Sales"])

st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# Bar chart
st.write("")
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("Outlet Type vs Sales")
st.bar_chart(df.groupby("Outlet_Type")["Item_Outlet_Sales"].mean())
st.markdown('</div>', unsafe_allow_html=True)