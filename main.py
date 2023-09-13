# @Project ：gui_test 
# @File    ：main.py
# @Author  ：aircraft carrier
# @Date    ：2023/9/12 16:08

import streamlit as st
from streamlit_option_menu import option_menu
from common.log_base import config_flask_log
from common.streamlit_frame import get_audio_bytes, set_sidebar, sever_fail_page
from config import (get_help_url, report_a_bug_url, locale_host, test_host, about_text, layout, initial_sidebar_state)
from views.home import home_page
from views.address import address_page
from views.business import business_page
from views.car import car_page
from views.color import color_page
from views.company import company_page
from views.device import device_page
from views.house import house_page
from views.other import other_page
from views.people import people_page
from views.text import text_page
from views.time import time_page
from views.unique import unique_page


# 设置全局变量
if "locale_host" not in st.session_state:
    st.session_state.locale_host = locale_host
if "test_host" not in st.session_state:
    st.session_state.test_host = test_host
if "page_title" not in st.session_state:
    st.session_state.page_title = "主页"
if "page_icon" not in st.session_state:
    st.session_state.page_icon = "🏠"

# 页面设置
st.set_page_config(
    page_title=st.session_state["page_title"],
    page_icon=st.session_state["page_icon"],
    layout=layout,
    initial_sidebar_state=initial_sidebar_state,
    menu_items={
        'Get Help': get_help_url,
        'Report a bug': report_a_bug_url,
        'About': about_text
    })

# 设置日志
config_flask_log()




def page_params(key):
    # 设置主页参数
    selection = st.session_state[key]
    if selection == "地址":
        st.session_state["page_icon"] = "🗺️"
    if selection == "商业":
        st.session_state["page_icon"] = "🎢"
    if selection == "汽车":
        st.session_state["page_icon"] = "🚗"
    if selection == "颜色":
        st.session_state["page_icon"] = "🥝"
    if selection == "公司":
        st.session_state["page_icon"] = "💼"
    if selection == "设备":
        st.session_state["page_icon"] = "🚆"
    if selection == "房屋":
        st.session_state["page_icon"] = "🏟️"
    if selection == "人物":
        st.session_state["page_icon"] = "👩"
    if selection == "字符串":
        st.session_state["page_icon"] = "🅰️"
    if selection == "时间":
        st.session_state["page_icon"] = "⏲️"
    if selection == "唯一键":
        st.session_state["page_icon"] = "📍"
    if selection == "其他":
        st.session_state["page_icon"] = "☘️"


# 设置侧边栏
with st.sidebar:
    # 设置目录选项
    choose = option_menu(menu_title="目录",
                         menu_icon="slack",
                         options=["主页", "地址", "商业", "汽车", "颜色", "公司", "设备", "房屋", "人物", "字符串", "时间", "唯一键", "其他"],
                         icons=["house", "geo-alt-fill", "cart4", "car-front-fill", "palette", "briefcase-fill",
                                "device-hdd", "house-heart-fill", "people", "file-earmark-font", "alarm", "1-circle",
                                "tag"],
                         default_index=0,
                         # styles={
                         #     "container": {"padding": "0!important", "background-color": "#fafafa",
                         #                   "font-family": "Permanent Marker"},
                         #     "icon": {"color": "orange", "font-size": "25px"},
                         #     "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px",
                         #                  "--hover-color": "#eee"},
                         #     "nav-link-selected": {"background-color": "green"},
                         # },
                         key="page_title",
                         on_change=page_params
                         )
    # 设置服务器地址
    host = set_sidebar(local_host=st.session_state.locale_host, test_host=st.session_state.test_host)
    # 设置音乐
    st.write(f' :musical_note: 周杰伦-稻香.mp3 正在播放...')
    st.audio(get_audio_bytes(), format='audio/mp3')

print(f"================================{choose}")

# 判断服务器是否正常
if host is False:
    sever_fail_page()

# 主页显示
if choose == "主页":
    home_page(host)

# 地址页面显示
if choose == "地址":
    address_page(host)

# 地址页面显示
if choose == "商业":
    business_page(host)

# 汽车页面
if choose == "汽车":
    car_page(host)

# 颜色页面
if choose == "颜色":
    color_page(host)

# 公司页面
if choose == "公司":
    company_page(host)

# 设备页面
if choose == "设备":
    device_page(host)

# 房屋页面
if choose == "房屋":
    house_page(host)

# 人物页面
if choose == "人物":
    people_page(host)

# 字符传页面
if choose == "字符串":
    text_page(host)

# 时间页面
if choose == "时间":
    time_page(host)

# 唯一键页面
if choose == "唯一键":
    unique_page(host)

# 其他页面
if choose == "其他":
    other_page(host)