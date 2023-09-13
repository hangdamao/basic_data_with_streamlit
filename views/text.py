# @Project ：gui_basicdataservice_with_streamlit
# @File    ：9_🅰️_字符串.py
# @Author  ：theQ
# @Date    ：2023/8/15 19:04

import streamlit as st
from common.streamlit_frame import set_api_radio
from common.tools import page_obj_input_parse


def text_page(host):
    # 字符页面
    about_content = "字符串"
    prefix = '/text'

    # 标题
    st.title(f" :blue[{about_content}相关] ")

    # 正文内容
    items = page_obj_input_parse(prefix=prefix, host=host)
    set_api_radio(api_items=items)
