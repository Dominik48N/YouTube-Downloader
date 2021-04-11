from pytube import YouTube
import os


def downloadYouTubeVideo():
    try:
        yt = YouTube(video_url)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        yt.download(download_path)
        print("The video is downloaded!")
    except:
        print("There has been an error. Presumably the video was not found.")


if __name__ == "__main__":
    video_url = input("What is the YouTube video URL? ")
    download_path = input("Please enter the path in which the downloaded YouTube video should be played. ")

    downloadYouTubeVideo()
