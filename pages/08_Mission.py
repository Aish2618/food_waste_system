import streamlit as st

st.set_page_config(page_title="Mission", layout="wide")

# ---------------- THEME (PURE WHITE) ----------------
st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
    color: #000000;
}

/* MAIN TITLE */
h1 {
    font-weight: 900;
    color: #000000;
    text-align: center;
}

/* SECTION HEADINGS */
h2, h3 {
    font-weight: 800;
    color: #000000;
}

/* Highlight box */
.highlight {
    background: #f9f9f9;
    padding: 15px;
    border-left: 6px solid #000000;
    border-radius: 10px;
    margin-top: 10px;
    font-size: 16px;
}

/* Image style (medium size) */
img {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎯 Mission, Vision & Objectives")

# Function for medium image
def show_image(url):
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(url, use_container_width=True)

# ---------------- MISSION ----------------
st.subheader("🌍 Our Mission")
show_image("https://images.unsplash.com/photo-1606787366850-de6330128bfc")

st.write("""
Our mission is to reduce food wastage and ensure that surplus food reaches those in need 
quickly and efficiently. We connect donors, NGOs, and volunteers through a smart platform.
""")

st.markdown("""
<div class="highlight">
⭐ <b>Key Point:</b> Every extra meal can save a life — don’t waste, donate.
</div>
""", unsafe_allow_html=True)

# ---------------- VISION ----------------
st.subheader("🔭 Our Vision")
show_image("https://images.unsplash.com/photo-1509099836639-18ba1795216d")

st.write("""
We envision a world where no food is wasted and no one goes hungry. 
We aim to build a sustainable system where sharing food becomes a habit.
""")

st.markdown("""
<div class="highlight">
⭐ <b>Key Point:</b> A hunger-free world is possible together.
</div>
""", unsafe_allow_html=True)

# ---------------- OBJECTIVES ----------------
st.subheader("🎯 Our Objectives")
show_image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d")

st.write("""
• Reduce food wastage  
• Deliver surplus food quickly  
• Connect people in real-time  
• Ensure safe food distribution  
""")

st.markdown("""
<div class="highlight">
⭐ <b>Key Point:</b> Fast action prevents food spoilage.
</div>
""", unsafe_allow_html=True)

# ---------------- CORE VALUES ----------------
st.subheader("💡 Core Values")
show_image("https://images.unsplash.com/photo-1529156069898-49953e39b3ac")

st.write("""
• Compassion  
• Sustainability  
• Collaboration  
• Integrity  
""")

st.markdown("""
<div class="highlight">
⭐ <b>Key Point:</b> Strong values create strong impact.
</div>
""", unsafe_allow_html=True)

# ---------------- WHY IT MATTERS ----------------
st.subheader("❗ Why This Matters")
show_image("https://images.unsplash.com/photo-1488521787991-ed7bbaae773c")

st.write("""
Millions face hunger while food is wasted daily. This platform helps balance that gap 
by redistributing food effectively.
""")

st.markdown("""
<div class="highlight">
⭐ <b>Key Point:</b> Saving food means saving lives.
</div>
""", unsafe_allow_html=True)