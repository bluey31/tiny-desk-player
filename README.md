# tiny-desk-player
CLI tool to download and play Tiny Desk performances offline. 

I love playing these performances in the background while I code, whether it be at home or in the office. As a result, I wrote this small tool to be able to quickly spin up a terminal window and have them play in the background without the need to open YouTube, search for the right video, etc.

## Installation

So far `tiny-desk-player` is only available on GitHub:

    git clone https://github.com/bluey31/tiny-desk-player.git
    
Install the requirements:

```bash
# tiny-desk-player uses mp4 files under the hood and as a result depends on ffmpeg
brew install ffmpeg 

pip install -r requirements.txt
```
    
##  Quickstart

Play the Harry Styles Tiny Desk:

```python
python3 tiny-desk-player.py play "Harry Styles"
```

Download the Men I Trust Tiny Desk for later playback:

```python
python3 tiny-desk-player.py download "Men I Trust"
```

##  TODO

- [ ] Make what is shown during playback more interesting (dancing table?) 
- [ ] Make TUI for `download` more interesting (progress bar etc) 
- [ ] Add a "live" mode that plays back the stream, without the need to download it first
- [ ] Proper logging and exception handling
