# @Project ：gui_test 
# @File    ：2222.py
# @Author  ：aircraft carrier
# @Date    ：2023/9/12 19:53

import streamlit as st
from streamlit_option_menu import option_menu

if "menu_5" not in st.session_state:
    st.session_state["menu_5"] = "12345"


def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")


selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        on_change=on_change, key='menu_5', orientation="horizontal")

print(selected5)