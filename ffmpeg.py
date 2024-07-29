import time
import os
import subprocess
import glob

# Define the directory containing the MP4 files
directory_path = 'download_output'

import math
def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

files = glob.glob('output/*')
for f in files:
    os.remove(f)

i = 1
total = 1000
DEVNULL = open(os.devnull, 'wb')
for filename in os.listdir(directory_path):
    if filename.endswith('.mp4'):
        start = time.time()
        mp4_file_path = os.path.join(directory_path, filename)

        mp3_filename = filename.split(".mp4")[0] + ".mp3"
        mp3_file_path = os.path.join("output", mp3_filename)
        ffmpeg_command = f'ffmpeg -i "{mp4_file_path}" -vn -acodec libmp3lame -q:a 2 "{mp3_file_path}"'

        _ = subprocess.run(ffmpeg_command, shell=True, stdout=DEVNULL,stderr=DEVNULL)
        i = i + 1
        end = time.time()
        print(f"Processed: {i} / {total}  |  {(i / total) * 100}%  |  Time Taken: {truncate(end - start, 2)}  |  Saved: {mp3_file_path}")

print("Conversion completed.")
