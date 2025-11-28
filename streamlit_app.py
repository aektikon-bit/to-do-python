import streamlit as st

st.set_page_config(page_title="Mobile To-Do App", layout="centered")

# ------------ CSS ------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: "Prompt", sans-serif;
}

/* การ์ดงาน */
.card {
    background: white;
    padding: 14px 16px;
    margin-bottom: 12px;
    border-radius: 16px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.12);
}

/* ข้อความงาน */
.task-text {
    font-size: 18px;
    display: flex;
    align-items: center;
}

.done {
    text-decoration: line-through;
    color: gray;
}

.icon-btn {
    background: #f2f2f2;
    border: 1px solid #dcdcdc;
    border-radius: 10px;
    padding: 6px 10px;
    font-size: 20px;
}

.icon-btn:hover {
    background: #e2e2e2;
}

</style>
""", unsafe_allow_html=True)

# ------------ STATE ------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ------------ INPUT ------------
st.title("🧾 To-Do List")

new_task = st.text_input("", placeholder="เพิ่มงานใหม่...")

if st.button("เพิ่มงาน", use_container_width=True):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.rerun()

# ------------ TASK LIST ------------
st.write("## รายการของคุณ")

for i, task in enumerate(st.session_state.tasks):

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # 3 คอลัมน์: ✔ | งาน | 🗑
    col1, col2, col3 = st.columns([0.12, 0.70, 0.18])

    # ------------------ ปุ่ม ✔ หน้า ------------------
    with col1:
        if st.button("✔", key=f"done_{i}"):
            st.session_state.tasks[i]["done"] = not st.session_state.tasks[i]["done"]
            st.rerun()

    # ------------------ ข้อความงาน ------------------
    with col2:
        text_class = "task-text done" if task["done"] else "task-text"
        st.markdown(f'<div class="{text_class}">{task["text"]}</div>', unsafe_allow_html=True)

    # ------------------ ปุ่ม 🗑 หลัง ------------------
    with col3:
        if st.button("🗑", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
