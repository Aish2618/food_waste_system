import streamlit as st

st.set_page_config(page_title="Contact Us", layout="wide")

# ---------------- THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
    color: #000000;
}

/* TITLE */
h1 {
    font-weight: 900;
    color: #000000;
    text-align: center;
}

/* HEADINGS */
h2, h3 {
    font-weight: 800;
    color: #000000;
}

/* CARD STYLE */
.card {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid black;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-top: 10px;
}

/* IMAGE */
img {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("📞 Contact Smart Food Rescue")

# ---------------- IMAGE ----------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("https://images.unsplash.com/photo-1521791136064-7986c2920216", use_container_width=True)

# ---------------- INTRO ----------------
st.write("""
We would love to hear from you! Whether you are a restaurant willing to donate food,
an NGO seeking support, or a volunteer wanting to help the community,
feel free to reach out to us.
""")

st.markdown("""
<div class="card">
⭐ <b>We are here to connect, support, and serve the community.</b>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT INFO ----------------
st.subheader("📌 Contact Information")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        📧 <b>Email</b><br>
        support@smartfoodrescue.org
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        📞 <b>Phone</b><br>
        +91 9876543210
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        📍 <b>Address</b><br>
        Chennai, Tamil Nadu, India
    </div>
    """, unsafe_allow_html=True)

# ---------------- EXTRA IMAGE ----------------
st.subheader("🤝 Let's Connect")

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d")

with col2:
    st.image("https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca")

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align:center; margin-top:40px; font-size:18px;">
"Together we can reduce food waste and fight hunger."
</div>
""", unsafe_allow_html=True)