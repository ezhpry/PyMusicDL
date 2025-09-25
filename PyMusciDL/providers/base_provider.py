# providers/base_provider.py
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class BaseProvider(ABC):
    """
    所有音乐源提供者的抽象基类。
    定义了所有子类必须实现的接口。
    """

    @abstractmethod
    def search_song(self, word: str) -> List[Dict[str, Any]]:
        """根据关键词搜索歌曲"""
        pass

    @abstractmethod
    def get_download_url(self, song_id: int, quality: int) -> Optional[str]:
        """根据歌曲ID和音质获取下载链接"""
        pass