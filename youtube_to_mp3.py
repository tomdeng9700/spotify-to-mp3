import os
import subprocess

# pip install pytube
from pytube import YouTube

# Define the download location (optional).
download_path = 'music'

# Get the absolute path by joining the current working directory and the relative path.
output_directory = os.path.join(os.getcwd(), download_path)

# Ensure the directory exists; if not, create it.
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def download_video(video_id):
    # Replace 'video_url' with the URL of the YouTube video you want to download audio from.
    video_url = 'https://www.youtube.com/watch?v=' + video_id

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the video's title
    video_title = yt.title

    # Select the audio stream with the desired quality (e.g., highest quality audio stream).
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream.
    audio_file_path = audio_stream.download(output_path=output_directory)

    # Create an MP3 file from the downloaded audio file.
    output_mp3_file = os.path.join(output_directory, f"{video_title}.mp3")

    subprocess.run(['ffmpeg', '-i', audio_file_path, '-q:a', '0', '-map', 'a', output_mp3_file])

    # Remove the original MP4 file.
    os.remove(audio_file_path)

    print("Audio download and conversion to MP3 completed.")