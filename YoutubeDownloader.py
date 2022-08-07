from pytube import YouTube,Playlist
import time,requests
def main():

    vop = str(input("Videos or Playlist> "))
    if vop == 'Playlist' or vop == 'playlist':
        
        playlist_link = input("Link to the playlist> ")
        ytplist = []
        ytplaylist = Playlist(playlist_link)
        for x in ytplaylist.video_urls:
            ytplist.append(x)
        try:
            vidnum = 0
            for video in ytplist:
                ytp = YouTube(video)
                ytpd = ytp.streams.get_highest_resolution()
                ytpd.download('/Users/sd320/OneDrive/Desktop/Yt-downloads')
                print(f'Successfully downloaded {1+vidnum}: {ytp.title}.mp4')
                vidnum += 1
        except requests.HTTPError as httperror:
            print(f'Server overload {httperror}')
        time.sleep(5)

    elif (vop == 'Videos') or (vop =='videos') or (vop =='video') or (vop =='Video'):

        linknum = int(input("How many vids do you want to download> "))
        vidresolution = str(input('What resolution do you want your video(s)> '))
        testlist = []
        for i in range(linknum):
            url = input("Link > ")
            testlist.append(url)
        for x in testlist:
            yt = YouTube(x)
            ytd = yt.streams.get_by_resolution(vidresolution)
            ytd.download('/Users/sd320/OneDrive/Desktop/Yt-downloads')
            print(f'Successfully downloaded: {yt.title}.mp4')
        time.sleep(5)

    else:
        print('Not an option')

if __name__ == '__main__':
    main()