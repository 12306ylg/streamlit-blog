import streamlit as st
from config import lang

def about():
    st.header(lang.about["header"])
    st.write(lang.about["description"])
    with st.expander(lang.about["read_more"]):
        st.write(lang.about["open_source"])
        st.markdown("![Github](https://badgen.net/badge/icon/GitHub?icon=github&label \"Github\")GitHub: https://github.com/12306ylg/streamlit-blog/")
    st.write("---")
