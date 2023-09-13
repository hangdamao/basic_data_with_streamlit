# @Project ：gui_basicdataservice_with_streamlit
# @File    ：8_👩‍_人物.py
# @Author  ：theQ
# @Date    ：2023/8/15 19:04

import streamlit as st
from common.streamlit_frame import set_api_radio
from common.tools import page_obj_input_parse


def people_page(host):
    # 人物页面
    about_content = "人物"
    prefix = '/people'

    # 标题
    st.title(f" :blue[{about_content}相关] ")

    # 正文内容
    items = page_obj_input_parse(prefix=prefix, host=host)
    set_api_radio(api_items=items)
