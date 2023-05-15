import os

from pydub import AudioSegment
from pydub.playback import play as play_audio
from download import download


def play(artist: str):
    """
    Finds the tinydesk audio file for the given artist and plays it back
    If the file cannot be found, the user will be asked if they wish to download it and then play it once the download is finished.
    """

    filename = artist + ".mp4"
    
    if os.path.isfile(filename):
        audio = AudioSegment.from_file(filename, format="mp4")
        print(f"Playing Tiny Desk ...")
        return play_audio(audio)
    else:
        choice = input("Tiny Desk Performance not found, do you want to download it? (y/n): ")
        if choice.lower() == "y":
            download(artist)
        else:
            print("Playback cancelled.")