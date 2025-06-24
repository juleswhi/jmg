#!/bin/python3

import subprocess
import os

def download_playlists_as_mp3(playlist_file, output_directory="downloads"):
    """
    Reads a file with YouTube playlist URLs and downloads them as MP3s
    using yt-dlp into the specified output directory.

    Args:
        playlist_file (str): The path to the file containing playlist URLs (one per line).
        output_directory (str): The directory where the downloaded MP3s will be saved.
                                Defaults to "downloads".
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created output directory: {output_directory}")

    try:
        with open(playlist_file, 'r') as f:
            playlist_urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Playlist file not found at '{playlist_file}'")
        return

    if not playlist_urls:
        print("No playlist URLs found in the file.")
        return

    print(f"Found {len(playlist_urls)} playlists to download.")

    for i, playlist_url in enumerate(playlist_urls):
        print(f"\nDownloading playlist {i+1}/{len(playlist_urls)}: {playlist_url}")

        # Construct the yt-dlp command
        # -o specifies the output template, putting files into subdirectories
        # based on the playlist title and index.
        command = [
            "yt-dlp",
            "--cookies-from-browser", "firefox",
            "-x",  # Extract audio
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", os.path.join(output_directory, "%(playlist)s", "%(playlist_index)s - %(title)s.%(ext)s"),
            playlist_url
        ]

        try:
            # Run the yt-dlp command
            subprocess.run(command, check=True, text=True)
            print(f"Finished downloading playlist: {playlist_url}")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading playlist '{playlist_url}': {e}")
            print(f"Stderr: {e.stderr}")
        except FileNotFoundError:
            print("Error: yt-dlp command not found. Make sure yt-dlp is installed and in your PATH.")
            break
            # Stop processing if yt-dlp isn't found


if __name__ == "__main__":
    playlist_file_name = "playlists.txt"  # Name of the file with playlist links
    output_dir_name = "output" # Name of the output directory

    # Create a dummy playlist file for demonstration if it doesn't exist
    if not os.path.exists(playlist_file_name):
        with open(playlist_file_name, 'w') as f:
            f.write("# Add your YouTube playlist links below, one per line\n")
            f.write("# Example:\n")
            f.write("# https://www.youtube.com/playlist?list=PL some_playlist_id_1\n")
            f.write("# https://www.youtube.com/playlist?list=PL some_playlist_id_2\n")
        print(f"Created a sample '{playlist_file_name}' file. Please add your playlist URLs to it.")
    else:
        download_playlists_as_mp3(playlist_file_name, output_dir_name)

