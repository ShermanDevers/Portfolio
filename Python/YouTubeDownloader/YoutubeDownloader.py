from pytube import YouTube, Playlist, exceptions
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
    print()


def download_vids(vid_list, dl_location):
    print("Downloading Video(s)")
    for link in vid_list:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(dl_location)
        print()
        print(f"Successfully downloaded: '{yt.title}'.mp4")


def download_playlist(playlist_link, dl_location):
    playlist_link = "".join(playlist_link)
    print(playlist_link)
    playlist = Playlist(playlist_link)
    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download(dl_location)
            progress_bar()
        except exceptions.AgeRestrictedError:
            print(f"{video.title}: Age Restricted")
        except requests.HTTPError as httpe:
            print(f"Server overload {httpe}")
    print(f"Successfully downloaded {playlist.title}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI program to download YouTube videos and Playlists using pytube"
    )
    parser.add_argument(
        "Video_or_Playlist",
        type=str,
        help="Choose whether to download a Video or a Playlist",
    )
    parser.add_argument(
        "videos", nargs="+", type=str, help="URLs of the videos or playlist"
    )
    parser.add_argument(
        "download_location",
        type=str,
        help="Where to download the videos (full path) (For videos. It can create the directory if its not there but for playlists it does not)",
    )
    argus = parser.parse_args()

    if argus.Video_or_Playlist in ["Playlist", "playlist"]:
        download_playlist(argus.videos, argus.download_location)
    elif argus.Video_or_Playlist in ["Videos", "videos", "Video", "video"]:
        dl_vids_t = threading.Thread(
            target=download_vids, args=[argus.videos, argus.download_location]
        ).start()
        progress_bar_t = threading.Thread(target=progress_bar).start()

    else:
        print("Not an option")
