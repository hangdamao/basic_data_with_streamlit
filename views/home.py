# @Project ：gui_basicdataservice_with_streamlit
# @File    ：home.py
# @Author  ：theQ
# @Date    ：2023/8/10 14:46


import streamlit as st
from common.tools import get_api_type_list, get_api_path_list, api_DataFrame
from config import api_doc
from streamlit_extras.add_vertical_space import add_vertical_space


def home_page(host):
    # 主页展示
    st.title("基础 _:blue[数据]_ 生成")
    st.caption("测试数据的治理是软件测试的重要话题🐛，如何治理一直是困扰着测试工程师们👨‍💼，本项目旨在解决此:mag:难题，"
               "同时给予更好的用户体验，点击👈左侧侧边栏即可开始")

    # 成果物
    add_vertical_space(1)   # 添加空白行
    st.subheader('成果物🏅')
    st.caption("接口服务及文档📜；GUI🖼️访问系统")
    ip = host.split(':')[1]
    st.markdown(f"""
        - 【Flask接口文档地址】：[api doc]({api_doc})
        - 【Streamlit访问地址】：[streamlit app](https://basicdatawithapp-grnpyvmtrqq36lsfknyxsh.streamlit.app/)
    """)

    # 接口列表
    add_vertical_space(1)  # 添加空白行
    st.subheader('接口清单📃')
    for api_type in get_api_type_list():
        print(api_type)
        format_str = "/" + api_type.split("（")[1].split("）")[0]
        with st.expander(f"**{api_type}**"):
            path_list = get_api_path_list(prefix=format_str)
            print(path_list)

            df = api_DataFrame(prefix=format_str)
            st.dataframe(
                df,
                column_config={
                    "name": "Api Name",
                    "path": "Api Path",
                    "method": "Method",
                    "api_doc": st.column_config.LinkColumn("Api Doc"),
                },
                hide_index=True,
            )

    # 背景
    add_vertical_space(1)  # 添加空白行
    st.subheader('背景🎬')
    st.caption("随着业务的不断发展🍭，测试数据的治理问题越来越难🏝️，为了解决效率及构建测试数据的👿尴尬，故启动该项目")
    st.markdown(f"""
        - 解决光靠测试人员拍脑袋生成测试数据的 _:orange[囧境]_ ；
        - 解决大批量生成测试数据的 _:violet[困难]_ ；
        - 解决测试数据穷举的 _:blue[痛点]_ ；
        - 解决数据类型不够全面的 _:red[问题]_ 。
    """)

    # 思路
    add_vertical_space(1)  # 添加空白行
    st.subheader('思路🎡')
    st.caption("接口服务🚀 & 服务构建🤖 & GUI访问系统🖥️")
    st.markdown(f"""
        - 基于`flask mimesis faker`等构建接口服务
        - 基于`jenkins`构建接口接口服务及GUI服务
        - 基于`streamlit`构建GUI访问系统
    """)

    # 技术细节
    add_vertical_space(1)  # 添加空白行
    st.subheader('技术细节展示👀')
    with st.expander("**:orange[Flask]**"):
        code_flask = '''
            class TextChinese(Resource):

                def __init__(self, **kwargs):
                    self.logger = kwargs.get('logger')
                    self.parser = reqparse.RequestParser()

                def post(self):
                    # 生成中文字符串
                    self.parser.add_argument('number', required=True, location='json', type=int,
                                             help="目标数量不可为空，且必须是int型！")
                    self.parser.add_argument('length', required=True, location='json', type=int, help="长度不可为空，且必须是int型！")
                    param = self.parser.parse_args()
                    self.logger.info("生成指定长度的中文字符串，支持批量生成。")
                    length = param.get("length")
                    number = param.get("number")
                    return return_data(code=StatusCode.SUCCESS.value,
                                       message="操作成功！",
                                       data=[_processes_num(length=length, key="chinese_words") for _ in range(number)])
        '''
        st.code(code_flask, language='python')
    with st.expander("**:green[Mimesiss]**"):
        code_mimesiss = '''
            class MimesisDataProvider(BaseProvider):
                class Meta:
                    name = "mimesis_data_provider"

                @staticmethod
                def get_date():
                    # 获取当前年月日
                    return datetime.datetime.now().strftime('%Y-%m-%d')

                @staticmethod
                def get_timestamp():
                    # 获取当前时间的时间戳
                    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                @staticmethod
                def ulid():
                    # ulid
                    return ulid.new().str

                @staticmethod
                def id():
                    # 身份证
                    faker = Faker(locale="zh_CN")
                    return faker.ssn(min_age=18, max_age=90)

                @staticmethod
                def english_words():
                    # 英文字符串
                    return string.ascii_letters

                @staticmethod
                def digits_words():
                    # 数字字符串
                    return string.digits
        '''
        st.code(code_mimesiss, language='python')
    with st.expander("**:blue[Streamlit]**"):
        code_streamlit = """
                def set_background_img(img='.\\source\\img_1.jpg'):
                # 加载背景图
                img_url = image_to_url(img, width=-3, clamp=False, channels='RGB', output_format='auto', image_id='')
                st.markdown(
                    '''
                    <style>
                    .css-fg4pbf {background-image: url(''' + img_url + ''');};
                </style>
                ''', unsafe_allow_html=True)
        """
        st.code(code_streamlit, language='python')

    # 参考
    add_vertical_space(1)  # 添加空白行
    st.subheader('参考🏷️')
    tab_flask, tab_faker, tab_mimesis, tab_requests, tab_streamlit = st.tabs(
        ['**Flask**', '**Faker**', '**Mimesis**', '**Requests**', '**Streamlit**'])
    # flask
    from flask import Flask

    app = Flask(__name__)
    with tab_flask:
        st.help(app)
    # faker
    from faker import Faker

    with tab_faker:
        st.help(Faker)

    # mimesis
    import mimesis

    with tab_mimesis:
        st.help(mimesis)
    # requests
    import requests

    with tab_requests:
        st.help(requests)
    # streamlit
    with tab_streamlit:
        st.help(st)
