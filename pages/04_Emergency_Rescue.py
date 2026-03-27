import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

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

# ================= LOGOUT =================
col1, col2, col3 = st.columns([8,1,1])
with col3:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("app.py")

# ================= SESSION =================
if "requests" not in st.session_state:
    st.session_state.requests = []

if "volunteer_notifications" not in st.session_state:
    st.session_state.volunteer_notifications = []

# ================= TITLE =================
st.title("🚨 Emergency Rescue System")

# =========================================================
# 🏥 NGO
# =========================================================
if st.session_state.get("role") == "NGO":

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
            "Restaurant_Name": "Not Assigned",
            "Volunteer_Assigned": "Not Assigned",
            "Delivered": "No",
            "Rating": None,
            "Time": datetime.now().strftime("%H:%M")
        })
        st.success("✅ Sent to Restaurant!")

# =========================================================
# 🍱 RESTAURANT
# =========================================================
elif st.session_state.get("role") == "Restaurant":

    st.subheader("🍱 Restaurant Panel")

    for i, r in enumerate(st.session_state.requests):

        st.write(f"📍 {r['Location']} | 🍽 {r['Meals']} meals")

        if r["Restaurant_Response"] == "Pending":

            col1, col2 = st.columns(2)

            if col1.button(f"✅ Accept {i}"):

                st.session_state.requests[i]["Restaurant_Response"] = "Accepted"
                st.session_state.requests[i]["Status"] = "Food Ready"
                st.session_state.requests[i]["Restaurant_Name"] = st.session_state.get("user")

                # 🔔 Notification
                st.session_state.volunteer_notifications.append({
                    "message": f"🍱 Pickup from {st.session_state.get('user')} ({r['Meals']} meals) at {r['Location']}"
                })

                st.success("✅ Accepted & Notified Volunteers")
                st.rerun()

            if col2.button(f"❌ Reject {i}"):

                st.session_state.requests[i]["Restaurant_Response"] = "Rejected"
                st.session_state.requests[i]["Status"] = "Rejected"
                st.rerun()

# =========================================================
# 🚚 VOLUNTEER
# =========================================================
elif st.session_state.get("role") == "Volunteer":

    st.subheader("🚚 Volunteer Panel")

    # 🔔 Notifications
    st.subheader("🔔 Notifications")
    if st.session_state.volunteer_notifications:
        for n in reversed(st.session_state.volunteer_notifications):
            st.info(n["message"])
    else:
        st.info("No notifications")

    # 📦 Tasks
    st.subheader("📦 Pickup Tasks")

    for i, r in enumerate(st.session_state.requests):

        if r["Restaurant_Response"] == "Accepted" and r["Delivered"] == "No":

            st.write(f"""
📍 Location: {r['Location']}  
🍽 Meals: {r['Meals']}  
🏨 Hotel: {r.get('Restaurant_Name')}  
👤 Assigned: {r.get('Volunteer_Assigned')}
""")

            # ✅ ACCEPT TASK FIRST
            if r.get("Volunteer_Assigned") == "Not Assigned":
                if st.button(f"🙋 Accept Task {i}"):
                    st.session_state.requests[i]["Volunteer_Assigned"] = st.session_state.get("user")
                    st.rerun()

            # 🚚 DELIVERY
            if r.get("Volunteer_Assigned") == st.session_state.get("user"):
                if st.button(f"🚚 Pick Up & Deliver {i}"):

                    st.session_state.requests[i]["Delivered"] = "Yes"
                    st.session_state.requests[i]["Status"] = "Completed"

                    st.success("🎉 Delivered Successfully!")
                    st.rerun()

# =========================================================
# ⭐ RATING SYSTEM
# =========================================================
st.markdown("---")
st.subheader("⭐ Rate Deliveries")

for i, r in enumerate(st.session_state.requests):

    if r.get("Delivered") == "Yes" and r.get("Rating") is None:

        st.write(f"📍 {r['Location']} | 👤 {r.get('Volunteer_Assigned')}")

        rating = st.slider(f"Rate Delivery {i}", 1, 5)

        if st.button(f"Submit Rating {i}"):
            st.session_state.requests[i]["Rating"] = rating
            st.success("⭐ Rating Submitted!")
            st.rerun()

# =========================================================
# 📊 STATUS
# =========================================================
st.markdown("---")
st.subheader("📋 Request Status")

for r in st.session_state.requests:

    if r["Delivered"] == "Yes":
        st.success(f"""
✅ Completed  
📍 {r['Location']}  
🍽 {r['Meals']} meals  
👤 Volunteer: {r.get('Volunteer_Assigned')}  
⭐ Rating: {r.get('Rating', 'Not Rated')}
""")

    elif r["Restaurant_Response"] == "Rejected":
        st.error(f"❌ Rejected - {r['Location']}")

    elif r["Restaurant_Response"] == "Accepted":
        st.info(f"🚚 In Progress - {r['Location']} | 🏨 {r.get('Restaurant_Name')}")

    else:
        st.warning(f"⏳ Waiting - {r['Location']}")