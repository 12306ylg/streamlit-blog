import streamlit as st
import home
import about
import admin
from config import demo_mode,lang
if not st.session_state.get("is_show", False):
    if demo_mode:st.info("IS DEMO OR THE CONFIG \"demo_mode\" is True", icon="🧪")
    st.title("Streamlit Blog(example)")
    st.button("Refresh")
    tabs = st.tabs(["home", "about","admin"])
    with tabs[0]:
        home.head()
        home.body()
    with tabs[1]:
        about.about()
    with tabs[2]:
        pas=st.text_input("Enter admin password:", type="password")
        if pas and not st.session_state.get("is_show", False):
            admin.admin(pas)