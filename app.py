import streamlit as st

st.set_page_config(page_title="Smart Sales AI", layout="wide")

# ===== GLASS CSS =====
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
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    color: white;
}

h1, h2, h3, p {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ===== HOME PAGE =====
st.markdown("""
<div class="glass">
    <h1>💎 Smart Sales Intelligence System</h1>
    <p>AI-powered dashboard for prediction & analytics</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("### 🚀 Features")
st.write("📊 Dashboard")
st.write("🔮 Sales Prediction")
st.write("📈 Analytics")

st.info("👉 Use the sidebar to navigate")