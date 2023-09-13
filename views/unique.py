# @Project ：gui_basicdataservice_with_streamlit
# @File    ：12_☘️_其他.py
# @Author  ：theQ
# @Date    ：2023/8/24 18:29

import streamlit as st
from common.streamlit_frame import set_api_radio
from common.tools import page_obj_input_parse


def unique_page(host):
    # 唯一键页面
    about_content = "唯一键"
    prefix = '/unique'

    # 标题
    st.title(f" :blue[{about_content}相关] ")

    # 正文内容
    items = page_obj_input_parse(prefix=prefix, host=host)
    set_api_radio(api_items=items)
