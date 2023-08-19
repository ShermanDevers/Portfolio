from pytube import YouTube, Playlist
import requests
import argparse
import time
import threading


def progress_bar():
    bars_amount = 2
    for i in range(10):
        time.sleep(1)
        bar_progress = "=" * bars_amount
        print(f"\r[{bar_progress}", end="]")
        bars_amount += 2


def download_vids(vid_list, dl_location):
    print("Downloading Video(s)")
    for link in vid_list:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(dl_location)
        print()
        print(f"Successfully downloaded: '{yt.title}'.mp4")


def download_playlist(playlist):
    try:
        vidnum = 0
        for video in playlist:
            ytp = YouTube(video)
            ytp.streams.get_highest_resolution().download("/home/sherman/Videos")
            vidnum += 1
            print(f"Successfully downloaded {vidnum}: {ytp.title}.mp4")
    except requests.HTTPError as httperror:
        print(f"Server overload {httperror}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI program to download YouTube videos and Playlists"
    )
    parser.add_argument(
        "Video_or_Playlist",
        type=str,
        help="Choose whether to download a Video or a Playlist",
    )
    parser.add_argument("videos", nargs="+", type=str, help="URLs of the videos")
    parser.add_argument(
        "Download_location", type=str, help="Where to download the videos (full path)"
    )
    argus = parser.parse_args()

    if argus.Video_or_Playlist in ["Playlist", "playlist"]:
        playlist_link = input("Link to the playlist> ")
        yt_playlist = []
        ytplaylist = Playlist(playlist_link)
        for x in ytplaylist.video_urls:
            yt_playlist.append(x)
            download_playlist(yt_playlist)

    elif argus.Video_or_Playlist in ["Videos", "videos", "Video", "video"]:
        dl_vids_t = threading.Thread(
            target=download_vids, args=[argus.videos, argus.Download_location]
        ).start()
        progress_bar_t = threading.Thread(target=progress_bar).start()

    else:
        print("Not an option")
