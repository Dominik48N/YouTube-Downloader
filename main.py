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
    video_format = input("In which format do you want to download the video? (MP3 or MP4) ")

    if video_format.lower() != "mp4" and video_format.lower() != "mp3":
        print("The video format heard is not available. Please also use mp3 or mp4.")
        pass

    downloadYouTubeVideo()
