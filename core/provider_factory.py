# core/provider_factory.py

from providers.netease import NeteaseProvider
from providers.tencent import TencentProvider
from typing import Optional

def get_provider(source: str) -> Optional[NeteaseProvider or TencentProvider]:
    """
    根据源名称返回对应的提供者实例。
    """
    providers = {
        "netease": NeteaseProvider(),
        "tencent": TencentProvider()
    }
    return providers.get(source)