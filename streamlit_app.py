import streamlit as st

# --- ส่วนหัว ---
st.title("📝 My To-Do List")
st.write("แอพบันทึกงานฉบับนักเรียน")

# --- ส่วนความจำ ---
if 'tasks' not in st.session_state:
    st.session_state.tasks = []  # เก็บเป็น list ของ dict เช่น {"text": "...", "done": False}

# --- ส่วนเพิ่มงาน ---
col1, col2 = st.columns([0.8, 0.2])
with col1:
    new_task = st.text_input("เพิ่มรายการใหม่:", placeholder="พิมพ์สิ่งที่ต้องทำ...", label_visibility="collapsed")
with col2:
    add_btn = st.button("เพิ่มงาน", use_container_width=True)

if add_btn and new_task:
    st.session_state.tasks.append({"text": new_task, "done": False})
    st.rerun()

# --- แสดงรายการงาน ---
st.divider()
st.subheader(f"รายการที่ต้องทำ ({len(st.session_state.tasks)})")

for i, task in enumerate(st.session_state.tasks):

    c1, c2, c3 = st.columns([0.1, 0.75, 0.15])

    # checkbox ทำเครื่องหมายเสร็จ
    with c1:
        done = st.checkbox("", value=task["done"], key=f"done_{i}")
        st.session_state.tasks[i]["done"] = done

    # แสดงข้อความงาน
    with c2:
        if done:
            st.success(f"~~{task['text']}~~ ✔")
        else:
            st.write(task["text"])

    # ปุ่มลบงาน
    with c3:
        if st.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# --- ส่วนท้าย ---
if len(st.session_state.tasks) == 0:
    st.info("ยังไม่มีงานค้าง เย้! 🎉")
