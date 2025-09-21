# main.py
import argparse
from core import downloader, provider_factory

def main():
    parser = argparse.ArgumentParser(description="音乐下载")
    parser.add_argument("--word", "-w", required=True, help="要搜索的歌曲名")
    parser.add_argument("--source", "-s", required=True, choices=["netease", "tencent"],
                        help="音乐源，支持 netease 或 tencent")

    args = parser.parse_args()

    provider = provider_factory.get_provider(args.source)
    if not provider:
        print("不支持的音乐源。")
        return

    # 1. 搜索歌曲
    print(f"正在搜索来自 {args.source} 的歌曲：{args.word}...")
    songs = provider.search_song(word=args.word)

    if not songs:
        print("未找到歌曲。")
        return

    # 展示搜索结果
    print("\n搜索结果:")
    # 限制只显示前10个结果，以防列表过长
    for i, song in enumerate(songs[:10], 1):
        song_name = song.get("song", "未知歌曲")
        artist = song.get("singer", "未知歌手")
        print(f"  {i}. {song_name} - {artist}")

    # 2. 接收用户输入
    try:
        choice = int(input("\n请输入要下载歌曲的序号："))
        # 验证用户输入是否在有效范围内
        chosen_index = choice - 1
        if not (0 <= chosen_index < len(songs)):
            print("选择的序号无效。")
            return
    except (ValueError, IndexError):
        print("输入无效，请确保输入一个数字。")
        return

    # 3. 根据用户选择的序号获取下载 URL
    selected_song = songs[chosen_index]
    song_id = selected_song.get("id")

    if not song_id:
        print(f"选中的歌曲 {selected_song.get('song')} 没有有效的ID。")
        return

    print(f"\n已选择歌曲：{selected_song.get('song')} (ID: {song_id})")

    print("正在获取下载链接...")
    download_url = provider.get_download_url(song_id, quality=9)
    if not download_url:
        print("获取下载链接失败，请检查歌曲ID或音质设置。")
        return

    # 4. 下载音乐文件
    song_name = selected_song.get('song', '未知歌曲')
    artist_name = selected_song.get('singer', '未知歌手')
    filename = f"{song_name} - {artist_name}.mp3"
    filename = "".join(x for x in filename if x.isalnum() or x in " -_.").strip()

    print(f"获取到下载链接，准备下载文件：{filename}")
    downloader.download_file(download_url, filename)


if __name__ == "__main__":
    main()