import streamlit as st

st.set_page_config(page_title="Mobile To-Do App", layout="centered")

# ---------------- CSS ----------------
css = """
<style>

html, body, [class*="css"] {
    font-family: "Prompt", sans-serif;
}

.task-card {
    background: white;
    border-radius: 16px;
    padding: 12px 16px;
    margin-bottom: 12px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.10);
    display: flex;
    justify-content: space-between;
    align-items: center;      /* <<< ทำให้ปุ่มและข้อความอยู่กึ่งกลางแนวตั้ง */
}

/* ข้อความงาน */
.task-text {
    font-size: 18px;
    flex-grow: 1;             /* <<< ทำให้กินพื้นที่ด้านซ้าย */
    padding-right: 10px;
}

.done {
    text-decoration: line-through;
    color: #8d8d8d;
}

/* ปุ่มไอคอน */
.icon-btn {
    background: #f0f0f0;
    border-radius: 12px;
    padding: 6px 10px;
    font-size: 20px;
    border: 1px solid #dcdcdc;
    cursor: pointer;
    margin-left: 6px;
}

.icon-btn:hover {
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

# ---------------- LIST ----------------
st.write("## รายการของคุณ")

for i, task in enumerate(st.session_state.tasks):
    
    text_class = "task-text done" if task["done"] else "task-text"

    st.markdown(
        f"""
        <div class="task-card">
            <div class="{text_class}">
                {task['text']}
            </div>
            <div>
                <form action="" method="post">
                    <button class="icon-btn" type="submit" name="done_{i}">✔</button>
                    <button class="icon-btn" type="submit" name="del_{i}">🗑</button>
                </form>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # จัดการปุ่มใน form
    if f"done_{i}" in st.session_state:
        st.session_state.tasks[i]["done"] = not st.session_state.tasks[i]["done"]
        st.session_state.pop(f"done_{i}", None)
        st.rerun()

    if f"del_{i}" in st.session_state:
        st.session_state.tasks.pop(i)
        st.session_state.pop(f"del_{i}", None)
        st.rerun()
