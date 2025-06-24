<div align="center">

# MG

Music Grabber

</div>

## Usage

+ Have python3 installed
+ Put all playlist links in "download.txt"
+ Run install.py
+ Output mp3 will be in "output"

```sh
chmod +x install.py
./install.py
```

## Configuring Browser Cookies

There is a high chance that youtube will require you to use your cookies to
download your music.

To fix this, ensure you are logged into youtube on your browser.

Edit the line 6 in `install.py` to point to the browser you are signed in on

```py
BROWSER = "YOUR_BROWSER_HERE"
```
