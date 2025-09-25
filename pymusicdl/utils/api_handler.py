# utils/api_handler.py

import requests

import config


def get_data(endpoint:str,params:dict):
    """
    统一处理get请求
    :param endpoint: 平台，如：tencent、netease。
    :param params:
    :return:
    """
    url = f"{config.API_BASE_URL}{endpoint}"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 如果响应状态码不是 2xx，则抛出 HTTPError
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None
    except Exception as e:
        print(f"发生未知错误: {e}")
        return None