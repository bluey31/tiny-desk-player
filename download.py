import urllib.request
import json 
import os

from pytube import YouTube, Stream, StreamQuery

def download_best_audio_from_id(id: str, artist: str) -> str:
    """
    Downloads mp4 file from the YouTube video with the given id.
    download_best_audio_from_id will prioritise downloading the stream with the highest resolution.

    Returns the path of the downloaded file, if successful.
    Can raise Exception if unable to download audio file from the given id.
    """

    url = f"https://www.youtube.com/watch?v={id}"
    filename = artist + ".mp4"

    try:
        yt = YouTube(url)
        audio_streams: StreamQuery = yt.streams.filter(mime_type="audio/mp4", only_audio=True)
        best_stream: Stream = audio_streams.order_by("abr").last()
        audio_file: str = best_stream.download(output_path="tinydesks/", filename=filename)
        return audio_file
    except:
        raise Exception(f"Unable to download audio file from id {id}")

def get_desired_video_id_from_search_url(search_url: str) -> str:
    try:
        response = urllib.request.urlopen(search_url)
        data = response.read().decode('utf-8')
        json_data = json.loads(data)
        video_id_items = json_data["items"]
        return video_id_items[0]["id"]["videoId"]
    except:
        raise Exception(f"Cannot get specific video id, required items not found in response")
    
def download(artist: str) -> str:
    """
    Attempts to download the given artists Tiny Desk performance audio in mp4 format.

    Returns the path of the downloaded file, if successful.
    Can raise Exception if unable to download audio file from the given id.
    """

    filename = "./tinydesks/" + artist + ".mp4"
    
    if not os.path.isfile(filename):
        base_url = "https://www.googleapis.com/youtube/v3"
        tiny_desk_channel_id = "UC4eYXhJI4-7wSWc8UNRwD4A"
        maybe_api_key = os.environ.get("YOUTUBE_API_KEY")
        
        if maybe_api_key is None:
            raise Exception("Unable to download audio: environment variable YOUTUBE_API_KEY is not set")
        else:
            videos_url = f"{base_url}/search?part=snippet&channelId={tiny_desk_channel_id}&q={artist}&key={maybe_api_key}&maxResults=1"

            try:
                video_id = get_desired_video_id_from_search_url(videos_url)
                return download_best_audio_from_id(id=video_id, artist=artist)

            except urllib.error.URLError as e:
                raise Exception(f"Error getting audio for the {artist}: {e}")
    else:
        print("Tiny Desk already available, cancelling download.")
