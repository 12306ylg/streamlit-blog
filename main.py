import streamlit as st
import home
import about
import admin
from config import is_in_streamlitcloud
if not st.session_state.get("is_show", False):
    if is_in_streamlitcloud:st.info("IS IN STREAMLIT CLOUD? OR THE CONFIG \"is_in_streamlitcloud\" IS True", icon="🧪")
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
