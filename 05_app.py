## Example - 5 :: Form Section + Progress Bar 
import streamlit as st
import time

st.title("Order Processing App")

# ---------- Form Section ----------
with st.form("order_form"):
    name = st.text_input("Name")
    quantity = st.number_input(
        "Quantity", min_value=1, max_value=100, value=1
    )
    submitted = st.form_submit_button("Place Order")

# ---------- Progress Section ----------
if submitted:
    st.info("Processing your order...")

    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        time.sleep(0.02)  # simulate long task
        progress.progress(i + 1)
        status.text(f"Processing step {i + 1}/100")

    status.empty()
    st.success(f" Order placed successfully: {name} × {quantity}")
