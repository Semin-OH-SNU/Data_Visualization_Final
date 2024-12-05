import spotipy
from typing import Dict,List
import pandas as pd

"""Get audio_features from Spotify API Query requesting"""

#must get id, secret from "Spotify for Developer" page first.
#register your spotify accounts here: https://developer.spotify.com/dashboard
cid = 'ca54418c3218402b95563af47a745061'
secret = '1fd59395ee214f77ab52c05864bd2860'
redirect_uri = 'http://localhost:8080/callback'
ccm = spotipy.SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=ccm)


def get_audio_features(song_title:str)->Dict:
    query = f"track:{song_title}"
    result = sp.search(q=query, type="track", limit=1)
    
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        track_id = track["id"]  
        audio_features = sp.audio_features(track_id)[0] 
        return audio_features
 

def get_artist_genres(title:str)->Dict:
    result = sp.search(q=f"track:{title}", type="artist", limit=1)
    if result["artists"]["items"]:
        artist = result["artists"]["items"][0]  
        artist_name = artist["name"]
        genres = artist["genres"]  
        return {"artist": artist_name, "genres": genres}


def get_artist_genres_by_track_id(track_id:str)->List:
    track_info = sp.track(track_id)
    artist_id = track_info["artists"][0]["id"]  
    artist_info = sp.artist(artist_id)
    genres = artist_info.get("genres", [])
    return genres


df = pd.read_csv("./ preparation.csv")
for index, row in df.iterrows():
    if not pd.isna(row["danceability"]):
        continue
    features = get_audio_features(row["titles"])
    if not features:
        continue     
    for feature, value in features.items():
        df.at[index, feature] = value


for index, row in df.iterrows():
    if not pd.isna(row["genres"]):
        continue
    features = get_artist_genres_by_track_id(row["id"])
    if not features:
        continue
   
    for feature, value in features.items():
        df.at[index, feature] = value


for index, row in df.iterrows():
    if not pd.isna(row["genres"]):
        continue
    features = get_artist_genres_by_track_id(row["id"])
    if not features:
        continue
   
    df.at[index,"genres"] = features


df.to_csv("./prepared.csv")