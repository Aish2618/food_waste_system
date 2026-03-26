import streamlit as st

st.set_page_config(layout="wide")

# ================= SESSION =================
if "donations" not in st.session_state:
    st.session_state.donations = []

if "notifications" not in st.session_state:
    st.session_state.notifications = []

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
    if st.button("🚪 Logout", key="logout_ngo"):
        st.session_state.user = None
        st.session_state.role = None
        st.switch_page("app.py")

# ================= SECURITY =================
if st.session_state.get("role") != "NGO":
    st.error("❌ Only NGO users can access this page")
    st.stop()

# ================= TITLE =================
st.subheader("🏥 NGO Dashboard")

# ================= DONATIONS =================
st.subheader("📦 Food Donations")

for i, d in enumerate(st.session_state.donations):

    st.write(f"""
    🏨 {d.get('Hotel')}  
    🍱 {d.get('Food')}  
    🍽 Meals: {d.get('Qty')}  
    📍 {d.get('Address')}  
    📌 Status: {d.get('Status')}  
    """)

    col1, col2 = st.columns(2)

    if d.get("Status") == "Pending":
        if col1.button("✅ Accept", key=f"accept_{i}"):
            st.session_state.donations[i]["Status"] = "Accepted"
            st.session_state.donations[i]["Accepted_By"] = st.session_state.get("user")
            st.rerun()

    elif d.get("Status") == "Accepted":
        if col2.button("📦 Complete", key=f"complete_{i}"):
            st.session_state.donations[i]["Status"] = "Completed"
            st.rerun()

# ================= MAP FUNCTION (REAL LOCATION) =================
def show_map(location_text):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={location_text}"

    st.markdown(f"""
    <a href="{maps_url}" target="_blank">
        <button style="
            background-color:#4CAF50;
            color:white;
            padding:8px 15px;
            border:none;
            border-radius:8px;
            cursor:pointer;">
            📍 Open Location in Google Maps
        </button>
    </a>
    """, unsafe_allow_html=True)

# ================= EMERGENCY =================
st.markdown("---")
st.subheader("🚨 Emergency Request")

with st.form("ngo_emergency"):
    location = st.text_input("📍 Location")
    meals = st.number_input("🍽 Meals Needed", min_value=1)

    submit = st.form_submit_button("Send to Restaurant")

if submit:
    st.session_state.requests.append({
        "Location": location,
        "Meals": meals,
        "Status": "Waiting for Restaurant",
        "Restaurant_Response": "Pending",
        "Restaurant_Name": "Not Assigned",
        "Delivered": "No"
    })

    st.success("✅ Sent to Restaurant!")

# ================= TRACK =================
st.subheader("📋 Emergency Tracking")

for r in st.session_state.requests:

    st.write(f"""
    📍 {r['Location']}  
    🍽 {r['Meals']} meals  
    📌 Status: {r['Status']}  
    🏨 Restaurant: {r['Restaurant_Name']}  
    🚚 Delivered: {r['Delivered']}  
    """)

    # ✅ REAL MAP BUTTON
    show_map(r['Location'])

# ================= SUMMARY =================
st.markdown("---")
st.subheader("📊 Summary")

c1, c2 = st.columns(2)

c1.metric("Total Donations", len(st.session_state.donations))
c2.metric(
    "Completed",
    len([d for d in st.session_state.donations if d.get("Status") == "Completed"])
)