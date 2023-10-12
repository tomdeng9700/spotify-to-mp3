from spotify import get_playlist
from youtube import get_video_id
from youtube_to_mp3 import download_video

if __name__ == '__main__':
    playlist_uri = input("Enter the URI for a spotify playlist: ")
    playlist = get_playlist(playlist_uri)
    for song, artists in playlist:
        print(f"Getting Video ID for Track: {song}, Artists: {', '.join(artists)}")
        video_id = get_video_id(song + ' ' + ' '.join(artists))
        if not video_id:
            print("Could not find Video ID, skipping download")
            continue
        
        print(f"Downloading song")
        download_video(video_id)
        print()