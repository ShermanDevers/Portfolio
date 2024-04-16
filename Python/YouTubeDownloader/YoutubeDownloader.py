import requests
from pytube import YouTube, Playlist, exceptions
from pytube.cli import on_progress

def try_again():
    answer = input("Would you like to try again? (y/n): ")

    if answer in ["y","Y","Yes","yes"]:
        choice_of_download()
    else:
        print("Goodbye")

def check_yt_link(link): 
	try:
    	return requests.get(link).status_code == 200 or requests.get(link).status_code == 400
	except pytube.exceptions.RegexMatchError:
		print("Missing Characters of a valid link")
        
def download_vids(vid_list, dl_location):
    invalid_links = []
    print("Downloading Video(s)")
    for link in vid_list:
        if check_yt_link(link) is True:
          print("Good Link")
          video = YouTube(link, on_progress_callback=on_progress)
          video.streams.get_highest_resolution().download(dl_location)
          print(f"Successfully downloaded: '{video.title}'.mp4")
        else:
            print("Blocked or Invalid Link")
            invalid_links.append(link)

    for link in invalid_links:
        print(link)

    print("These links is were invalid or something is blocked it")
    print("Check if your school or antivirus is blocking it")
    try_again() 

def download_playlist(playlist_link, dl_location):
    if check_link(playlist_link) is False:
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


def add_link():
    link = input("Link> ")
    if "https://www.youtube.com/watch?v=" in link or "https://youtube.com/watch?v=" in link:
        video_list.append(link)
    else:
        not_youtube = input("Not a youtube link, would you like to enter another (y/n): ")
        if not_youtube in ["y","Y","yes","Yes"]:
            add_link()


def choice_of_download():
    
    video_or_playlist = input("Video(s) or Playlist?: ")
    if video_or_playlist in ["Playlist", "playlist"]:
        link = input("Link of the playlist> ")
        download_playlist(link, download_location)
    elif video_or_playlist in ["Videos", "videos", "Video", "video"]:
        video_amount = int(input("Amount of videos> "))
        for _ in range(video_amount):
            add_link()

        download_vids(video_list, download_location)
    else:
        print("Not an option")
        try_again()


if __name__ == "__main__":
    global video_list
    video_list = []
    download_location = input("Where do you want to store your downloads: ")
    choice_of_download()
