import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
from utils.data_manager import get_notifications
import pydeck as pdk
import urllib.parse

st.set_page_config(page_title="Volunteer", layout="wide")

# ---------------- SESSION ----------------
if "requests" not in st.session_state:
    st.session_state.requests = []

if "volunteers" not in st.session_state:
    st.session_state.volunteers = []

# =========================================================
# 🔐 FIXED SECURITY (ROLE ISSUE SOLVED)
# =========================================================
role = st.session_state.get("role")

if not role:
    st.warning("⚠️ Please login first")
    st.stop()

if role.strip().lower() != "volunteer":
    st.error(f"❌ Access denied for role: {role}")
    st.stop()

# ---------------- HEADER ----------------
st.title("🤝 Volunteer Dashboard")

# ---------------- LOGOUT ----------------
col1, col2 = st.columns([8,1])
with col2:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("app.py")

# =========================================================
# 📝 VOLUNTEER REGISTRATION
# =========================================================
st.subheader("📝 Register as Volunteer")

with st.form("volunteer_form"):
    name = st.text_input("👤 Name")
    phone = st.text_input("📞 Phone")
    area = st.text_input("📍 Area")

    submit = st.form_submit_button("Register")

if submit:
    if name and phone and area:
        st.session_state.volunteers.append({
            "Name": name,
            "Phone": phone,
            "Area": area,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        st.session_state.user = name
        st.session_state.role = "Volunteer"   # ✅ ENSURE ROLE SET CORRECTLY
        st.success("✅ Registered successfully!")
    else:
        st.error("⚠️ Please fill all fields")

# =========================================================
# 📍 LIVE LOCATION
# =========================================================
st.subheader("📍 Your Live Location")

components.html("""
<!DOCTYPE html>
<html>
<body>
<p id="location">Fetching location...</p>

<script>
navigator.geolocation.getCurrentPosition(
    function(position) {
        document.getElementById("location").innerHTML =
        "Latitude: " + position.coords.latitude + 
        "<br>Longitude: " + position.coords.longitude;
    },
    function(error) {
        document.getElementById("location").innerHTML =
        "Location access denied.";
    }
);
</script>
</body>
</html>
""", height=150)

# =========================================================
# 🗺 MAP
# =========================================================
st.subheader("🗺 Live Delivery Map")

map_data = pd.DataFrame({
    "lat": [13.0827],
    "lon": [80.2707]
})

layer = pdk.Layer(
    "ScatterplotLayer",
    data=map_data,
    get_position='[lon, lat]',
    get_color=[0, 200, 0],
    get_radius=200,
)

view_state = pdk.ViewState(
    latitude=13.0827,
    longitude=80.2707,
    zoom=11
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# =========================================================
# 🔔 NOTIFICATIONS (FIXED MAP LINK)
# =========================================================
st.subheader("🔔 Pickup Notifications")

notes = []

try:
    external_notes = get_notifications("volunteer") or []
    notes.extend(external_notes)
except:
    pass

for r in st.session_state.requests:
    if r.get("Restaurant_Response") == "Accepted" and r.get("Delivered") == "No":
        notes.append({
            "restaurant": r.get("Restaurant_Name", "Unknown Restaurant"),
            "location": r.get("Location"),
            "meals": r.get("Meals", 0)
        })

if notes:
    for n in reversed(notes):

        restaurant = n.get("restaurant", "Food Ready")
        location = n.get("location")
        meals = n.get("meals", 0)

        if location and str(location).strip():
            encoded_location = urllib.parse.quote(str(location))
            google_map_url = f"https://www.google.com/maps/search/?api=1&query={encoded_location}"
            map_link = f"🔗 [Open Live Map]({google_map_url})"
        else:
            map_link = "⚠️ Location not available"

        st.info(f"""
🍱 {restaurant}  
📍 Location: {location if location else 'Not provided'}  
🍽 Meals: {meals}  
{map_link}
        """)

else:
    st.info("No pickup notifications yet")

# =========================================================
# 🚚 DELIVERY TASKS
# =========================================================
st.subheader("🚚 Delivery Tasks")

task_found = False

for i, r in enumerate(st.session_state.requests):

    if r.get("Restaurant_Response") == "Accepted" and r.get("Delivered") == "No":

        task_found = True

        st.write(f"""
        📍 Location: {r.get('Location')}  
        🍽 Meals: {r.get('Meals')}  
        🏨 Restaurant: {r.get('Restaurant_Name')}
        """)

        if st.button(f"🚚 Deliver Order {i}"):

            st.session_state.requests[i]["Delivered"] = "Yes"
            st.session_state.requests[i]["Status"] = "Completed"
            st.session_state.requests[i]["Volunteer_Name"] = st.session_state.get("user")

            st.success("✅ Delivered successfully!")
            st.rerun()

if not task_found:
    st.info("No delivery tasks available")

# =========================================================
# 📦 COMPLETED DELIVERIES
# =========================================================
st.subheader("📦 Completed Deliveries")

for r in st.session_state.requests:
    if r.get("Delivered") == "Yes":
        st.success(f"""
        ✅ Delivered by: {r.get('Volunteer_Name', 'Unknown')}  
        📍 {r.get('Location')}  
        🍽 {r.get('Meals')} meals
        """)