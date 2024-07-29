import time
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import math

def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

print("""
___  ___          _        _____           _     _
|  \/  |         (_)      |  __ \         | |   | |
| .  . |_   _ ___ _  ___  | |  \/_ __ __ _| |__ | |__   ___ _ __
| |\/| | | | / __| |/ __| | | __| '__/ _` | '_ \| '_ \ / _ \ '__|
| |  | | |_| \__ \ | (__  | |_\ \ | | (_| | |_) | |_) |  __/ |
\_|  |_/\__,_|___/_|\___|  \____/_|  \__,_|_.__/|_.__/ \___|_|
""")

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
print("")
print(f"Time elapsed for playlist conversion: {truncate(end_time - start_time, 0)}")
fdf.close()

downloads = open(FULL_DOWNLOAD_FILE, "r")
lines = downloads.readlines()

total_len = lines.__len__()

counter = [0]

def download_song(url):
    start = time.time()
    command = f'yt-dlp -o "{OUTPUT_DIR}/%(title)s.%(ext)s" {url.strip()}'
    subprocess.run(command, shell=True, stdout=DEVNULL,stderr=DEVNULL)
    end = time.time()
    counter[0] += 1
    print(f"Downloaded song: {url.strip()}  |  Took: {truncate(end-start,2)}s  |  {counter[0]} out of {total_len}  |  {truncate((counter[0] / total_len) * 100, 1)}%")

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(download_song, set(lines))

os.remove(FULL_DOWNLOAD_FILE)
print(f"Finished!\n.Mp4 files are located at: {OUTPUT_DIR}")
