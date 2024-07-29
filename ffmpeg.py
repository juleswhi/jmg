import time
import os
import subprocess
import glob
from concurrent.futures import ThreadPoolExecutor
import math

def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

directory_path = 'download_output'

files = glob.glob('output/*')
for f in files:
    os.remove(f)

DEVNULL = open(os.devnull, 'wb')

counter = [0]
total = 1500

def convert_mp4_to_mp3(mp4_file_path):
    filename = os.path.basename(mp4_file_path)
    mp3_filename = filename.split(".mp4")[0] + ".mp3"
    mp3_file_path = os.path.join("output", mp3_filename)
    ffmpeg_command = f'ffmpeg -i "{mp4_file_path}" -vn -acodec libmp3lame -q:a 2 "{mp3_file_path}"'
    subprocess.run(ffmpeg_command, shell=True, stdout=DEVNULL, stderr=DEVNULL)
    counter[0] += 1
    print(f"completed: {truncate((counter[0] / total) * 100, 1)}%")

with ThreadPoolExecutor(max_workers=10) as executor:
    mp4_files = glob.glob(os.path.join(directory_path, '*.mp4'))
    executor.map(convert_mp4_to_mp3, mp4_files)

print("Conversion completed.")

