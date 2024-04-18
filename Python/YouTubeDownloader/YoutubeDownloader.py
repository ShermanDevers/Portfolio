from pytube.cli import on_progress
from pytube import YouTube, Playlist, exceptions
import requests
import urllib


def try_again():
    answer = input("Would you like to try again? (y/n): ")

    if answer in ["y", "Y", "Yes", "yes"]:
        main()
    else:
        print("Goodbye")


def check_yt_link(link):
    try:
        return requests.get(link, timeout=10).status_code
    except exceptions.RegexMatchError:
        print("Missing Characters of a valid link")


def download_vids(vid_list, dl_location):
    invalid_links = []
    print("Downloading Video(s)")
    for link in vid_list:
        if check_yt_link(link) == 200:
            video = YouTube(link, on_progress_callback=on_progress)
            try:
                video.streams.get_highest_resolution().download(dl_location)
                print(f"Successfully downloaded: '{video.title}'.mp4")
            except requests.HTTPError:
                print("These links is were invalid or something is blocked it")
                print("Check if your school or antivirus is blocking it")
                try_again()
            except exceptions.AgeRestrictedError:
                print(f"{video.title}: Age Restricted")
            except urllib.error.HTTPError:
                print("Blocked")
        else:
            print("Blocked or Invalid Link")
            invalid_links.append(link)

    for link in invalid_links:
        print(link)


def download_playlist(playlist_link, dl_location):
    if check_yt_link(playlist_link) != 200:
        print("Link is not valid or something is block it")
        print("Check if your school or antivirus is blocking it")
        try_again()

    playlist = Playlist(playlist_link)

    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download(dl_location)
        except exceptions.AgeRestrictedError:
            print(f"{video.title}: Age Restricted")
        except requests.HTTPError as httpe:
            print(f"Server overload {httpe}")

    print(f"Successfully downloaded {playlist.title}")


def main():
    download_location = input("Where do you want to store your downloads: ")
    video_or_playlist = input("Video(s) or Playlist?: ")
    if video_or_playlist in ["Playlist", "playlist"]:
        link = input("Link of the playlist> ")
        download_playlist(link, download_location)
    elif video_or_playlist in ["Videos", "videos", "Video", "video"]:
        video_amount = int(input("Amount of videos> "))
        video_list = []
        for _ in range(video_amount):
            link = input("Link>")
            video_list.append(link)

        download_vids(video_list, download_location)
    else:
        print("Not an option")
        try_again()


if __name__ == "__main__":
    main()
