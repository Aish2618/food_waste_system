import streamlit as st

# ================= SIDEBAR =================
st.sidebar.success(f"👤 {st.session_state.get('user')}")
st.sidebar.write(f"Role: {st.session_state.get('role')}")

if st.sidebar.button("Logout", key="logout_leaderboard"):
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# ================= UI =================
st.markdown("""
<style>
.title {
    font-size:40px;
    font-weight:900;
    text-align:center;
    margin-bottom:20px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding:15px;
    border-radius:12px;
    margin-bottom:10px;
    text-align:center;
}

/* Top 3 styles */
.rank1 {border:2px solid gold;}
.rank2 {border:2px solid silver;}
.rank3 {border:2px solid #cd7f32;}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<div class="title">🏆 Leaderboard</div>', unsafe_allow_html=True)

# ================= CHECK DATA =================
if "leaderboard" not in st.session_state or not st.session_state.leaderboard:
    st.info("No donations yet")
    st.stop()

# ================= SORT DATA =================
data = sorted(
    st.session_state.leaderboard.items(),
    key=lambda x: x[1],
    reverse=True
)

# ================= TOP 3 =================
st.subheader("🥇 Top Contributors")

top3 = data[:3]
cols = st.columns(3)

for i, (name, meals) in enumerate(top3):
    with cols[i]:
        st.markdown(f"""
        <div class="card rank{i+1}">
            <h3>#{i+1}</h3>
            🏨 {name}<br>
            🍽 {meals} meals
        </div>
        """, unsafe_allow_html=True)

# ================= FULL LIST =================
st.subheader("📊 Full Rankings")

for i, (name, meals) in enumerate(data, start=1):
    st.markdown(f"""
    <div class="card">
        <b>#{i}</b> — 🏨 {name} <br>
        🍽 Meals Donated: <b>{meals}</b>
    </div>
    """, unsafe_allow_html=True)

# ================= STATS =================
st.subheader("📈 Statistics")

total_donors = len(data)
total_meals = sum(meals for _, meals in data)

col1, col2 = st.columns(2)

col1.metric("Total Donors", total_donors)
col2.metric("Total Meals Donated", total_meals)

# ================= SEARCH =================
st.subheader("🔍 Search Donor")

search = st.text_input("Enter hotel name")

if search:
    found = False
    for i, (name, meals) in enumerate(data, start=1):
        if search.lower() in name.lower():
            found = True
            st.success(f"#{i} 🏨 {name} → 🍽 {meals} meals")

    if not found:
        st.error("No matching donor found")