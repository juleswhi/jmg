import os
import subprocess

DOWNLOAD_FILE = "download.txt"
FULL_DOWNLOAD_FILE = "download_full.tmp"
OUTPUT_DIR = "download_output"

DEVNULL = open(os.devnull, 'wb')

with open(DOWNLOAD_FILE, 'r') as file:
    lines = file.readlines()

i = 1
total_len = lines.__len__()

fdf = open(FULL_DOWNLOAD_FILE, "w")

for line in lines:
    if "playlist" in line:
        _ = subprocess.run(["yt-dlp", "--flat-playlist", "-i", "--print-to-file", "url", FULL_DOWNLOAD_FILE, line])
        print(f"Decompressed Playlist: {line}")
        fdf.write("\n")
    else:
        fdf.write(f"{line}\n")

lines = fdf.readlines()


for line in lines:
    command = f'yt-dlp -o "{OUTPUT_DIR}/%(title)s.%(ext)s" {line.strip()}'
    _ = subprocess.run(command, shell=True, stdout=DEVNULL)
    print("*********************")
    print("")
    print(f"Complete: {i} / {total_len}, {(i / total_len) * 100}%")
    print("")
    print("*********************")
    i = i + 1

print("DONE!")
