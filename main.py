import streamlit as st
import home
import about
import admin
from config import demo_mode,lang
if not st.session_state.get("is_show"):
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
if st.session_state.get("content") and st.session_state.get("is_show"):
    home.show_content(st.session_state["content"]) # type: ignore
    home.Comment.comment(st.session_state["content"]) # type: ignore
    home.Comment.show_comment(st.session_state["content"]) # type: ignore