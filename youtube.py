import os

# pip install python-dotenv
from dotenv import load_dotenv
# pip install google-api-python-client
from googleapiclient.discovery import build

load_dotenv()

# Set your API key here
api_key = os.getenv("YOUTUBE_DATA_API_KEY")

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_id(search_query):
    # Search for videos
    search_results = youtube.search().list(q=search_query, type='video', part='id', maxResults=1).execute()

    # Extract video ID from the search results
    if 'items' in search_results:
        video = search_results['items'][0]
        video_id = video['id']['videoId']
        return video_id

    return ''