# To download a video from YouTube using Python, you can use the `pytube` library. First, you need to install it by running `pip install pytube` in your Python environment. Then, you can use the following code to download the video specified in your question:


from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=0NRLKM3GZcw&list=RD0NRLKM3GZcw&start_radio=1"
yt = YouTube(video_url)
video = yt.streams.get_highest_resolution()

# Specify the path where you want to save the video
video.download('/path/to/save')

print("Video downloaded successfully!")


# Make sure to replace `/path/to/save` with the actual path where you want to save the video on your computer.
