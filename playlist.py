import subprocess
f = open("playlists.txt")
data = f.read()

lines = data.splitlines()

# yt-dlp --flat-playlist -i --print-to-file url file.txt "playlist-url"

i = 1
total = lines.__len__()

for line in lines:
    _ = subprocess.run(["yt-dlp", "--flat-playlist", "-i", "--print-to-file", "url", "to_download.txt", line])
    print("**************")
    print(f"Percentage complete: {(i / total) * 100}")
    print("**************")
    i = i + 1

