import os
import streamlit as st
import config
import shutil
def about():
    st.header("About")
    st.write("This is a simple blog application built using Python and Streamlit.")
    st.write("这是一个使用Python和Streamlit构建的简单博客应用程序。")
    with st.expander("Read More"):
        st.write("This application based MIT license and is open-sourced on GitHub.")
        st.write("这个应用程序基于MIT许可证，并在GitHub上开源。")
        st.write("GitHub: https://github.com/12306ylg/streamlit-blog/")
    st.write("---")
def preview(type,text):
    st.write("## Preview")
    st.markdown("---")
    with st.container(border=True):
     if type == "md":
        st.markdown(text)
     elif type == "txt":
        st.write(text)
     elif type == "html":
        st.markdown(text, unsafe_allow_html=True)
     elif type == "python":
        st.warning("NOT SAFE FOR EXECUTION")
        st.code(text, language="python")
def post(title,type,text):
    type="py" if type=="python" else type
    open(f"./blog/{title}.{type}", "w").write(text)
    st.success("Post added successfully")
def delete(title):
    def rmdir():
        shutil.rmtree(f"./blog/{title}")
        st.success("Directory deleted successfully")
    path=f"./blog/{title}"
    if os.path.isfile(path):os.remove(path);st.success("Post deleted successfully")
    elif os.path.isdir(path):
        st.warning("This is a directory, press the button below to delete it or open your file manager to delete posts in this directory.")
        st.button("Delete ALL Post on this directory",on_click=rmdir)
    else:raise Exception("Huhh???")
def admin(password:str):
    if password == config.password:
        st.write("Admin Page")
        st.write("管理员页面")
        st.write("---")
        choice=st.radio("Choose an action", ["Add Post","Delete Post"],key="action")
        if choice == "Add Post":
            title=st.text_input("Title",key="title")
            type=st.selectbox("Type",["md","txt","html","python"],key="type")
            text=st.text_area("Text",key="text")
            if text!="":preview(type,text)
            st.button("Add Post",on_click=post,args=(title,type,text))
        elif choice == "Delete Post":
            title=st.selectbox("Title",os.listdir("./blog"),key="title")
            st.button("Delete Post",on_click=delete,args=(title,))
    else:
        st.error("Incorrect password")
        
