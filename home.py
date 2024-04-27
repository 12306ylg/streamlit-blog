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
    content_f = open("./blog/" + item, "r", encoding="utf-8")
    content = content_f.read()
    st.markdown(f":gray[total:{len(content)}]")
    if content_f.name.endswith(".py"):
        exec(content)
    elif content_f.name.endswith(".md"):
        st.markdown(content)
    elif content_f.name.endswith(".txt"):
        st.text(content)
    elif content_f.name.endswith(".html"):
        st.write(content, unsafe_allow_html=True)
    elif content_f.name.endswith(".mp4"):
        st.video(content_f.name) if st.checkbox(f"Play{content.name}") else None
    elif content_f.name.endswith(".mp3"):
        st.audio(content_f.name) if st.checkbox(f"Play{content.name}") else None
    cls=lambda: close();content_f.close()
    st.button("Close",on_click=cls)

def head():
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
                    


