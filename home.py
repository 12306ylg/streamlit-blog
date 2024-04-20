import time
import streamlit as st
import os
import config
import admin
def close():
    st.session_state["is_show"] = False
def show_content(item: str):
    st.session_state["is_show"] = True
    st.image(config.icon,width=50)
    st.write(config.name,unsafe_allow_html=True)
    st.markdown("---")
    content = open("./blog/" + item, "r", encoding="utf-8")
    if content.name.endswith(".py"):
        exec(content.read()) if content.read().startswith("#!blog") else None
    elif content.name.endswith(".md"):
        st.markdown(content.read())
    elif content.name.endswith(".txt"):
        st.text(content.read())
    elif content.name.endswith(".html"):
        st.write(content.read(), unsafe_allow_html=True)
    elif content.name.endswith(".mp4"):
        st.video(content.name) if st.checkbox(f"Play{content.name}") else None
    elif content.name.endswith(".mp3"):
        st.audio(content.name) if st.checkbox(f"Play{content.name}") else None
    st.button("Close",on_click=close)

def head():
    """"""
    st.header("HomePage!")
    st.info(time.ctime())
    st.info("page is in home.py")


def body():
    directory = admin.PostIndex()#Get index of .index
    file: list[str] = []
    dirs: list[str] = []
    for item in directory:
        if os.path.isfile("./blog/" + item):
            file.append(item)
        else:
            dirs.append(item)
    def show(file: list[str]):
     for item in file:
        st.markdown("---")
        st.markdown(f"## {item.split(".")[0]}")
        #show cover image if it exists
        image=item.split(".")[0]+".png" \
        if os.path.isfile(f"./blog/{item.split('.')[0]}.png") else item.split(".")[0]+".jpg" \
        if os.path.isfile(f"./blog/{item.split('.')[0]}.jpg") else item.split(".")[0]+".gif" \
        if os.path.isfile(f"./blog/{item.split('.')[0]}.gif") else None
        #============================================
        if image:st.image(f"./blog/{item}",width=200)
        st.markdown(f"**{open(f"./blog/{item}",encoding="utf-8",errors="ignore").read(100)}……**")
        st.button("Read", on_click=show_content, args=(item,), key=item)
    show(file)
    for item in dirs:
        with st.expander(item):
            show([f"./{item}/"+i for i in os.listdir(f"./blog/{item}")])
                    


