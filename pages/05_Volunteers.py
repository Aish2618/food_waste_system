# ------------------ VOLUNTEER SECTION ------------------
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Volunteer Management", layout="wide")

# ================= SESSION =================
if "volunteers" not in st.session_state:
    st.session_state.volunteers = []

# 👉 IMPORTANT (for emergency flow)
if "requests" not in st.session_state:
    st.session_state.requests = []

if "volunteer_notifications" not in st.session_state:
    st.session_state.volunteer_notifications = []

# ================= NAVBAR =================
st.markdown(f"""
<style>
.navbar {{
    position: sticky;
    top: 0;
    z-index: 999;
    display: flex;
    justify-content: space-between;
    padding: 12px 25px;
    background: rgba(0,0,0,0.7);
    border-radius: 10px;
    margin-bottom: 20px;
}}
.nav-left {{
    font-size: 22px;
    font-weight: bold;
    color: #4CAF50;
}}
.nav-right {{
    font-size: 14px;
    color: white;
}}
</style>

<div class="navbar">
    <div class="nav-left">🍱 Smart Food Rescue</div>
    <div class="nav-right">
        👤 {st.session_state.get('user')} | {st.session_state.get('role')}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"### 👋 Welcome, {st.session_state.get('user')}!")

# ================= LOGOUT =================
col1, col2, col3 = st.columns([8,1,1])
with col3:
    if st.button("🚪 Logout", key="logout_vol"):
        st.session_state.user = None
        st.session_state.role = None
        st.switch_page("app.py")

# ================= SECURITY =================
if st.session_state.get("role") != "Volunteer":
    st.error("❌ Only Volunteer can access this page")
    st.stop()

# ================= TITLE =================
st.markdown('<div class="title">🤝 Volunteer Management System</div>', unsafe_allow_html=True)

# ================= 🔔 NOTIFICATIONS =================
st.subheader("🔔 Pickup Notifications")

if st.session_state.volunteer_notifications:
    for n in st.session_state.volunteer_notifications:
        st.info(f"""
        🍱 Food Ready from {n['Hotel']}  
        📍 Location: {n['Location']}  
        🍽 Meals: {n['Meals']}
        """)
else:
    st.info("No pickup notifications yet")

# ================= 🚚 DELIVERY =================
st.subheader("🚚 Delivery Tasks")

for i, r in enumerate(st.session_state.requests):

    if r.get("Restaurant_Response") == "Accepted" and r.get("Delivered") == "No":

        st.write(f"""
        📍 {r['Location']}  
        🍽 Meals: {r['Meals']}  
        🏨 Restaurant: {r['Restaurant_Name']}  
        """)

        if st.button(f"🚚 Deliver {i}"):
            st.session_state.requests[i]["Delivered"] = "Yes"
            st.session_state.requests[i]["Status"] = "Completed"
            st.success("✅ Delivered successfully!")
            st.rerun()

# ================= FORM =================
st.subheader("📝 Register as Volunteer")

with st.form("volunteer_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Name")
        phone = st.text_input("📞 Phone")

    with col2:
        area = st.text_input("📍 Area / Location")
        role = st.selectbox("🎯 Role", ["Pickup", "Delivery", "Coordinator"])

    availability = st.selectbox("⏰ Availability", ["Full-Time", "Part-Time"])

    submit = st.form_submit_button("🚀 Register")

# ================= SAVE =================
if submit:
    st.session_state.volunteers.append({
        "Name": name,
        "Phone": phone,
        "Area": area,
        "Role": role,
        "Availability": availability,
        "Status": "Active",
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    st.success("✅ Volunteer Registered Successfully!")

# ================= LIST =================
st.subheader("📋 Volunteer List")

if st.session_state.volunteers:
    df = pd.DataFrame(st.session_state.volunteers)

    for i, row in df.iterrows():
        st.write(f"""
        👤 {row['Name']} | 📞 {row['Phone']}  
        📍 {row['Area']}  
        🎯 {row['Role']}  
        ⏰ {row['Availability']}  
        """)

        col1, col2 = st.columns(2)

        if col1.button(f"❌ Deactivate {i}"):
            st.session_state.volunteers[i]["Status"] = "Inactive"
            st.rerun()

        if col2.button(f"🗑 Remove {i}"):
            st.session_state.volunteers.pop(i)
            st.rerun()

else:
    st.info("No volunteers registered yet.")