import urllib.request
import json 
import os

from pytube import YouTube, Stream, StreamQuery
from typing import Optional


def download_best_audio_from_id(id: str, artist: str) -> Optional[str]:
    """
    Downloads mp4 file from the YouTube video with the given id.
    download_best_audio_from_id will prioritise downloading the stream with the highest resolution.

    Returns the path of the downloaded file, otherwise returns None.
    """

    url = f"https://www.youtube.com/watch?v={id}"
    filename = artist.replace(" ", "") + ".mp4"

    try:
        yt = YouTube(url)
        audio_streams: StreamQuery = yt.streams.filter(mime_type="audio/mp4", only_audio=True)
        best_stream: Stream = audio_streams.order_by("abr").last()
        audio_file: str = best_stream.download(output_path="tinydesks/", filename=filename)
        return audio_file
    except:
        raise Exception(f"Unable to download audio file from id {id}")

def download(artist: str) -> str:

    """
    Attempts to download the given artists Tiny Desk performance audio in mp4 format.

    Returns the path of the downloaded file, otherwise returns None.
    """

    base_url = "https://www.googleapis.com/youtube/v3"
    tiny_desk_channel_id = "UC4eYXhJI4-7wSWc8UNRwD4A"
    maybe_api_key = os.environ.get("YOUTUBE_API_KEY")
    
    if maybe_api_key is None:
        raise Exception("$YOUTUBE_API_KEY is not set")
    else:
        videos_url = f"{base_url}/search?part=snippet&channelId={tiny_desk_channel_id}&q={artist}&key={maybe_api_key}&maxResults=1"

        try:
            response = urllib.request.urlopen(videos_url)
            data = response.read().decode('utf-8')
            json_data = json.loads(data)

            try:
                video_id_items = json_data["items"]
            except:
                raise Exception(f"Required items not found in response for {artist}, try another artist name")
            
            video_id = video_id_items[0]["id"]["videoId"]
            
            return download_best_audio_from_id(id=video_id, artist=artist)

        except urllib.error.URLError as e:
            raise Exception(f"Error getting URL for the {artist}: {e}")
