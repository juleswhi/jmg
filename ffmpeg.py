import os
import subprocess

# Define the directory containing the MP4 files
directory_path = 'input'

i = 1
total = 941
DEVNULL = open(os.devnull, 'wb')
# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.mp4'):
        # Construct the full file paths for the MP4 and the target MP3
        mp4_file_path = os.path.join(directory_path, filename)

        mp3_filename = os.path.splitext(mp4_file_path)[0] + '.mp3'
        mp3_file_path = os.path.join("/home/juleswhite/projects/music-fr/output", mp3_filename)

        # Construct the ffmpeg command
        ffmpeg_command = f'ffmpeg -i "{mp4_file_path}" -vn -acodec libmp3lame -q:a 2 "{mp3_file_path}"'

        # Execute the ffmpeg command
        _ = subprocess.run(ffmpeg_command, shell=True, stdout=DEVNULL)
        print("****************")
        print("")
        print(f"Processed: {i} / {total} | {(i / total) * 100}%")
        print("")
        print("****************")
        i = i + 1

print("Conversion completed.")

