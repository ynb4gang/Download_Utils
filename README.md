# YouTube Downloader

A simple Python script to download videos, playlists, channels, audio, and video-only streams from YouTube using the Pytube library.

## Features

- Download individual videos
- Download entire playlists
- Download all videos from a channel
- Download audio only from videos
- Download video only (without audio)

## Requirements

- Python 3.x
- Pytube library

## Installation

1. Clone the repository or download the script.
2. Install Pytube:
  ```bash
    pip install pytube
  ```
## Usage
Run the script and follow the prompts:
  ```bash
   python your_script_name.py
  ```
You'll be prompted to choose one of the following options:

*playlist* to download a playlist

*video* to download a video

*channel* to download all videos from a channel

*voice* to download audio only

*picture* to download video only


Then, enter the corresponding URL when prompted.

## Example
To download a video, choose video and enter the URL:
  ``` mathematica
Enter:
'video' to download a video
Your choice: video
Enter the URL of the video:
URL: https://www.youtube.com/watch?v=example
 ```
## Note
Ensure you have the necessary permissions to download the content.
The script saves downloaded files in a folder named after the title of the video or playlist.
