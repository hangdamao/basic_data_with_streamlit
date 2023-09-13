import streamlit as st
from PIL import Image
from common.requests_base import requests_run
from streamlit.elements.image import image_to_url
from common.tools import is_positive_integer, format_print, project_dir
import logging
from pathlib import Path


def sever_fail_page():
    # 服务器报错页面
    logging.info("服务未启动 ！")
    st.toast('连接到 **_:red[服务器]_** 失败!', icon='🎉')
    st.snow()
    image = Image.open(Path(project_dir(), "source", "dft.jpg"))
    st.image(image, caption='Oh My God !')
    st.header("人生如 _:orange[梦]_，你要做的就是不断 _:red[追逐]_ ！")
    st.stop()


def service_status_check(host, opt_obj):
    # 目标服务状态检查
    res = requests_run(host=host, api_path='/home/', method='GET')
    if res is None:
        opt_obj.error('目标服务未启动 ！', icon="🚨")
        return False
    if res == "Error":
        opt_obj.error('目标服务未启动 ！', icon="🚨")
        return False
    if res.get("service_state") == "OK":
        opt_obj.success('目标服务器正常~', icon="✅")
        print("服务正常！")
        # st.balloons()
        return True


def set_sidebar(local_host, test_host):
    # 设置侧边栏
    sid = st.sidebar

    # sid.title('基础数据服务')
    local = f'本地服务（{local_host}）'
    test = f'测试服务（{test_host}）'
    sid.write(" **:blue[请选择服务器：]** ")
    select_serve = sid.selectbox('请选择服务器', (local, test),
                                 index=1,
                                 help="所选服务器地址即为页面接口的访问地址！",
                                 label_visibility="collapsed")
    # 链接服务器状态条
    if select_serve == local:
        if service_status_check(host=local_host, opt_obj=sid) is True:
            # st.toast('连接到 **_:green[本地服务]_** 成功!', icon='🎉')
            logging.info(f"当前为【{select_serve}】：{local_host}")
            return local_host
        else:
            return False
    elif select_serve == test:
        if service_status_check(host=test_host, opt_obj=sid) is True:
            # st.toast('连接到 **_:green[测试服务]_** 成功!', icon='🎉')
            logging.info(f"当前为【{select_serve}】：{test_host}")
            return test_host
        else:
            return False
    else:
        pass


def set_background_img(img=Path(project_dir(), "source", "img_1.jpg")):
    # 加载背景图
    img_url = image_to_url(img, width=-3, clamp=False, channels='RGB', output_format='auto', image_id='')
    st.markdown(
        '''
        <style>
        .css-fg4pbf {background-image: url(''' + img_url + ''');};
    </style>
    ''', unsafe_allow_html=True)


@st.cache_resource
def get_audio_bytes():
    audio_file = open(Path(project_dir(), "source", "周杰伦-稻香.mp3"), 'rb')
    audio_bytes = audio_file.read()
    audio_file.close()
    return audio_bytes


def send_get_request_and_show_response(host, api_path, count):
    """发送get请求并展示结果"""
    with st.spinner('加载中...'):
        # if is_positive_integer(num) is True:
        data = {"count": count}
        res = requests_run(method='GET', host=host, api_path=api_path, params=data)
        # print(f'get==============={res}')
        if res.get("code") == "0000":
            st.write(" **:blue[请求地址如下：]** ")
            st.code(host + api_path + f"?count={count}", 'Shell')
            # 展示正确的返回结果
            st.write(" **:blue[返回参数如下：]** ")
            # st.json(data)
            st.code(format_print(res), 'JSON')
            st.toast(':green[成功!]', icon='🎉')
            # st.success('请求成功 !')
        elif res.get("code") == "0001":
            st.warning(res.get("message"), icon="⚠️")
        else:
            e = RuntimeError('This is an exception of type RuntimeError')
            st.exception(e)


