from crewai.tools import tool
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_video_id(YT_URL: str) -> str:
    parsed_url = urlparse(YT_URL)

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    if "shorts" in parsed_url.path:
        return parsed_url.path.split("/")[-1]

    return None


@tool("YouTube Transcript Tool")
def yt_tool(YT_URL: str) -> str:
    """Extract transcript from a YouTube video URL"""

    video_id = extract_video_id(YT_URL)

    if not video_id:
        return "Invalid YouTube URL"

    try:
        transcript_obj = YouTubeTranscriptApi()
        transcript = transcript_obj.fetch(video_id)
        transcript =transcript[:10]

        return " ".join([t.text for t in transcript])

    except Exception as e:
        return f"Error fetching transcript: {str(e)}"