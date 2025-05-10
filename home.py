import sys
import threading
import time
import streamlit as st
import os
import config
import admin
import random

def close():
    st.session_state["is_show"] = False

def handle_close(content_f):
    close()
    content_f.close()

def show_content(item: str):
    st.session_state["content"] = item
    st.session_state["is_show"] = True
    st.image(config.icon, width=50)
    st.write(config.name, unsafe_allow_html=True)
    st.markdown("---")
    content_f = open(f"./blog/{item}", "r", encoding="utf-8")
    content = content_f.read()
    st.markdown(f":gray[total:{len(content)}]")
    # Show content
    if content_f.name.endswith(".py"):
        exec(content)
    elif content_f.name.endswith(".md"):
        st.markdown(content)
    elif content_f.name.endswith(".txt"):
        st.text(content)
    elif content_f.name.endswith(".html"):
        st.write(content, unsafe_allow_html=True)
    elif content_f.name.endswith(".mp4"):
        if st.checkbox(f"Play {content_f.name}"):
            st.video(content_f.name)
    elif content_f.name.endswith(".mp3"):
        if st.checkbox(f"Play {content_f.name}"):
            st.audio(content_f.name)
    
    st.button("Close", 
              key=f"cls_{random.randint(1, sys.maxsize)}", 
              on_click=lambda: handle_close(content_f))

def setsssts(key,value):
    st.session_state[key]=value

class Comment:
    @staticmethod
    def comment(content:str):
        def submit(name:str,email:str,comment:str):
            if st.session_state.get("commeted"):
                st.error("You can only comment once per 10 seconds!")
                return
            elif not name or not email or not comment:return st.error("Please fill in the form!")
            else:
                st.session_state["commeted"] = True
                threading.Timer(10, setsssts, args=("commeted",False)).start()
            with open(f"./blog/{content}.comment","a+",encoding="utf-8") as f:
                if f.read().split("\x1f").count(comment) >5:st.error("Too many same comments!")
                else:f.write(f"{time.ctime()}| {name} {email}:{comment}\x1f")
        st.text_area("Comment here",key="comment")
        st.text_input("Name",key="name")
        st.text_input("Email",key="email")
        st.button("Submit",on_click=submit,args=(st.session_state["name"],st.session_state["email"],st.session_state["comment"]))

    @staticmethod
    def show_comment(content:str):
        if os.path.isfile(f"./blog/{content}.comment"):
            with open(f"./blog/{content}.comment",encoding="utf-8") as f:
                for comment in f.read().split("\x1f"):
                    if comment:
                        st.markdown("---")
                        st.write(comment)
        else:st.write("No comment")

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
            st.markdown(f"## {item.split('.')[0]}")
            #show cover image if it exists
            image=item.split(".")[0]+".png" \
            if os.path.isfile(f"./blog/{item.split('.')[0]}.png") else item.split(".")[0]+".jpg" \
            if os.path.isfile(f"./blog/{item.split('.')[0]}.jpg") else item.split(".")[0]+".gif" \
            if os.path.isfile(f"./blog/{item.split('.')[0]}.gif") else None
            #============================================
            if image:st.image(f"./blog/{image}",width=200)
            st.markdown(f"**{open(f"./blog/{item}",encoding="utf-8",errors="ignore").read(100)}……**")
            st.button("Read", on_click=show_content, args=(item,), key=item)
    show(file)
    for item in dirs:
        with st.expander(item):
            show([f"./{item}/"+i for i in os.listdir(f"./blog/{item}")])
