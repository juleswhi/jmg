import time
import os
import subprocess

import math
def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

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
        print(f"Extracting songs from: {line.strip()}", end="\r")
        _ = subprocess.run(["yt-dlp", "--flat-playlist", "-i", "--print-to-file", "url", FULL_DOWNLOAD_FILE, line], stdout=DEVNULL, stderr=DEVNULL)
    else:
        fdf.write(f"{line}")

end_time = time.time()
print(f"Time elapsed for playlist conversion: {truncate(end_time - start_time, 0)}")
fdf.close()

downloads = open(FULL_DOWNLOAD_FILE, "r")
lines = downloads.readlines()

total_len = lines.__len__()

total_elapsed_time = 0
estimated_elapsed = 0
average_elapsed = 0

print(f"Songs Found: {total_len}")

for line in set(lines):
    start = time.time()
    command = f'yt-dlp -o "{OUTPUT_DIR}/%(title)s.%(ext)s" {line.strip()}'
    _ = subprocess.run(command, shell=True, stdout=DEVNULL, stderr=DEVNULL)
    end = time.time()
    if average_elapsed == 0:
        average_elapsed = (end - start)
    else:
        average_elapsed = (float(average_elapsed) + float(end - start) ) / 2

    i = i + 1
    estimated_seconds_left = (total_len - i) * average_elapsed
    print(f"Complete: {i} / {total_len}, {truncate((i / total_len) * 100, 1)}%   |   Elapsed: {truncate(end - start, 0)}   |   {truncate(estimated_seconds_left/60,0)}   |   Downloaded: {line.strip()}", end="\r")

print(f"Finished!\n.Mp4 files are located at: {OUTPUT_DIR}")

os.remove(FULL_DOWNLOAD_FILE)
