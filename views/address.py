# @Project ：gui_basicdataservice_with_streamlit
# @File    ：3_🗺️_地址.py
# @Author  ：theQ
# @Date    ：2023/8/18 14:10

import streamlit as st
from common.streamlit_frame import set_api_radio
from common.tools import page_obj_input_parse


def address_page(host):
    # 地址页面
    about_content = "商业"
    prefix = '/business'
    # 标题
    st.title(f" :blue[{about_content}相关] ")

    # 正文内容
    items = page_obj_input_parse(prefix=prefix, host=host)
    set_api_radio(api_items=items)
