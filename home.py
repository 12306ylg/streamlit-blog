import time
import streamlit as st
import os
import config
def close():
    st.session_state["is_show"] = False
    print("关闭", st.session_state["is_show"])

def show_content(item: str):
    st.session_state["is_show"] = True
    print("打开", item, st.session_state["is_show"])
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
        st.video(content.name) if st.checkbox(f"播放{content.name}") else None
    elif content.name.endswith(".mp3"):
        st.audio(content.name) if st.checkbox(f"播放{content.name}") else None
    st.button("关闭",on_click=close)

def head():
    st.header("HomePage!")
    st.info(time.ctime())
    st.info("page is in home.py")


def body():
    directory = os.listdir("./blog")
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
        image=item.split(".")[0]+".png" \
        if os.path.isfile(f"./blog/{item.split('.')[0]}.png") else item.split(".")[0]+".jpg" \
        if os.path.isfile(f"./blog/{item.split('.')[0]}.jpg") else item.split(".")[0]+".gif" \
        if os.path.isfile(f"./blog/{item.split('.')[0]}.gif") else None
        if image:st.image(f"./blog/{item}",width=200)
        st.markdown(f"**{"".join(open(f"./blog/{item}", 'r', encoding='utf-8',errors='ignore').read().splitlines()[:1])[:100]}……**")
        st.button("Read", on_click=show_content, args=(item,), key=item)
    show(file)
    for item in dirs:
        with st.expander(item):
            show([f"./{item}/"+i for i in os.listdir(f"./blog/{item}")])
                    


