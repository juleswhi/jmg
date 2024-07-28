import os
import subprocess

# Read YouTube links from file
DEVNULL = open(os.devnull, 'wb')
with open('matthew_music', 'r') as file:
    youtube_links = file.readlines()

i = 1
total = youtube_links.__len__()

for link in youtube_links:
    # Download video and extract title
    command = f'yt-dlp -o "matthew-output/%(title)s.%(ext)s" {link.strip()}'
    _ = subprocess.run(command, shell=True, stdout=DEVNULL)
    print("*********************")
    print("")
    print(f"Complete: {i} / {total}, {(i / total) * 100}%")
    print("")
    print("*********************")
    i = i + 1
