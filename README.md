# Youtube_Audio_Downloader
![Python Logo](https://img.shields.io/badge/Python-3.12%252B-blue)
![MIT Logo](https://img.shields.io/badge/License-MIT-green)


A Python script to download audio from YouTube videos in various formats and quality settings. This tool utilizes `yt-dlp` to extract and convert audio, embedding metadata and the video thumbnail with the final audio file.

## Features

-   Download audio from any YouTube video URL.
-   Choose from multiple audio formats (e.g., `mp3`, `m4a`, `opus`).
-   Select the desired audio quality (bitrate).
-   Saves files to a user-specified directory.
-   Automatically embeds metadata like title and artist into the audio file.
-   Downloads and embeds the video thumbnail.
-   Displays real-time download progress.

## Prerequisites

Before you begin, ensure you have the following installed:

-   [Python 3+](https://www.python.org/downloads/)
-   [FFmpeg](https://ffmpeg.org/download.html): This is required for audio processing and conversion. You must either add FFmpeg to your system's PATH environment variable or update the path in the `youtube_audio_downloader.py` script.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/miguel-menchaca/youtube_audio_downloader.git
    cd youtube_audio_downloader
    ```

2.  **Install the required Python package:**
    ```bash
    pip install yt_dlp
    ```

3.  **Install FFmpeg:**
    -   Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
    -   Extract the files to a location on your computer (e.g., `C:/ffmpeg`).
    -   **Important:** Either add the `bin` directory of your FFmpeg installation to your system's PATH or update the `ffmpeg_location` variable in `youtube_audio_downloader.py` to point to your FFmpeg executable's location.

    ```python
    # In youtube_audio_downloader.py
    ydl_opts = {
        'ffmpeg_location': 'C:/ffmpeg', # Change this path if needed
        # ...
    }
    ```

## Usage

Run the script from your terminal:

```bash
python youtube_audio_downloader.py
```

The script will prompt you for the following information:
1.  **YouTube video URL:** The full URL of the video you want to download audio from.
2.  **Output directory:** The folder where the audio file will be saved. Defaults to `./downloads`.
3.  **Audio format:** The desired audio format. Defaults to `mp3`.
4.  **Audio quality:** The desired audio bitrate. Defaults to `192`.

### Example

```bash
$ python youtube_audio_downloader.py
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter output directory (default: './downloads'): my_music
Enter audio format (mp3, m4a, opus; default: mp3): mp3
Enter audio quality (128, 192, 256, 320; default: 192): 320
Downloading: 100.0% complete (2.50MiB/s)
Processing audio...
Download completed successfully! File saved in my_music
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. The developers are not responsible for how users employ this tool. Downloading copyrighted material without permission may violate terms of service and copyright laws in your country.
