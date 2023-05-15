import argparse

from download import download
from play import play

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="\
        A simple CLI for playing the audio from Tiny Desk performances.\n\
        For documentation and more information about tinydeskplayer checkout \
        `https://github.com/bluey31/tiny-desk-player`.\n\n\
        For help with certain subcommands run `tinydesk <SUBCOMMAND> --help`.")

    subparsers = parser.add_subparsers(dest="action")

    download_parser = subparsers.add_parser("download", help="Download the tiny desk audio for a given artist for later playback")
    download_parser.add_argument("artist", help="Artist name")

    play_parser = subparsers.add_parser("play", help="Play the tiny desk of the given artist")
    play_parser.add_argument("artist", help="Artist name")

    args = parser.parse_args()

    artist = args.artist.lower().replace(" ", "+")

    if args.action == "download":
        download(artist)
    elif args.action == "play":
        play(artist)
    else:
        raise Exception(f"Argument '{args.action}' not recognised")
