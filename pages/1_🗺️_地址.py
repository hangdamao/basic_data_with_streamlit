# @Project ：gui_basicdataservice_with_streamlit
# @File    ：3_🗺️_地址.py
# @Author  ：theQ
# @Date    ：2023/8/18 14:10

import streamlit as st
from common.streamlit_frame import set_sidebar, set_api_radio
import logging
from common.tools import page_obj_input_parse
from config import get_help_url, report_a_bug_url, locale_host, test_host, about_text, layout, initial_sidebar_state

about_content = "地址"
prefix = '/address'

# 设置页面基础信息
st.set_page_config(
    page_title=about_content,
    page_icon="🗺️",
    layout=layout,
    initial_sidebar_state=initial_sidebar_state,
    menu_items={
        "Get Help": get_help_url,
        "Report a bug": report_a_bug_url,
        "About": about_text
    })

# 设置全局变量
if "locale_host" not in st.session_state:
    st.session_state.locale_host = locale_host
if "test_host" not in st.session_state:
    st.session_state.test_host = test_host

# 选择目标服务器
host = set_sidebar(st.session_state.locale_host, st.session_state.test_host)
logging.info(f"本次请求服务为：{host}")

# 标题
st.title(f" :blue[{about_content}相关] ")

# 正文内容
items = page_obj_input_parse(prefix=prefix, host=host)
set_api_radio(api_items=items)