def send_post_request_and_show_response(host, api_path, length, count):
    """发送get请求并展示结果"""
    with st.spinner('加载中...'):
        # if is_positive_integer(length) and is_positive_integer(count) is True:
        data = {"length": length, "number": count}
        res = requests_run(method='POST', host=host, api_path=api_path, json=data)
        # print(f'post==============={res}')
        if res.get("code") == "0000":
            st.write(" **:blue[请求地址如下：]** ")
            st.code(host + api_path, 'Shell')
            # 展示正确的返回结果
            st.write(" **:blue[返回参数如下：]** ")
            # st.json(data)
            st.code(format_print(res), 'JSON')
            st.toast(':green[成功!]', icon='🎉')
            # st.success('请求成功 !')
        elif res.get("code") == "0001":
            st.warning(res.get("message"), icon="⚠️")
        else:
            e = RuntimeError('This is an exception of type RuntimeError')
            st.exception(e)
    # else:
    #     st.warning('请输入正确的数据类型，仅支持正整数！', icon="⚠️")


def get_show(host, api_path, desc, input_key, api_doc):
    """接口请求为get，且请求路径中包含参数个数的展示方式"""
    logging.info(f'本次请求的接口为：{api_path}')
    with st.form(desc):
        st.write(" **:blue[接口文档地址为：]** ")
        st.code(api_doc)
        st.write(" **:blue[请输入数量：]** ")
        count = st.text_input(label="数量",
                              max_chars=3,
                              key=input_key,
                              placeholder="请填写正参数...",
                              label_visibility='collapsed')
        # logging.info(f'本次请求数量为---：{count}')
        # 提交按钮
        button = st.form_submit_button("submit", help="点击后调用接口", type="primary")
        if button:
            input_value = is_positive_integer(count)
            if count == '' or input_value is False:
                st.warning('请输入正确的数据类型，仅支持正整数！', icon="⚠️")
            else:
                send_get_request_and_show_response(host=host, api_path=api_path, count=input_value)


def post_show(host, api_path, desc, input_1_key, input_2_key, api_doc):
    """接口请求为post，且请求路径中包含参数个数的展示方式"""
    logging.info(f'本次请求的接口为：{api_path}')
    with st.form(desc):
        st.write(" **:blue[接口文档地址为：]** ")
        st.code(api_doc)
        st.write(" **:blue[请输入长度：]** ")
        length = st.text_input(label="长度",
                               max_chars=3,
                               key=input_1_key,
                               placeholder="请填写正参数...",
                               label_visibility='collapsed')
        # logging.info(f'本次请求长度为---：{length}')
        st.write(" **:blue[请输入数量：]** ")
        number = st.text_input(label="数量",
                               max_chars=3,
                               key=input_2_key,
                               placeholder="请填写正参数...",
                               label_visibility='collapsed')
        # logging.info(f'本次请求数量为---：{number}')
        # 提交按钮
        button = st.form_submit_button("submit", help="点击后调用接口", type="primary")
        if button:
            input_value_1 = is_positive_integer(length)
            input_value_2 = is_positive_integer(number)
            if (length == '' and number == '') or input_value_1 is False or input_value_2 is False:
                st.warning('请输入正确的数据类型，仅支持正整数！', icon="⚠️")
            else:
                send_post_request_and_show_response(host=host, api_path=api_path, length=input_value_1,
                                                    count=input_value_2)


def set_api_radio(api_items):
    # 选择接口
    one_tuple = (i.get('desc') for i in api_items)
    # st.write(" **:blue[请选择目标接口：]** ")
    with st.expander(" **:blue[请选择目标接口：]** ", expanded=True):
        radio = st.radio("请选择接口：", one_tuple, label_visibility="collapsed")
    # 入参处理
    for api in api_items:
        if radio == api.get('desc'):
            host = api.get('host')
            api_path = api.get('api_path')
            desc = api.get('desc')
            api_doc = api.get('api_doc')
            if 'input_key' in api:
                input_key = api.get('input_key')
                get_show(host, api_path, desc, input_key, api_doc)
            if 'input_1_key' and 'input_2_key' in api:
                input_1_key = api.get('input_1_key')
                input_2_key = api.get('input_2_key')
                post_show(host, api_path, desc, input_1_key, input_2_key, api_doc)
