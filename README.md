> This script reads a list of song titles from a text file, searches for these songs on YouTube using the youtubesearchpython library, and downloads the audio tracks as MP3 files using yt-dlp.
> # Searching for Songs: The script uses youtubesearchpython to search for videos on YouTube. It performs searches based on song titles listed in a text file.
>>
> # Downloading and Converting: It then uses yt-dlp to download the audio from the found YouTube videos and converts them to MP3 format.

## Requirements

- Python 3.x
- `yt-dlp` library
- `youtubesearchpython` library
- `ffmpeg` (make sure it's installed and accessible)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

   ```bash
   pip install yt-dlp youtubesearchpython
