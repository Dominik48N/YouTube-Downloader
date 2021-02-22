from pytube import YouTube
import os


def downloadYouTubeVideo(videoUrl, downloadPath):
    try:
        yt = YouTube(videoUrl)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if not os.path.exists(downloadPath):
            os.makedirs(downloadPath)

        yt.download(downloadPath)
        print("The video is downloaded!")
    except:
        print("There has been an error. Presumably the video was not found.")


if __name__ == "__main__":
    videoUrl = input("What is the YouTube video URL? ")
    downloadPath = input("Please enter the path in which the downloaded YouTube video should be played. ")

    downloadYouTubeVideo(videoUrl, downloadPath)
