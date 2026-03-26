import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Analytics", layout="wide")

# ---------------- THEME (WHITE + BLACK TEXT + BLOCK HEADINGS) ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #ffffff;
}

/* TEXT */
h1, h2, h3, h4, p, label {
    color: #000000 !important;
}

/* HEADINGS IN BLOCK LETTERS */
h1, h2, h3, h4 {
    text-transform: uppercase;
    font-weight: 900;
}

/* METRIC BOX */
[data-testid="metric-container"] {
    background-color: #f5f5f5;
    border-radius: 12px;
    padding: 15px;
    color: black;
}

/* TABLE */
[data-testid="stDataFrame"] {
    background-color: #ffffff;
    border-radius: 10px;
    color: black;
}

/* SUBHEADERS */
.css-10trblm {
    color: #000000 !important;
    font-weight: 900;
    text-transform: uppercase;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📊 ANALYTICS DASHBOARD")

# ---------------- SESSION ----------------
if "donations" not in st.session_state:
    st.session_state.donations = []

# ---------------- LOAD DATA ----------------
df = pd.DataFrame(st.session_state.donations)

# ---------------- EMPTY CHECK ----------------
if df.empty:
    st.warning("⚠ NO DONATION DATA AVAILABLE. PLEASE ADD DATA FIRST.")

else:
    # Clean column names
    df.columns = df.columns.str.strip().str.title()

    # ---------------- KPIs ----------------
    total_donations = len(df)
    total_meals = df["Meals"].sum() if "Meals" in df.columns else 0
    total_restaurants = df["Restaurant"].nunique() if "Restaurant" in df.columns else 0
    total_locations = df["Location"].nunique() if "Location" in df.columns else 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🍱 TOTAL DONATIONS", total_donations)
    col2.metric("🍽 MEALS SAVED", total_meals)
    col3.metric("🏪 RESTAURANTS", total_restaurants)
    col4.metric("📍 LOCATIONS", total_locations)

    st.markdown("---")

    # ---------------- BAR CHART ----------------
    if "Restaurant" in df.columns and "Quantity" in df.columns:
        st.subheader("📊 FOOD QUANTITY BY RESTAURANT")
        rest_data = df.groupby("Restaurant")["Quantity"].sum()
        st.bar_chart(rest_data)

    # ---------------- CATEGORY ----------------
    if "Category" in df.columns:
        st.subheader("🥧 FOOD CATEGORY DISTRIBUTION")
        cat_data = df["Category"].value_counts()
        st.bar_chart(cat_data)

    # ---------------- LOCATION ----------------
    if "Location" in df.columns:
        st.subheader("📍 DONATIONS BY LOCATION")
        loc_data = df["Location"].value_counts()
        st.bar_chart(loc_data)

    # ---------------- TOP DONORS ----------------
    if "Restaurant" in df.columns and "Meals" in df.columns:
        st.subheader("🏆 TOP DONATING RESTAURANTS")
        top = df.groupby("Restaurant")["Meals"].sum().sort_values(ascending=False)
        st.dataframe(top)

    # ---------------- TIME ANALYTICS ----------------
    if "Time" in df.columns and "Meals" in df.columns:
        st.subheader("🕒 DONATIONS OVER TIME")

        df["Time"] = pd.to_datetime(df["Time"], errors='coerce')
        df = df.dropna(subset=["Time"])

        if not df.empty:
            time_data = df.groupby(df["Time"].dt.date)["Meals"].sum()
            st.line_chart(time_data)

    # ---------------- DATA TABLE ----------------
    st.subheader("📋 ALL DONATIONS DATA")

    if "Time" in df.columns:
        st.dataframe(df.sort_values(by="Time", ascending=False))
    else:
        st.dataframe(df)