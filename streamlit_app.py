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
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---- HEADER ----
st.markdown("<h1 style='text-align:center; font-size:36px; margin-top:-20px;'>📱 To-Do List</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center; font-size:18px; color:gray;'>สไตล์แอปมือถือที่ใช้ง่ายสุดๆ</p>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---- INPUT ----
new_task = st.text_input("เพิ่มงานใหม่", placeholder="พิมพ์สิ่งที่ต้องทำ...")

if st.button("เพิ่มงาน", use_container_width=True):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.rerun()

# ---- LIST ----
st.write("## รายการของคุณ")

if not st.session_state.tasks:
    st.info("🎉 ไม่มีงานค้างเลย เก่งมาก!")
else:
    for i, task in enumerate(st.session_state.tasks):

        # แสดงงานในการ์ด
        bg = "#d4f8d4" if task["done"] else "#ffffff"
        text_dec = "line-through; color: #777;" if task["done"] else "none"

        st.markdown(
            f"""
            <div class="task-card" style="background:{bg};">
                <div style="flex-grow:1; font-size:18px; text-decoration:{text_dec};">
                    {task['text']}
                </div>
                <div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([0.2,0.2])

        with col1:
            if st.button("✔️", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = not task["done"]
                st.rerun()

        with col2:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

        st.markdown("</div></div>", unsafe_allow_html=True)
