import yt_dlp
import os

def download_playlist(playlist_url):
    try:
        # Menentukan direktori utama (folder YoutubePlaylistDownloader)
        current_directory = os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.dirname(current_directory)  # Folder YoutubePlaylistDownloader
        download_folder = os.path.join(parent_directory, 'downloaded_videos')  # Folder untuk menyimpan video

        # Pastikan folder unduhan ada
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Pengaturan untuk yt-dlp
        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Menyimpan video dengan nama file sesuai judul
            'format': 'best',  # Mendownload kualitas terbaik
            'noplaylist': False,  # Mengaktifkan pengunduhan playlist
        }

        # Mengunduh playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

        print("Selesai mengunduh playlist.")
    except Exception as e:
        print(f"Gagal mengunduh playlist. Error: {str(e)}")

if __name__ == "__main__":
    # Masukkan URL playlist YouTube
    playlist_url = input("Masukkan URL playlist YouTube: ")

    # Mengunduh playlist
    download_playlist(playlist_url)
