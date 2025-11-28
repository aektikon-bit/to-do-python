import streamlit as st

st.set_page_config(page_title="Mobile To-Do App", layout="centered")

# ---------------- CSS ----------------
css = """
<style>

html, body, [class*="css"] {
    font-family: "Prompt", sans-serif;
}

/* การ์ดแต่ละงาน */
.task-card {
    background: white;
    border-radius: 16px;
    padding: 14px 16px;
    margin-bottom: 12px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.12);
    display: flex;
    justify-content: space-between;   /* ทำให้ข้อความอยู่ซ้าย ปุ่มอยู่ขวา */
    align-items: center;              /* จัดปุ่มและข้อความให้อยู่กึ่งกลาง */
}

/* ข้อความงาน */
.task-text {
    font-size: 18px;
    flex-grow: 1;
}

.done {
    text-decoration: line-through;
    color: gray;
}

/* ปุ่มไอคอน */
.icon {
    background: #f2f2f2;
    border: 1px solid #dcdcdc;
    border-radius: 10px;
    padding: 6px 10px;
    font-size: 20px;
    margin-left: 6px;
}

.icon:hover {
    background: #e2e2e2;
}

</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ---------------- STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------------- INPUT ----------------
st.title("🧾 To-Do List")

new_task = st.text_input("", placeholder="เพิ่มงาน...")

if st.button("เพิ่มงาน", use_container_width=True):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.rerun()

# ---------------- LIST DISPLAY ----------------
st.write("## รายการของคุณ")

for i, task in enumerate(st.session_state.tasks):

    # แสดง UI การ์ด
    text_class = "task-text done" if task["done"] else "task-text"

    st.markdown(
        f"""
        <div class="task-card">
            <div class="{text_class}">
                {task["text"]}
            </div>
            <div style="display:flex;">
                <div id="done_btn_{i}"></div>
                <div id="del_btn_{i}"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ใส่ปุ่มลงในตำแหน่งที่กำหนด
    done_col = st.container()
    with done_col:
        if st.button("✔️", key=f"done_{i}"):
            st.session_state.tasks[i]["done"] = not st.session_state.tasks[i]["done"]
            st.rerun()

    del_col = st.container()
    with del_col:
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
