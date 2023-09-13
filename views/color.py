# @Project ：gui_basicdataservice_with_streamlit
# @File    ：color.py
# @Author  ：theQ
# @Date    ：2023/8/24 18:26

import streamlit as st
from common.streamlit_frame import set_api_radio
from common.tools import page_obj_input_parse


def color_page(host):
    # 颜色页面
    about_content = "颜色"
    prefix = '/color'

    # 标题
    st.title(f" :blue[{about_content}相关] ")

    # 正文内容
    items = page_obj_input_parse(prefix=prefix, host=host)
    set_api_radio(api_items=items)
