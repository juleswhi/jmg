yt-dlp -f bestaudio -o $2 $1
ffmpeg -i $2 -vn -c:a copy $2.ogg
echo done!
