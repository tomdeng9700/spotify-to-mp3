from spotify import get_playlist
from youtube import get_video_id
from youtube_to_mp3 import download_video

# for track in playlist['items']:
#     track_name = track['track']['name']
#     artists = [artist['name'] for artist in track['track']['artists']]
#     print(f"Track: {track_name}, Artists: {', '.join(artists)}")

if __name__ == '__main__':
    playlist = get_playlist('https://open.spotify.com/playlist/2B17v6HfMJPIgHcOhMYnSd?si=2008c80328734a4f')
    for song, artists in playlist:
        print(f"Getting Video ID for Track: {song}, Artists: {', '.join(artists)}")
        video_id = get_video_id(song + ' ' + ' '.join(artists))
        if not video_id:
            print("Could not find Video ID, skipping download")
            continue
        
        print(f"Downloading song")
        download_video(video_id)
        print()