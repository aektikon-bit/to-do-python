import streamlit as st

# ---- CONFIG ----
st.set_page_config(page_title="Mobile To-Do App", layout="centered")

# ---- CUSTOM CSS (สไตล์มือถือ) ----
mobile_style = """
<style>
/* ฟอนต์กลมมน */
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

/* กล่องการ์ด */
.task-card {
    background: #ffffff;
    padding: 14px 18px;
    border-radius: 18px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* ปุ่ม */
button[kind="primary"] {
    border-radius: 12px !important;
    padding: 10px 0px !important;
    font-size: 18px !important;
}

.stTextInput > div > div > input {
    border-radius: 12px !important;
    padding: 12px;
    font-size: 16px;
}

/* ปุ่มลบ */
.delete-btn {
    background: #ff4d4f;
    color: white;
    border-radius: 12px;
    padding: 6px 10px;
    font-size: 20px;
    border: none;
}

</style>
"""
st.markdown(mobile_style, unsafe_allow_html=True)

# ---- STATE ----
if "task
