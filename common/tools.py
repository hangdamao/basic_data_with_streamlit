# @Project ：gui_basicdataservice_with_streamlit
# @File    ：tools.py
# @Author  ：theQ
# @Date    ：2023/8/11 9:30

import json
import os
import time
import random
from pathlib import Path
import pandas as pd
import streamlit as st
import jsonpath


def now_timestamp():
    # 当前时间的时间戳
    timestamp = time.time()
    str_time = str(timestamp).replace('.', '')
    return str_time


def is_number(s):
    # 判断入参是否能转换为数字
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def is_positive_integer(num):
    # 判断入参是否为正整数
    result = str(num).isdecimal() and int(num) > 0
    if result is True:
        return int(num)
    return False


def format_print(obj):
    '''格式化打印打印数据'''
    if isinstance(obj, (dict, list)):
        res = json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
        return res
    if isinstance(obj, bytes):
        if obj == b'':
            return obj
        res = json.dumps(json.loads(obj), ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
        return res
    if isinstance(obj, str):
        res = json.dumps(json.loads(obj), ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
        return res
    else:
        return None


def project_dir():
    # 获取当前项目的根路径
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return project_dir


def random_a_color():
    # 选择一个扩展框颜色
    colors = ['blue', 'green', 'orange', 'red', 'violet']
    color = random.choice(colors)
    return color


@st.cache_data
def parse_json_file(filename=Path(project_dir(), "source", "基础数据生成服务.openapi.json")):
    # 解析json文件
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        # print(data)
        # print(type(data))
        # format_res = json.dumps(data, indent=4, ensure_ascii=False)
        # print(format_res)
        # print(type(format_res))
        return data


def get_api_type_list():
    # 获取接口分类
    result = parse_json_file()
    type_list = [i.get("name") for i in result.get("tags")]
    return type_list


def get_api_path_list(prefix):
    # 接口path列表
    data = parse_json_file()
    paths = data.get('paths')
    result = paths.keys()
    return list(filter(lambda a: a.startswith(prefix), result))


def api_DataFrame(prefix):
    # 通过openapi.json接口文档构建Streamlit源数据

    data = parse_json_file()
    paths = data.get('paths')
    result = paths.keys()

    def __get_api_method_list():
        # 获取接口的请求方法
        path_list = get_api_path_list(prefix=prefix)
        result = [list(paths.get(path).keys())[0] for path in path_list]
        return result

    def __inner(key, m=True):
        path_list = get_api_path_list(prefix=prefix)
        method_list = __get_api_method_list()
        result = []
        for path, method in zip(path_list, method_list):
            if m is True:
                api_summary = paths.get(path).get(method).get(key)[0:-4]
                result.append(api_summary)
            if m is False:
                api_summary = paths.get(path).get(method).get(key)
                result.append(api_summary)
        return result

    # 构建pandas数据类型
    df = pd.DataFrame(
        {
            "name": __inner(key="summary", m=False),
            "path": get_api_path_list(prefix=prefix),
            "method": __get_api_method_list(),
            "api_doc": __inner(key="x-run-in-apifox", m=True),
        }
    )
    return df


def page_obj_input_parse(prefix, host):
    # 页面对象入参解析
    items = []
    df = api_DataFrame(prefix=prefix)
    data_path = df.path
    data_desc = df.name
    data_method = df.method
    data_api_doc = df.api_doc
    for (api_path, desc, method, api_doc) in zip(data_path, data_desc, data_method, data_api_doc):
        if method == 'get':
            one = dict(host=host,
                       api_path=api_path,
                       desc=desc,
                       input_key=f"input_{api_path}",
                       api_doc=api_doc)
            items.append(one)
        if method == 'post':
            one = dict(host=host,
                       api_path=api_path,
                       desc=desc,
                       input_1_key=f"input_{api_path}_1",
                       input_2_key=f"input_{api_path}_2",
                       api_doc=api_doc)
            items.append(one)
    return items


if __name__ == '__main__':
    # 接口路径列表
    # df = api_DataFrame(prefix='/text')
    # print(df)

    # str = "/car/park/number"
    # format_str = "/" + str.split('/')[1]
    # print(format_str)
    # res = get_api_type_list()[0]
    # print(res)
    # print(dir(res))
    # print(res.split("（")[1].split("）")[0])
    s = "https://app.apifox.com/project/3221202/apis/api-107409280-run"
    # print(s[0:-4])
    page_obj_input_parse(prefix='/text', host="http://127.0.0.1:5000")
