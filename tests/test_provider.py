import providers.tencent

def test_tencent_provider():
    tencen_provider = providers.tencent.TencentProvider()
    search_result=tencen_provider.search_song('花海')
    print(f'搜索结果:{search_result}')
    url=tencen_provider.get_download_url(search_result[0]['id'])
    print(f'下载地址:{url}')


test_tencent_provider()