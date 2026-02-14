import streamlit as st
from vulnerability_scanner.sql_scanner import scan_sql
from vulnerability_scanner.xss_scanner import scan_xss
from password_strength_ai.password_ai import check_password_strength

st.title("🛡 Cyber Security Dashboard")

tab1, tab2, tab3 = st.tabs([
    "Vulnerability Scanner",
    "Password Analyzer",
    "IDS Alerts"
])

# ---------------- SCANNER ----------------
with tab1:
    st.header("Website Vulnerability Scanner")

    url = st.text_input("Enter Website URL")

    if st.button("Scan Website"):
        if not url.startswith("http"):
            url = "https://" + url

        st.subheader("SQL Injection Result")
        st.write(scan_sql(url))

        st.subheader("XSS Result")
        st.write(scan_xss(url))

# ---------------- PASSWORD ----------------
with tab2:
    st.header("Password Strength Checker")

    pwd = st.text_input("Enter Password", type="password")

    if st.button("Check Strength"):
        st.write(check_password_strength(pwd))

# ---------------- IDS ----------------
# ---------------- IDS ----------------
import os

with tab3:
    st.header("Network Intrusion Alerts")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(BASE_DIR, "ids_log.txt")

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            logs = f.read()

        if logs.strip():
            st.text(logs)
        else:
            st.info("No alerts detected")
    else:
        st.warning("IDS log file not found")

