import requests
import logging
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectTimeout, ConnectionError


def requests_run(method, host, api_path, **kwargs):
    """requests接口请求封装"""
    url = host + api_path
    logging.info(f'请求地址：{url}')
    try:
        response = requests.request(method=method, url=url, timeout=5, **kwargs)
        # if 'json' in kwargs:
            # logging.info(f'请求参数：{kwargs.get("json")}')
        # if 'params' in kwargs:
            # logging.info(f'请求参数：{kwargs.get("params")}')
        if response.status_code == 200:
            result = response.json()
            # logging.info(f'接口返回：{result}')
            return result
        else:
            # print(response.status_code)
            return None
    except (ConnectTimeout, ConnectionError):
        return "Error"


if __name__ == '__main__':
    data = {"length": 10, "number": 3}
    res = requests_run(method='POST', host="http://127.0.0.1:5000", api_path="/text/figure", json=data)
    print(res)

    data = {"length": 10, "number": 3}
    res = requests_run(method='POST', host="http://127.0.0.1:5000", api_path="/text/english", json=data)
    print(res)

    data = {"count": 3}
    res = requests_run(method='GET', host="http://127.0.0.1:5000", api_path="/address/chinese/areas", params=data)
    print(res)
