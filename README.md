### 📥 **YouTube Playlist Downloader**

#### **Description:**
This Python-based tool allows users to download entire YouTube playlists with a simple command. It uses the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library to fetch and save videos locally for offline viewing.

---

## ⚙️ **Key Features**
- Download full YouTube playlists with a single command.
- Supports multiple video formats like MP4, MKV, etc.
- Simple command-line interface for easy usage.
- Videos are saved in a dedicated folder named `downloaded_videos`.

---

## 📦 **How to Use**

### Step 1: Clone this repository
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/YouTubePlaylistDownloader.git
```

### Step 2: Install Required Libraries
Install the required libraries using `pip`:

```bash
pip install yt-dlp
```

### Step 3: Run the Program
Navigate to the folder where the program is located and run the script:

```bash
python src/downloader.py
```

### Step 4: Enter Playlist URL
When prompted, paste the YouTube playlist URL. The program will download all videos in the playlist.

Example:
```bash
Masukkan URL playlist YouTube: https://www.youtube.com/playlist?list=PL1234567890abcdef
```

### Step 5: Find Your Videos
Downloaded videos will be saved in the `downloaded_videos` folder in the project directory.
