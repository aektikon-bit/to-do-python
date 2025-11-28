import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Mobile To-Do App", layout="centered")

# ---------------- CSS (ดีไซน์ใหม่ทั้งหมด) ----------------
css = """
<style>

html, body, [class*="css"] {
    font-family: "Prompt", sans-serif;
}

h1 {
    font-weight: 700;
}

/* กล่องอินพุต */
.stTextInput > div > div > input {
    border-radius: 14px !important;
    padding: 13px 14px !important;
    font-size: 17px !important;
    border: 1.5px solid #d9d9d9;
}

/* ปุ่มหลัก */
.stButton > button {
    background: #4a90e2 !important;
    color: white !important;
    border-radius: 14px !important;
    padding: 12px 0px !important;
    font-size: 18px !important;
    border: none !important;
}

/* การ์ดรายการ */
.task-card {
    background: white;
    border-radius: 18px;
    padding: 14px 16px;
    margin-bottom: 14px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.12);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* ข้อความงาน */
.task-text {
    font-size: 18px;
}

/* สถานะงานเสร็จ */
.done {
    text-decoration: line-through;
    color: #8d8d8d;
}

/* ปุ่มไอคอน */
.icon-btn {
    background: #f5f5f5;
    border-radius: 12px;
    padding: 8px 12px;
    font-size: 20px;
    border: 1px solid #e0e0e0;
}

.icon-btn:hover {
    background: #dedede;
}

</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ---------------- STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center; font-size:40px;'>🧾 To-Do List</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-size:18px; color:gray;'>สไตล์แอปมือถือที่สวยและใช้งานง่าย</p>",
    unsafe_allow_html=True
)

st.write("")

# ---------------- INPUT ----------------
new_task = st.text_input("", placeholder="เพิ่มงานใหม่ เช่น ทำการบ้านคณิต", label_visibility="collapsed")

st.write("")
if st.button("เพิ่มงาน", use_container_width=True):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.rerun()

st.write("## รายการของคุณ")

# ---------------- LIST DISPLAY ----------------

if not st.session_state.tasks:
    st.info("🎉 เยี่ยมมาก! ไม่มีงานค้างแล้ว")
else:
    for i, task in enumerate(st.session_state.tasks):
        text_class = "task-text done" if task["done"] else "task-text"

        st.markdown(
            f"""
            <div class="task-card">
                <div class="{text_class}">
                    {task['text']}
                </div>
                <div style='display:flex; gap:8px;'>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([0.2, 0.2])

        with col1:
            if st.button("✔️", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = not st.session_state.tasks[i]["done"]
                st.rerun()

        with col2:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

        st.markdown("</div></div>", unsafe_allow_html=True)
