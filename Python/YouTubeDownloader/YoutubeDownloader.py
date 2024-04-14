from pytube import YouTube, Playlist, exceptions
from pytube.cli import on_progress
import requests


def download_vids(vid_list, dl_location):
    print("Downloading Video(s)")
    for link in vid_list:
        yt = YouTube(link, on_progress_callback=on_progress)
        yt.streams.get_highest_resolution().download(dl_location)
        print(f"Successfully downloaded: '{yt.title}'.mp4")


def download_playlist(playlist_link, dl_location):
    playlist = Playlist(playlist_link)
    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download(dl_location)
        except exceptions.AgeRestrictedError:
            print(f"{video.title}: Age Restricted")
        except requests.HTTPError as httpe:
            print(f"Server overload {httpe}")
    print(f"Successfully downloaded {playlist.title}")


if __name__ == "__main__":
    video_or_playlist = input("Video(s) or Playlist?: ")
    download_location = input("Where do you want to store the video?: ")

    if video_or_playlist in ["Playlist", "playlist"]:
        link = input("Link of the playlist> ")
        download_playlist(link, download_location)

    elif video_or_playlist in ["Videos", "videos", "Video", "video"]:
        video_amount = int(input("Amount of videos> "))
        video_list = []

        for i in range(video_amount):
            link = input("Link> ")
            video_list.append(link)

        download_vids(video_list, download_location)
    else:
        print("Not an option")
