import streamlit as st
from utils.data_manager import get_notifications   # ✅ ADDED

# ---------------- CSS (FINAL POLISH) ----------------
st.markdown("""
<style>

/* Smooth animation */
@keyframes fadeIn {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}

/* HERO */
.hero {
    text-align:center;
    padding:90px 20px;
    background: rgba(255,255,255,0.05);
    border-radius:25px;
    backdrop-filter: blur(12px);
    animation: fadeIn 1s ease-in-out;
}

.hero-title {
    font-size:72px;
    font-weight:900;
    background: linear-gradient(90deg,#4CAF50,#a1ffce);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* SECTION TITLE */
.section-title {
    text-align:center;
    font-size:42px;
    margin:50px 0 30px;
    font-weight:700;
    color:#81C784;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.1);
    transition:0.4s;
    height:100%;
}

/* Hover effect */
.card:hover {
    transform: translateY(-12px) scale(1.03);
    border: 1px solid #4CAF50;
    box-shadow: 0px 20px 50px rgba(0,0,0,0.5);
}

/* Notification */
.notify {
    background: rgba(76,175,80,0.2);
    padding:15px;
    border-left:6px solid #4CAF50;
    border-radius:10px;
    margin:10px 0;
}

/* Image style */
img {
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <div class="hero-title">Smart Food Rescue</div>
    <p style="font-size:22px;">Turning surplus food into hope 🍲</p>
</div>
""", unsafe_allow_html=True)

# 🔥 ---------------- LOGIN / SIGNUP BUTTONS ---------------- 🔥
col1, col2, col3 = st.columns([1,1,1])

with col2:
    b1, b2 = st.columns(2)

    with b1:
        if st.button("🔐 Login"):
            st.session_state.page = "login"
            st.switch_page("App.py")

    with b2:
        if st.button("📝 Sign Up"):
            st.session_state.page = "login"
            st.switch_page("App.py")

# ---------------- IMAGE + TEXT ----------------
col1, col2 = st.columns([1,1], gap="large")

with col1:
    st.image("https://images.unsplash.com/photo-1593113598332-cd288d649433")

with col2:
    st.markdown("### 🌍 Why this matters?")
    st.write("""
Food waste and hunger exist together — and that’s the problem we solve.  
We connect **restaurants, NGOs, and volunteers** into one smart system.
""")
    st.success("🔥 200+ meals rescued today!")

# ---------------- FEATURE CARDS ----------------
st.markdown('<div class="section-title">✨ Platform Highlights</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09" width="100%">
        <h4>🍱 Smart Donation</h4>
        <p>Post surplus food with expiry & urgency tracking.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1584515933487-779824d29309" width="100%">
        <h4>🏥 NGO Network</h4>
        <p>NGOs quickly accept and distribute food.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c" width="100%">
        <h4>❤️ Community Impact</h4>
        <p>Reducing waste while helping people.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- IMPACT ----------------
st.markdown('<div class="section-title">🌟 Real Impact</div>', unsafe_allow_html=True)

e1, e2 = st.columns(2, gap="large")

with e1:
    st.image("https://images.unsplash.com/photo-1606787366850-de6330128bfc")

with e2:
    st.image("https://images.unsplash.com/photo-1509099836639-18ba1795216d")

# ---------------- METRICS ----------------
st.markdown('<div class="section-title">📊 Live Impact</div>', unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Meals Saved 🍽", "1,240", "+120 today")

with m2:
    st.metric("NGOs Connected 🏥", "35", "+3 new")

with m3:
    st.metric("Volunteers 🤝", "120", "+10 today")

# ---------------- NOTIFICATIONS ----------------
st.markdown('<div class="section-title">🔔 Notifications</div>', unsafe_allow_html=True)

# ✅ NEW LOGIC (CONNECTED TO DATA MANAGER)
user_role = st.session_state.get("role", "")

notes = get_notifications(user_role)

if not notes:
    st.info("No updates yet")
else:
    for n in reversed(notes):
        st.markdown(f'<div class="notify">{n["message"]}</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align:center; margin-top:50px; font-size:20px; opacity:0.8;">
"Food is not waste until we waste it."
</div>
""", unsafe_allow_html=True)