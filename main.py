import streamlit as st
import home
import about
import admin
from config import demo_mode,lang
lang=lang.main
if not st.session_state.get("is_show"):
    if demo_mode:st.info(lang["demo_tip"], icon="🧪")
    st.title(lang["title"])
    st.button(lang["rfsh"])
    tabs = st.tabs(lang["tabs"])
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