import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# ---------------- THEME (BLACK MODERN) ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

/* TITLE */
h1 {
    text-align: center;
    font-weight: 900;
    color: #4CAF50;
}

/* HEADINGS */
h2, h3 {
    color: #ffffff;
    font-weight: 800;
}

/* CARD DESIGN */
.card {
    background: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #4CAF50;
    margin-top: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
}

/* IMAGE */
img {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🍱 Smart Food Waste Redistribution System")

# ---------------- HERO IMAGE ----------------
st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836", use_container_width=True)

# ---------------- PROJECT OVERVIEW ----------------
col1, col2 = st.columns([1,1])

with col1:
    st.image("https://images.unsplash.com/photo-1606787366850-de6330128bfc")

with col2:
    st.markdown("""
    <div class="card">
    <h3>🌍 Project Overview</h3>
    <p>
    A smart platform that connects <b>Restaurants, NGOs, and Volunteers</b> 
    to reduce food waste and help needy people in real-time.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PROBLEM ----------------
col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    <div class="card">
    <h3>❗ Problem</h3>
    <p>
    Food is wasted daily while many people go hungry.
    There is no fast system to redistribute surplus food.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1488521787991-ed7bbaae773c")

# ---------------- SOLUTION ----------------
col1, col2 = st.columns([1,1])

with col1:
    st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d")

with col2:
    st.markdown("""
    <div class="card">
    <h3>💡 Solution</h3>
    <p>
    • Restaurants donate food  
    • NGOs manage requests  
    • Volunteers deliver food  
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- WORKFLOW ----------------
st.markdown("""
<div class="card">
<h3>🔄 Workflow</h3>
<p>
1️⃣ Restaurant uploads food <br>
2️⃣ NGO sends request <br>
3️⃣ Restaurant accepts <br>
4️⃣ Volunteer gets notification <br>
5️⃣ Delivery completed
</p>
</div>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca")

# ---------------- FEATURES ----------------
col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    <div class="card">
    <h3>🚀 Features</h3>
    <p>
    ✔ Donation system <br>
    ✔ Emergency rescue <br>
    ✔ Notifications <br>
    ✔ Analytics dashboard
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d")

# ---------------- USERS ----------------
st.markdown("""
<div class="card">
<h3>👥 User Roles</h3>
<p>
🏨 Restaurant – Donates food <br>
🏥 NGO – Manages requests <br>
🚚 Volunteer – Delivers food
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- TECHNOLOGY ----------------
col1, col2 = st.columns([1,1])

with col1:
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475")

with col2:
    st.markdown("""
    <div class="card">
    <h3>💻 Technology</h3>
    <p>
    • Python <br>
    • Streamlit <br>
    • Session State <br>
    • HTML + CSS
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- IMPACT ----------------
st.image("https://images.unsplash.com/photo-1529156069898-49953e39b3ac")

st.markdown("""
<div class="card">
<h3>🌟 Impact</h3>
<p>
✔ Reduces food wastage <br>
✔ Helps needy people <br>
✔ Promotes sustainability
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FINAL MESSAGE ----------------
st.markdown("""
<div style="text-align:center; margin-top:40px; font-size:20px; font-weight:bold;">
🌍 "Don't waste food — share it, save lives."
</div>
""", unsafe_allow_html=True)