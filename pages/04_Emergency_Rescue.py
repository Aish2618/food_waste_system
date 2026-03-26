import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

# ================= NAVBAR =================
st.markdown(f"""
<style>

/* Sticky Navbar */
.navbar {{
    position: sticky;
    top: 0;
    z-index: 999;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 25px;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(10px);
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

.page-name {{
    color: #ffa726;
    font-weight: bold;
}}

</style>

<div class="navbar">
    <div class="nav-left">🍱 Smart Food Rescue</div>
    <div class="nav-right">
        👤 {st.session_state.get('user')} | {st.session_state.get('role')} |
        <span class="page-name">EMERGENCY RESCUE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= WELCOME =================
st.markdown(f"### 👋 Welcome, {st.session_state.get('user')}!")

# ================= LOGOUT =================
col1, col2, col3 = st.columns([8,1,1])
with col3:
    if st.button("🚪 Logout"):
        st.session_state.user = None
        st.session_state.role = None
        st.switch_page("App.py")   # ✅ FIXED

# ================= SESSION =================
if "requests" not in st.session_state:
    st.session_state.requests = []

# Default role only if not set
if "role" not in st.session_state:
    st.session_state.role = "NGO"

st.sidebar.write(f"👤 Role: {st.session_state.role}")

# ================= TITLE =================
st.title("🚨 Emergency Rescue System")

# =========================================================
# 🏥 NGO → SEND REQUEST
# =========================================================
if st.session_state.role == "NGO":

    st.subheader("📢 Send Emergency Request")

    with st.form("ngo_form"):
        location = st.text_input("📍 Location")
        meals = st.number_input("🍽 Meals Needed", min_value=1)
        submit = st.form_submit_button("Send Request")

    if submit:
        st.session_state.requests.append({
            "Location": location,
            "Meals": meals,
            "Status": "Waiting for Restaurant",
            "Restaurant_Response": "Pending",
            "Delivered": "No",
            "Time": datetime.now().strftime("%H:%M")
        })
        st.success("✅ Sent to Restaurant!")

# =========================================================
# 🍱 RESTAURANT
# =========================================================
elif st.session_state.role == "Restaurant":

    st.subheader("🍱 Restaurant Panel")

    for i, r in enumerate(st.session_state.requests):

        st.write(f"📍 {r['Location']} | 🍽 {r['Meals']} meals")

        if r["Restaurant_Response"] == "Pending":

            col1, col2 = st.columns(2)

            if col1.button(f"✅ Accept {i}"):
                st.session_state.requests[i]["Restaurant_Response"] = "Accepted"
                st.session_state.requests[i]["Status"] = "Food Preparing"
                st.rerun()

            if col2.button(f"❌ Reject {i}"):
                st.session_state.requests[i]["Restaurant_Response"] = "Rejected"
                st.session_state.requests[i]["Status"] = "Rejected"
                st.rerun()

# =========================================================
# 🚚 VOLUNTEER
# =========================================================
elif st.session_state.role == "Volunteer":

    st.subheader("🚚 Volunteer Panel")

    for i, r in enumerate(st.session_state.requests):

        if r["Restaurant_Response"] == "Accepted" and r["Delivered"] == "No":

            st.write(f"📍 {r['Location']} | 🍽 {r['Meals']} meals")

            if st.button(f"🚚 Deliver {i}"):
                st.session_state.requests[i]["Delivered"] = "Yes"
                st.session_state.requests[i]["Status"] = "Completed"
                st.success("🎉 Delivery Completed!")
                st.rerun()

# =========================================================
# 📊 REQUEST STATUS (🔥 BEAUTIFUL + FIXED)
# =========================================================
st.markdown("---")
st.subheader("📋 Request Status")

for r in st.session_state.requests:

    if r["Delivered"] == "Yes":
        st.markdown(f"""
        <div style="
            background: rgba(76,175,80,0.15);
            padding:15px;
            border-left:6px solid #4CAF50;
            border-radius:10px;
            margin-bottom:10px;">
            
            <b>✅ Delivery Completed</b><br>
            📍 {r['Location']}<br>
            🍽 Meals: {r['Meals']}<br>
            ⏰⏰ {r.get('Time', 'Not Available')} 
        </div>
        """, unsafe_allow_html=True)

    elif r["Restaurant_Response"] == "Rejected":
        st.markdown(f"""
        <div style="
            background: rgba(244,67,54,0.15);
            padding:15px;
            border-left:6px solid #f44336;
            border-radius:10px;
            margin-bottom:10px;">
            
            <b>❌ Request Rejected</b><br>
            📍 {r['Location']}<br>
            🍽 Meals: {r['Meals']}
        </div>
        """, unsafe_allow_html=True)

    elif r["Restaurant_Response"] == "Accepted":
        st.markdown(f"""
        <div style="
            background: rgba(33,150,243,0.15);
            padding:15px;
            border-left:6px solid #2196F3;
            border-radius:10px;
            margin-bottom:10px;">
            
            <b>🚚 In Progress</b><br>
            📍 {r['Location']}<br>
            🍽 Meals: {r['Meals']}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style="
            background: rgba(255,193,7,0.15);
            padding:15px;
            border-left:6px solid #FFC107;
            border-radius:10px;
            margin-bottom:10px;">
            
            <b>⏳ Waiting for Restaurant</b><br>
            📍 {r['Location']}<br>
            🍽 Meals: {r['Meals']}
        </div>
        """, unsafe_allow_html=True)