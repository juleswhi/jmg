import time
import os
import subprocess

DOWNLOAD_FILE = "download.txt"
FULL_DOWNLOAD_FILE = "download_full.txt"
OUTPUT_DIR = "download_output"

DEVNULL = open(os.devnull, 'wb')

with open(DOWNLOAD_FILE, 'r') as file:
    lines = file.readlines()

i = 1
total_len = lines.__len__()

fdf = open(FULL_DOWNLOAD_FILE, "w")

start_time = time.time()

for line in set(lines):
    if "playlist" in line:
        _ = subprocess.run(["yt-dlp", "--flat-playlist", "-i", "--print-to-file", "url", FULL_DOWNLOAD_FILE, line], stdout=DEVNULL, stderr=DEVNULL)
        print(f"Decompressed Playlist: {line.strip()}")
    else:
        fdf.write(f"{line}")

end_time = time.time()
print(f"Time elapsed for playlist conversion: {end_time - start_time}")
fdf.close()

downloads = open(FULL_DOWNLOAD_FILE, "r")
lines = downloads.readlines()

total_len = lines.__len__()

total_elapsed_time = 0
estimated_elapsed = 0
average_elapsed = 0

for line in lines:
    start = time.time()
    command = f'yt-dlp -o "{OUTPUT_DIR}/%(title)s.%(ext)s" {line.strip()}'
    _ = subprocess.run(command, shell=True, stdout=DEVNULL, stderr=DEVNULL)
    end = time.time()
    if average_elapsed == 0:
        average_elapsed = (end - start)
    else:
        average_elapsed = (average_elapsed + (end - start) ) / 2

    i = i + 1
    print(f"Complete: {i} / {total_len}, {(i / total_len) * 100}%   |   Elapsed: {end - start}   |   Estimated Time Left: {(total_len - i) * average_elapsed}")

print(f"Finished!\n.Mp4 files are located at: {OUTPUT_DIR}")
