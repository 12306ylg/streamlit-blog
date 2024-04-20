import os
import streamlit as st
import config
import shutil
lang=config.lang.admin
def preview(type,text):
    st.write(f"## {lang["editor"][3]}")
    st.markdown("---")
    with st.container(border=True):
     if type == "md":
        st.markdown(text)
     elif type == "txt":
        st.write(text)
     elif type == "html":
        st.markdown(text, unsafe_allow_html=True)
     elif type == "python":
        st.warning(lang["msg"][1][1])
        st.code(text, language="python")
def post(title,type,text):
    type="py" if type=="python" else type
    open(f"./blog/{title}.{type}", "w").write(text)
    st.success(lang["msg"][0][0])
def delete(title):
    def rmdir():
        shutil.rmtree(f"./blog/{title}")
        st.success(lang["msg"][0][1])
    path=f"./blog/{title}"
    if os.path.isfile(path):os.remove(path);st.success(lang["msg"][0][2])
    elif os.path.isdir(path):
        st.warning(lang["msg"][1][0])
        st.button("Delete ALL Post on this directory",on_click=rmdir)
    else:raise Exception("Huhh???")
def build_PostIndex():
    ignore=set(open("./.index_ignore","r").read().splitlines())
    index=set([f for f in os.listdir("./blog")
            if f not in ignore if f!=""])
    open("./.index","w").writelines(index)
    return index
def PostIndex():
    return set(open("./.index","r").read().splitlines() if os.path.isfile("./.index") else build_PostIndex())
def admin(password:str):
    if password == config.password:
        st.write(lang["header"])
        st.write("---")
        choice=st.radio(lang["act"][0], lang["act"][1],key="action")
        if choice == lang["act"][1][0]:
            title=st.text_input(lang["editor"][0],key="title")
            type=st.selectbox(lang["editor"][1],["md","txt","html","python"],key="type")
            text=st.text_area(lang["editor"][2],key="text")
            if text!="":preview(type,text)
            st.button(lang["act"][1][0],on_click=post,args=(title,type,text))
        elif choice == lang["act"][1][1]:
            title=st.selectbox(lang["editor"][0],os.listdir("./blog"),key="title")
            st.button(lang["act"][1][1],on_click=delete,args=(title,))
    else:
        st.error(lang["msg"][2][0])
        
