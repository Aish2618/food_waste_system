import streamlit as st

st.set_page_config(layout="wide")

# ================= SESSION =================
if "user" not in st.session_state:
    st.session_state.user = None
    st.session_state.role = None

# 👉 PAGE CONTROL
if "page" not in st.session_state:
    st.session_state.page = "home"

# 👉 LOCAL USER STORAGE
if "users" not in st.session_state:
    st.session_state.users = []

# ================= REDIRECT TO HOME =================
if st.session_state.page == "home":
    st.switch_page("pages/01_Home.py")   # ✅ FIXED

# ================= LOGIN PAGE =================
elif st.session_state.page == "login" and not st.session_state.user:

    st.title("🔐 Smart Food Rescue Login")

    tab1, tab2, tab3 = st.tabs(["Login", "Sign Up", "Forgot Password"])

    # ================= LOGIN =================
    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            found = False
            for user in st.session_state.users:
                if user["username"] == username and user["password"] == password:
                    st.session_state.user = username
                    st.session_state.role = user["role"]
                    found = True
                    st.success(f"Login successful as {user['role']} ✅")
                    st.rerun()

            if not found:
                st.error("Invalid username or password ❌")

    # ================= SIGN UP =================
    with tab2:
        new_user = st.text_input("Username", key="signup_user")
        new_pass = st.text_input("Password", type="password", key="signup_pass")
        role = st.selectbox("Role", ["Restaurant", "NGO", "Volunteer"])

        ngo_license = ""
        if role == "NGO":
            ngo_license = st.text_input("NGO License Number")

        if st.button("Sign Up"):
            if not new_user or not new_pass:
                st.error("Please fill all fields")
            else:
                st.session_state.users.append({
                    "username": new_user,
                    "password": new_pass,
                    "role": role,
                    "ngo_license": ngo_license if role == "NGO" else None
                })
                st.success(f"{role} account created successfully 🎉")

    # ================= FORGOT PASSWORD =================
    with tab3:
        user_reset = st.text_input("Enter Username", key="reset_user")
        new_password = st.text_input("New Password", type="password")

        if st.button("Reset Password"):
            found = False
            for user in st.session_state.users:
                if user["username"] == user_reset:
                    user["password"] = new_password
                    found = True
                    st.success("Password updated successfully 🔑")
                    break

            if not found:
                st.error("User not found ❌")

# ================= AFTER LOGIN =================
elif st.session_state.user:

    st.sidebar.success(f"👤 {st.session_state.user}")
    st.sidebar.write(f"Role: {st.session_state.role}")

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.session_state.page = "home"
        st.rerun()
    # 🔥 ROLE REDIRECT
    if st.session_state.role == "Restaurant":
        st.switch_page("pages/02_Donate_Food.py")   # ✅ FIXED

    elif st.session_state.role == "NGO":
        st.switch_page("pages/03_NGO_Dashboard.py")   # ✅ FIXED

    elif st.session_state.role == "Volunteer":
        st.switch_page("pages/05_Volunteers.py")   # ✅ FIXED