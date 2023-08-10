from pytube import YouTube, Playlist
import requests
import argparse

def download_vids(vid_list):
    for link in vid_list:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download("/home/sherman/Videos")
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

    parser = argparse.ArgumentParser(description="CLI program to download YouTube videos and Playlists")
    parser.add_argument("Video_or_Playlist",type=str,help="Choose whether to download a Video or a Playlist")
    parser.add_argument("videos",nargs="+",type=str,help="URLs of the videos")
    args = parser.parse_args()
    pass
    if args.Video_or_Playlist in ["Playlist", "playlist"]:

        playlist_link = input("Link to the playlist> ")
        yt_playlist = []
        ytplaylist = Playlist(playlist_link)
        for x in ytplaylist.video_urls:
            yt_playlist.append(x)
            download_playlist(yt_playlist)

    elif args.Video_or_Playlist in ["Videos", "videos", "Video", "video"]:

        
        download_vids(args.videos)

    else:
        print("Not an option")
