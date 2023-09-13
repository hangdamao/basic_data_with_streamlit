# @Project ：gui_basicdataservice_with_streamlit
# @File    ：device.py
# @Author  ：theQ
# @Date    ：2023/8/24 18:27

import streamlit as st
from common.streamlit_frame import set_api_radio
from common.tools import page_obj_input_parse


def device_page(host):
    # 设备页面
    about_content = "设备"
    prefix = '/device'

    # 标题
    st.title(f" :blue[{about_content}相关] ")

    # 正文内容
    items = page_obj_input_parse(prefix=prefix, host=host)
    set_api_radio(api_items=items)
