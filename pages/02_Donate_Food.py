import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

# ================= SESSION =================
if "donations" not in st.session_state:
    st.session_state.donations = []

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {}

# 👉 ADD THIS (IMPORTANT FOR SYSTEM FLOW)
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
        <span class="page-name">DONATE FOOD</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"### 👋 Welcome, {st.session_state.get('user')}!")

# ================= LOGOUT =================
col1, col2, col3 = st.columns([8,1,1])
with col3:
    if st.button("🚪 Logout", key="logout_nav_final"):
        st.session_state.user = None
        st.session_state.role = None
        st.switch_page("app.py")

# ================= SECURITY =================
if st.session_state.get("role") != "Restaurant":
    st.error("❌ Only Restaurant users allowed")
    st.stop()

# ================= UI =================
st.markdown("""
<style>
.title {
    font-size:42px;
    font-weight:900;
    text-align:center;
    color:#4CAF50;
}
.card {
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:15px;
    margin-bottom:10px;
}
.pending {color:orange;}
.accepted {color:#4CAF50;}
.completed {color:cyan;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🍱 Donate Food</div>', unsafe_allow_html=True)

# ================= FORM =================
st.subheader("➕ Add Donation")

with st.form("donate_form"):
    col1, col2 = st.columns(2)

    with col1:
        hotel = st.text_input("🏨 Hotel Name")
        food = st.text_input("🍲 Food Item")
        qty = st.number_input("🍽 Meals", min_value=1)

    with col2:
        serving = st.number_input("👥 Serving per Meal", min_value=1)
        expiry = st.slider("⏱ Expiry Time (hrs)", 1, 24)
        address = st.text_area("📍 Pickup Address")
        contact = st.text_input("📞 Contact Number")

    submit = st.form_submit_button("🚀 Submit")

# ================= SAVE =================
if submit:
    if not hotel or not food or not address or not contact:
        st.error("⚠️ Fill all fields")

    elif not contact.isdigit() or len(contact) != 10:
        st.error("⚠️ Enter valid 10-digit contact number")

    else:
        urgency = "High" if expiry <= 4 else "Medium" if expiry <= 10 else "Low"

        donation = {
            "Hotel": hotel,
            "User": st.session_state.get("user"),
            "Food": food,
            "Qty": qty,
            "Serving": serving,
            "Expiry": expiry,
            "Urgency": urgency,
            "Address": address,
            "Contact": contact,
            "Status": "Pending",
            "Accepted_By": "Waiting",
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        st.session_state.donations.append(donation)

        # leaderboard update
        st.session_state.leaderboard[hotel] = \
            st.session_state.leaderboard.get(hotel, 0) + int(qty)

        st.success("✅ Donation submitted!")

# ================= FILTER =================
st.subheader("📦 Your Donations")

filter_status = st.selectbox(
    "Filter",
    ["All", "Pending", "Accepted", "Completed"]
)

# ================= DISPLAY =================
found = False

for d in reversed(st.session_state.donations):

    if d.get("User") == st.session_state.get("user"):

        if filter_status != "All" and d.get("Status") != filter_status:
            continue

        found = True
        status_class = d.get("Status", "").lower()

        st.markdown(f"""
        <div class="card">
        🏨 <b>{d.get('Hotel')}</b><br>
        🍱 {d.get('Food')}<br>
        🍽 Meals: {d.get('Qty')}<br>
        👥 Serving: {d.get('Serving')}<br>
        ⏱ Expiry: {d.get('Expiry')} hrs<br>
        ⚡ Urgency: {d.get('Urgency')}<br>
        📍 {d.get('Address')}<br>
        📞 {d.get('Contact')}<br><br>
        🕒 {d.get('Time')}<br>
        📌 Status: <span class="{status_class}">{d.get('Status')}</span><br>
        🤝 Accepted By: {d.get('Accepted_By')}
        </div>
        """, unsafe_allow_html=True)

if not found:
    st.info("No donations yet")

# ================= SUMMARY =================
st.subheader("📊 Summary")

user_data = [
    d for d in st.session_state.donations
    if d.get("User") == st.session_state.get("user")
]

total = len(user_data)
completed = len([d for d in user_data if d.get("Status") == "Completed"])

col1, col2 = st.columns(2)

col1.metric("Total Donations", total)
col2.metric("Completed", completed)