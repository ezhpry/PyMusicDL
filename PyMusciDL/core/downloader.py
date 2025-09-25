# core/downloader.py

import requests
import os
import config
from tqdm import tqdm


def download_file(url: str, filename: str):
    """
    从指定URL下载文件到本地，并显示下载进度。

    参数:
    - url: 文件的下载链接。
    - filename: 保存到本地的文件名。
    """
    # 确保下载目录存在
    if not os.path.exists(config.DOWNLOAD_PATH):
        os.makedirs(config.DOWNLOAD_PATH)

    file_path = os.path.join(config.DOWNLOAD_PATH, filename)

    print(f"正在下载 {filename}...")
    try:
        # 使用 stream=True 启用流式下载，这对于大文件至关重要
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 如果请求不成功，抛出异常

        # 获取文件总大小，如果可能的话
        total_size = int(response.headers.get('content-length', 0))

        # 使用 tqdm 创建一个进度条
        with open(file_path, 'wb') as f, tqdm(
                desc=filename,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            # 逐块写入文件，同时更新进度条
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))

        print(f"下载完成：{file_path}")
        return True

    # 新增的异常处理：当用户按下 Ctrl+C 时
    except KeyboardInterrupt:
        print("\n下载已取消，正在清理不完整的文件...")
        if os.path.exists(file_path):
            os.remove(file_path)
        return False

    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        # 如果下载失败，可以删除已下载的部分文件
        if os.path.exists(file_path):
            os.remove(file_path)
        return False


