# providers/tencent.py

from utils import api_handler
from typing import Optional
from providers.base_provider import BaseProvider

class TencentProvider(BaseProvider):

    def search_song(self, word: str, page: int = 1, num: int = 10) -> list:
        """
           搜索QQ音乐歌曲。

           返回一个歌曲列表，每个元素是一个字典，包含歌曲名、ID等信息。
           """
        params = {
            "word": word,
            "page": page,
            "num": num
        }
        data = api_handler.get_data("/tencent", params)
        if data and data.get("code") == 200:
            # 返回的歌曲列表在 data['data']
            return data["data"]
        return []

    def get_download_url(self, song_id: str, quality: int = 4) -> Optional[str]:
        """
        根据歌曲ID获取下载链接。
        """
        params = {
            "id": song_id,
            "quality": quality
        }
        data = api_handler.get_data("/tencent", params)
        if data and data.get("code") == 200:
            return data["data"]["url"]
        return None

