import streamlit as st
import pandas as pd
import numpy as np
import joblib

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
h1, h2, h3, p, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("🔮 Sales Prediction")

col1, col2 = st.columns(2)

# INPUT
with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📥 Enter Details")

    item_mrp = st.slider("Item MRP", 50.0, 500.0, 150.0)
    item_weight = st.slider("Item Weight", 1.0, 20.0, 10.0)

    outlet_size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
    outlet_type = st.selectbox("Outlet Type", ["Supermarket Type1", "Supermarket Type2", "Grocery Store"])

    st.markdown('</div>', unsafe_allow_html=True)

# OUTPUT
with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📊 Result")

    if st.button("🚀 Predict"):
        input_data = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

        input_data["Item_MRP"] = item_mrp
        input_data["Item_Weight"] = item_weight

        if f"Outlet_Size_{outlet_size}" in columns:
            input_data[f"Outlet_Size_{outlet_size}"] = 1

        if f"Outlet_Type_{outlet_type}" in columns:
            input_data[f"Outlet_Type_{outlet_type}"] = 1

        prediction = model.predict(input_data)[0]

        st.success(f"💰 Predicted Sales: ₹ {prediction:.2f}")

    st.markdown('</div>', unsafe_allow_html=True)