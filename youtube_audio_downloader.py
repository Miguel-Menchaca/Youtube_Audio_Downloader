import yt_dlp
import os
from pathlib import Path


def download_youtube_audio(url, output_dir="./downloads", format="mp3", quality="192"):
    """
    Download audio from a YouTube video and save it in the specified format selected by the user.

    Args:
        url (str): The YouTube video URL.
        output_dir (str): Directory to save the audio file.
        format (str): Desired audio format (e.g., 'mp3', 'm4a', 'opus').
        quality (str): Audio quality (e.g., '128', '192', '256', '320').
    """

    # Ensure that the output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Configure the options for yt-dlp
    ydl_opts = {
        'ffmpeg_location': 'C:/ffmpeg', # Ensure that ffmpeg is installed and added to the PATH enviroment variables (If ffmpeg is installed but not in PATH, change the location to your location)
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': quality,
        }],
        'embedmetadata': True,  # Embed metadata (e.g., title, artist) if available
        'writethumbnail': True,  # Download thumbnail
        'postprocessor_args': [
            '-metadata', 'title=%(title)s',
            '-metadata', 'artist=%(uploader)s',
        ],
        'progress_hooks': [progress_hook],  # Track download progress
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed successfully! File saved in {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")


def progress_hook(d):
    """Track download progress."""
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} complete ({d['_speed_str']})")
    elif d['status'] == 'finished':
        print("Processing audio...")


if __name__ == "__main__":
    # Example of usage
    video_url = input("Enter the YouTube video URL: ").strip()
    output_directory = input("Enter output directory (default: './downloads'): ").strip() or "./downloads"
    audio_format = input("Enter audio format (mp3, m4a, opus; default: mp3): ").strip().lower() or "mp3"
    audio_quality = input("Enter audio quality (128, 192, 256, 320; default: 192): ").strip() or "192"

    download_youtube_audio(video_url, output_directory, audio_format, audio_quality)
